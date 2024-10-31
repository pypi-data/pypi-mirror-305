from abc import abstractmethod, ABCMeta
from fwdi.Application.Abstractions.base_service import BaseServiceFWDI
from Application.Abstractions.base_web_parse_tools import BaseWebParseTools


class BaseWebParse(BaseServiceFWDI, metaclass=ABCMeta):

    @abstractmethod
    def parse(web_parse_tools: BaseWebParseTools) -> list[dict]:
        pass