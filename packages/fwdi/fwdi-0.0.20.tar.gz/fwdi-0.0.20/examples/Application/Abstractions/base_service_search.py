from abc import abstractmethod, ABCMeta
from fwdi.Application.Abstractions.base_service import BaseServiceFWDI
from Application.Abstractions.base_manager_db import BaseManagerContextDB
from Application.DTO.ContextReqestToLLMModel.context_request_to_llm import DataForLlmModel
from Application.DTO.Request.rag_question_project import RequestToLLM
from Application.Embeding.embeding_model import Embedding_Model
from Utilites.tools import TextTools_v1


class BaseServiceSearch(BaseServiceFWDI, metaclass=ABCMeta):
        
    @abstractmethod
    def relevant_search(self, 
                        question_pack: RequestToLLM,
                        manager_db: BaseManagerContextDB,                         
                        tools: TextTools_v1, 
                        embeding: Embedding_Model
                        ) -> DataForLlmModel:
        pass

