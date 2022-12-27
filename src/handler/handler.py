from abc import ABC

from src.handler.rabbitmq_handler import RabbitmqHandler
from src.reposiitory.redis_repository import RedisRepository
from src.models.handler_strategy import HandlerStrategy


class Handler(HandlerStrategy, ABC):
    def __init__(self):
        self.rabbit_handler = RabbitmqHandler()
        self.redis = RedisRepository()

    def execute(self):
        self.rabbit_handler.basic_consume()
        command = self.rabbit_handler.get_message()
        print(command)