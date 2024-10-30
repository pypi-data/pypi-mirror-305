import sys
from pathlib import Path
sys.path.insert(0,str(Path(sys.path[0]).parent))

#======= Package library ============================
from fwdi.WebApp.web_application import WebApplication
from fwdi.WebApp.web_application_builder import WebApplicationBuilder
#----------------------------------------------------
from Infrastructure.dependency_injection import DependencyInjection as InfrastructureDependencyInjection
from Persistance.dependency_injection import DependencyInjection as PersistanceDependencyInjection
from Presentation.dependency_injection import DependencyInjection as PresentationDependencyInjection
from Application.dependency_injection import DependencyInjection as ApplicationDependencyInjection
from Utilites.dependency_injection import DependencyInjection as UtilitesDependencyInjection
#----------------------------------------------------
def start_web_service():
    server_param = {
        'name':'Rest Inference service',
        'debug':'False'
    }
    builder:WebApplicationBuilder = WebApplication.create_builder(**server_param)
    #------------------------------------------------------------------------------------------
    #builder.add_authentification() #<--------------NEED create full code for functionality
    #------------------------------------------------------------------------------------------
    UtilitesDependencyInjection.AddUtils(builder.services)

    InfrastructureDependencyInjection.AddRestConfig(builder.services)

    PersistanceDependencyInjection.AddPersistance(builder.services)
    ApplicationDependencyInjection.AddApplicationInteractors(builder.services)
    #------------------------------------------------------------------------------------------
    PresentationDependencyInjection.AddScope(builder)
    
    app:WebApplication = builder.build()
    #------------------------------------------------------------------------------------------
    PresentationDependencyInjection.AddEndpoints(app)
    #------------------------------------------------------------------------------------------
    kwargs = {
            'host': "0.0.0.0",
            'port': 5000
        }
    app.run(**kwargs)
if __name__ == "__main__":
    start_web_service()