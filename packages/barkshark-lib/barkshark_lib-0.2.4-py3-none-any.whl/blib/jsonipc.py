from __future__ import annotations

import asyncio
import inspect
import traceback

from collections.abc import Awaitable, Callable
from json.decoder import JSONDecodeError
from typing import Any, Self

from .date import Date
from .misc import JsonBase, random_str
from .path import File
from .transport import AsyncTransport


class IpcMessage:
	"Represents an IPC message"

	id: str
	transport: AsyncTransport

	__slots__ = (
		"created",
		"data",
		"id",
		"message",
		"no_return",
		"server",
		"transport",
		"type"
	)


	def __init__(self,
				type: str,
				data: dict[str, Any] | None = None,
				message: str | None = None,
				no_return: bool = False) -> None:
		"""
			Create a new message

			:param type: Message type to create. Use ``response`` for a normal response and
				``error`` for an error response.
			:param data: :class:`dict` to send with the message
			:param message: Optional user-readable message text
		"""

		self.type: str = type
		self.data: dict[str, Any] | None = data
		self.message: str | None = message
		self.no_return: bool = no_return
		self.created: Date = Date.new_utc()


	def __repr__(self) -> str:
		parts = [
			repr(self.type),
			repr(self.id),
			f"data={repr(self.data)}",
			f"message={repr(self.message)}"
		]

		return f"IpcMessage({', '.join(parts)})"


	@classmethod
	def new_error(cls: type[Self], message: str) -> Self:
		"""
			Create a new error message

			:param message: Text of the error
		"""

		return cls("error", None, message)


	@classmethod
	def parse(cls: type[Self], raw_data: Any) -> Self:
		"""
			Parse JSON data into an :class:`IpcMessage` object

			:param raw_data: Data to parse. Can be a :class:`bytes`, :class:`str`, or :class:`dict`
				object.
		"""

		data: JsonBase[Any] = JsonBase.parse(raw_data)
		id = data.pop("id")

		msg = cls(**data)
		msg.id = id
		return msg


	def to_json(self, indent: int | str | None = None) -> str:
		"""
			Convert the message to a JSON representation

			:param indent: Character or number of spaces to use for indention
		"""

		data = JsonBase({
			"type": self.type,
			"id": self.id,
			"data": self.data,
			"message": self.message
		})

		return data.to_json(indent) + "\n"


Handler = Callable[[IpcMessage], Awaitable[IpcMessage | None]]


class IpcBase:
	def __init__(self, host: File | str = "localhost", port: int = 8080) -> None:
		self.host: File | str = host
		self.port: int = port
		self.handlers: dict[str, Handler] = {}
		self.responses: dict[str, IpcMessage] = {}

		self._post_init()


	def _post_init(self) -> None:
		pass


	async def __aenter__(self) -> Self:
		await self.start()
		return self


	async def __aexit__(self, *_: Any) -> None:
		await self.stop()


	def add_handler(self, name: str, func: Handler) -> None:
		"""
			Add a handler for messages of the specified type

			.. note:: ``disconnect`` is a reserved name

			:param name: Type name of messages the handler should handle
			:param func: The function to be ran for the specified message type
		"""

		if not inspect.iscoroutinefunction(func):
			raise TypeError("Handler must be an async method")

		self.handlers[name] = func


	def handler(self, name: str) -> Callable[[Handler], Handler]:
		"""
			Decorator for adding message handlers

			:param name: Type name of messages the handler should handle
		"""

		def wrapper(func: Handler) -> Handler:
			self.add_handler(name, func)
			return func

		return wrapper


	async def start(self) -> None:
		"Start the message reader loop"

		raise NotImplementedError


	async def stop(self) -> None:
		"Stop the message reader loop"

		raise NotImplementedError


	async def handle_message(self, request: IpcMessage) -> IpcMessage | None:
		try:
			handler = self.handlers[request.type]

		except KeyError:
			return IpcMessage.new_error(f"Invalid handler: {request.type}")

		try:
			return await handler(request)

		except Exception:
			traceback.print_exc()
			return IpcMessage.new_error("Handler error")


