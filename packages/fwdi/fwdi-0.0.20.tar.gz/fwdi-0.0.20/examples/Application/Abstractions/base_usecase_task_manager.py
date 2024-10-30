from abc import ABCMeta, abstractmethod
from fwdi.Application.Abstractions.base_service import BaseServiceFWDI

class BaseUsecaseTaskManager(BaseServiceFWDI, metaclass=ABCMeta):

    @abstractmethod
    def add_task(self):
        pass