from abc import ABCMeta, abstractmethod

from fwdi.Application.Abstractions.base_service import BaseServiceFWDI
from examples.Domain.Enums.enum_type_message import EnumTypeMessage

class BaseMessage(BaseServiceFWDI, metaclass=ABCMeta):

    @abstractmethod
    def set_msg(msg_type:EnumTypeMessage, msg:str):
        pass

    @abstractmethod
    def show_message(self, msg_type:EnumTypeMessage, message:str):
        pass
