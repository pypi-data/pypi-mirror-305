from abc import ABCMeta, abstractmethod
from fwdi.Application.Abstractions.base_service import BaseServiceFWDI

from Application.Abstractions.base_web_parse import BaseWebParse


class BaseProxyWebParse(BaseServiceFWDI, metaclass=ABCMeta):
    
    @abstractmethod
    def get_parse_stand() -> BaseWebParse:
        pass

    @abstractmethod
    def get_parse_bsp() ->BaseWebParse:
        pass