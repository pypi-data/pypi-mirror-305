from fwdi.WebApp.web_application import WebApplication
from Presentation.Endpoints.questions_endpoints import QuestionEndpoint


class DependencyInjection():
    from fwdi.WebApp.web_application_builder import WebApplicationBuilder

    def AddEndpoints(app:WebApplication):
        app.map_get(f'/api/v1.0/question', QuestionEndpoint.search)
        #app.map_get(f'/api/v1.0/rag_query', QuestionEndpoint.rag_query)

    def AddScope(builder:WebApplicationBuilder):
        scopes = {
            "admin": "Administration access.", 
            "question": "Question LLM access"
            }
        builder.add_scope(scopes)