class IpcClient(IpcBase):
	def __init__(self, host: File | str = "localhost", port: int = 8080) -> None:
		"""
			Create a new IPC client. Passing a :class:`File` object to ``host`` will use UNIX
			sockets instead of a TCP connection.

			:param host: Hostname or path to unix socket to connect to
			:param port: Port number the server is listening on
		"""

		IpcBase.__init__(self, host, port)

		self._transport: AsyncTransport | None = None


	async def request(self,
					type: str,
					data: dict[str, Any] | None = None,
					message: str | None = None,
					no_return: bool = False) -> IpcMessage | None:
		"""
			Send a request to the server. Convenience method for creating and sending a message.

			:param type: Message type to send
			:param data: Data to send with the message
			:param message: User-readable text to send with the message
		"""

		msg = IpcMessage(type, data, message, no_return)
		return await self.send(msg)


	async def send(self, message: IpcMessage) -> IpcMessage | None:
		"""
			Send a ``Message`` object to the server and wait for a response

			:param message: Message object to send
		"""

		if self._transport is None:
			await self.start()

		message.id = random_str(20)
		await self._transport.write(message.to_json()) # type: ignore[union-attr]

		if message.no_return:
			return None

		if message.type == "disconnect":
			return IpcMessage("response", message = "okay")

		count = 0

		while message.id not in self.responses:
			await asyncio.sleep(0.1)
			count += 1

			if count >= 100:
				raise TimeoutError("Failed to get response")

		return self.responses.pop(message.id)


	async def start(self) -> None:
		if self._transport is not None:
			return

		if isinstance(self.host, File):
			self._transport = await AsyncTransport.new_client(self.host, unix = True, timeout = 0)

		else:
			self._transport = await AsyncTransport.new_client(self.host, self.port, timeout = 0)

		asyncio.create_task(self.handle_run())


	async def stop(self) -> None:
		if self._transport is None:
			return

		if not self._transport.eof:
			await self.send(IpcMessage("disconnect"))

		await self._transport.close()
		self._transport = None


	async def handle_run(self) -> None:
		if self._transport is None:
			return

		while not self._transport.eof:
			try:
				if not (data := await self._transport.readline()):
					break

				message = IpcMessage.parse(data)
				message.transport = self._transport

			except JSONDecodeError:
				msg = IpcMessage.new_error("Failed to parse JSON data")
				msg.id = random_str(20)

				await self._transport.write(msg.to_json())
				continue

			if message.type == "disconnect":
				break

			if message.type in {"response", "error"}:
				self.responses[message.id] = message
				continue

			if (response := await self.handle_message(message)) is None:
				response = IpcMessage("response", None, "okay")

			if message.no_return:
				continue

			response.id = random_str(20)
			await self._transport.write(response.to_json())

		await self.stop()


class IpcServer(IpcBase):
	def __init__(self, host: File | str = "localhost", port: int = 8080) -> None:
		"""
			Create a new IPC server. Passing a :class:`File` object to ``host`` will use UNIX
			sockets instead of a TCP connection.

			:param host: Hostname or path to unix socket to listen on
			:param port: Port number the server will listen on
		"""

		IpcBase.__init__(self, host, port)

		self._clients: list[AsyncTransport] = []
		self._server: asyncio.Server | None = None


	def run(self) -> None:
		"Run the message listener loop and wait for it to close"

		asyncio.run(self.handle_run())


	async def send(self, message: IpcMessage, *ignore: AsyncTransport) -> None:
		"""
			Send a ``Message`` object to the server and wait for a response

			:param message: Message object to send
		"""

		message.id = random_str(20)
		message.no_return = True

		for client in self._clients:
			if client in ignore:
				continue

			await client.write(message.to_json())


	async def start(self) -> None:
		if self._server is not None:
			return

		if isinstance(self.host, File):
			self._server = await asyncio.start_unix_server(self.handle_client, self.host)

		else:
			self._server = await asyncio.start_server(self.handle_client, self.host, self.port)


	async def stop(self) -> None:
		if self._server is None:
			return

		if not self._server.is_serving():
			self._server = None
			return

		self._server.close()
		await self._server.wait_closed()


	async def handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
		transport = AsyncTransport(reader, writer, timeout = 0)
		self._clients.append(transport)

		while not transport.eof:
			try:
				request = IpcMessage.parse(await transport.readline())
				request.transport = transport

			except JSONDecodeError:
				msg = IpcMessage.new_error("Failed to parse JSON data")
				msg.id = random_str(20)
				await transport.write(msg.to_json())
				continue

			except (ConnectionResetError, BrokenPipeError):
				break

			if request.type == "disconnect":
				break

			if request.type in {"response", "error"}:
				self.responses[request.id] = request
				continue

			if (response := await self.handle_message(request)) is None:
				response = IpcMessage("response", None, "okay")

			if request.no_return:
				continue

			response.id = request.id

			try:
				await transport.write(response.to_json())

			except (ConnectionResetError, BrokenPipeError):
				break

		await transport.close()
		self._clients.remove(transport)


	async def handle_run(self) -> None:
		await self.start()
		await self._server.serve_forever() # type: ignore[union-attr]
