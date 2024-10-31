from Application.Abstractions.base_task_manager import BaseTaskManager
from Application.Abstractions.base_usecase_task_manager import BaseUsecaseTaskManager
from Application.DTO.ContextReqestToLLMModel.context_request_to_llm import DataForLlmModel
from fwdi.Infrastructure.LoggingService.logging_service import LoggingServiceFWDI

from fastapi import Depends, Security

class UsecaseTaskManager(BaseUsecaseTaskManager):
    def add_task(self, context_LLM: DataForLlmModel, task_manager: BaseTaskManager) -> str:
        place_queue = task_manager.add(context_LLM)
        if place_queue is None:
            #self.logger.info('Repeated request from one user.')
            return 'Вы выполнили запрос к системе, ожидайте, пожалуйста, ответа.'
        
        #self.logger.info('Add task for request to LLM.')
        
        if place_queue == 0:
            return 'Обрабатываю ваш запрос.'
        return f'Ваш запрос принят, вы {place_queue} в очереди.'