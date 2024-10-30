from neonize.client import NewClient
from neonize.proto.Neonize_pb2 import Message
from .utils import log
from typing import Generator, Type, Optional
from .core.graph import Graph
from abc import ABC, abstractmethod


class Middleware(ABC):
    stop: bool = True
    name: Optional[str] = None

    def __init__(self):
        if not self.name:
            self.name = self.__class__.__name__

    @abstractmethod
    def run(
        self, client: NewClient, message: Message
    ) -> (
        None | bool
    ):  # None -> continue, False -> global command will run after Middleware, True -> global command never execute
        ...


class MiddlewareRegister(list[Middleware], Graph):
    def add(self, middleware: Middleware | Type[Middleware]):
        """
        This method adds a middleware to the middleware register.

        :param middleware: The middleware instance or class to be added.
                           If a class is provided, it will be instantiated before being added.
        :type middleware: Middleware instance or Middleware class (Type[Middleware])
        """
        if isinstance(middleware, type):
            self.append(middleware())
        else:
            self.append(middleware)
        log.debug(f"{middleware.name} middleware loaded")

    def get_all_names(self) -> Generator[str, None, None]:
        """
        This method is a generator that yields the name of each middleware in the current instance.

        :yield: The name of each middleware in the current instance, as a string.
        :rtype: Generator[str, None, None]
        """
        for middleware in self:
            yield middleware.name.__str__()

    def execute(self, client: NewClient, message: Message) -> None | Middleware:
        """
        This method executes each middleware in the current instance with the provided client and message.
        If a middleware's run method returns True and its stop attribute is set to True, the method will return that middleware and no further middlewares or global commands will be executed.
        If the run method returns False, the global command will run after the Middleware.
        If the run method returns None, it will continue to the next middleware.

        :param client: The client that the middleware will be executed with.
        :type client: NewClient
        :param message: The message that the middleware will process.
        :type message: Message
        :return: The middleware that stopped the execution, if any. If no middleware stopped the execution, returns None.
        :rtype: None | Middleware
        """
        for middleware in self:
            status = middleware.run(client, message)
            if status and middleware.stop:
                return middleware


middleware = MiddlewareRegister()
