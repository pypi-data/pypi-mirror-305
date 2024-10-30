from fastapi import Depends, Security
from fwdi.Application.DTO.Auth.model_user import User
from fwdi.Infrastructure.JwtService.jwt_service import JwtServiceFWDI
#from fwdi.Infrastructure.LoggingService.logging_service import LoggingServiceFWDI

from Application.DTO.ContextReqestToLLMModel.context_request_to_llm import DataForLlmModel
from Application.DTO.Request.rag_question_project import RequestToLLM
from Application.Usecases.usecase_search import ServiceSearch
from Application.Usecases.usecase_task_manager import UsecaseTaskManager
from Utilites.ext_rest import RestResponse


class QuestionEndpoint():
    def search(question_pack:RequestToLLM,
                  search_answer: ServiceSearch=Depends(), 
                  task_manager: UsecaseTaskManager=Depends(),
                  current_user: User = Security(JwtServiceFWDI.get_current_active_user, scopes=["question"]),):
        
        #++++++++++++++++++USECASE FROM APPLICATION++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if not question_pack.refined_question:
            context_LLM = DataForLlmModel(question_pack, '', None)
            place_queue = task_manager.add_task(context_LLM)
            if place_queue is None:
                #logger.info('Repeated request from one user.')
                response = 'Вы выполнили запрос к системе, ожидайте, пожалуйста, ответа.'
            elif place_queue == 0:
                response = 'Предварительная обработка текста вашего вопроса.'
            else:
                response = f'Предварительная обработка текста вашего вопроса. Ваш запрос принят, вы {place_queue} в очереди.'
        else:
            context_for_llm = search_answer.relevant_search(question_pack)
            if type(context_for_llm) != str:
                response = task_manager.add_task(context_for_llm)
            else:
                response = context_for_llm

        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        if response == None:
            return RestResponse.make_response("Error auth")
        else:
            return RestResponse.response_200(response)

        
"""    def answer():
        pass
    """
