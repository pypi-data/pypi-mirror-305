import sys
from pathlib import Path
sys.path.insert(0,str(Path(sys.path[0]).parent))

from Application.Abstractions.base_random_uuid import BaseRandomGUID
from Application.Abstractions.base_message import BaseMessage
from Application.Abstractions.base_composit import BaseComposit

from Application.Usecases.generate_uuid_print import GenerateUuidAndPrint
from Application.Usecases.normal_message import UserNormalMessage
from Application.Usecases.user_random_id import UserRndGUID

#======= Package library ============================
from fwdi.Infrastructure.Configs.rest_client_config import RestClientConfig
from fwdi.Application.Abstractions.base_service_collection import BaseServiceCollectionFWDI
from fwdi.WebApp.web_application import WebApplication
from fwdi.WebApp.web_application_builder import WebApplicationBuilder
#----------------------------------------------------



class ApplicationDI():
    def add(services:BaseServiceCollectionFWDI):
        services.AddTransient(BaseRandomGUID, UserRndGUID) 
        services.AddTransient(BaseMessage, UserNormalMessage)
        services.AddTransient(BaseComposit, GenerateUuidAndPrint)

def start_web_service():
    server_param = {
        'name':'Python MVC Service',
        'debug':'False'
    }
 
    #====Block created Web Application layer

    builder:WebApplicationBuilder = WebApplication.create_builder(**server_param)
    
    #====/Block=====================================================================
    #==========Init Scopes =========================================================

    scopes = {
        "guest": "User without cofirm account.", 
        "user": "User access.",
        }
    
    builder.add_scope(scopes)
    builder.add_authentification()

    #==========/Init Scopes ========================================================
    #====Block registration all section application services to Dependecy Container
    restConfig = RestClientConfig()
    restConfig.server = '127.0.0.1'
    restConfig.port = 5000
    restConfig.security_layer = False
    restConfig.username = 'admin'
    restConfig.password = 'admin'
    builder.services.AddImplementSingleton(restConfig)

    ApplicationDI.add(builder.services)

    #====/Block=====================================================================
    
    app:WebApplication = builder.build()

    #WebService.AddEndpoints(app) <<< ---- maybe in new version
    from Persistance.dependency_injection import WebService
    WebService.AddControllers(app)
    
    kwargs = {
            'host': "0.0.0.0",
            'port': 5000
        }
    
    app.run(**kwargs)

if __name__ == "__main__":
    start_web_service()