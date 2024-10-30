from fwdi.Application.Abstractions.base_service_collection import BaseServiceCollectionFWDI


from Application.Abstractions.base_llm_service import BaseLlmService
from Application.Abstractions.base_service_search import BaseServiceSearch
from Application.Abstractions.base_task_manager import BaseTaskManager
from Application.Embeding.embeding_model import Embedding_Model
from Application.TaskManager.task_manager import TaskManager
from examples.Infrastructure.rag_llm_service import LLMService
from Application.Usecases.usecase_search import ServiceSearch

class DependencyInjection():
    def AddApplicationInteractors(services:BaseServiceCollectionFWDI):
        services.AddTransient(BaseServiceSearch, ServiceSearch)
        services.AddSingleton(Embedding_Model)
        services.AddTransient(BaseLlmService, LLMService)
        services.AddSingleton(BaseTaskManager, TaskManager)
