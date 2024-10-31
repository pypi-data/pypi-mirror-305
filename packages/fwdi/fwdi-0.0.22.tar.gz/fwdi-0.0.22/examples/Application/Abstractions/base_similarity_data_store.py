from abc import abstractmethod, ABCMeta
from fwdi.Application.Abstractions.base_service import BaseServiceFWDI


class BaseSimilarityDataStore(BaseServiceFWDI, metaclass=ABCMeta):

    @abstractmethod
    def read(path: str) -> list[dict]:
        pass

    @abstractmethod
    def write(lst_doc: list[dict], path: str, columns: list) -> bool:
        pass