from fwdi.Application.Abstractions.base_service_collection import BaseServiceCollectionFWDI
from fwdi.Infrastructure.Configs.rest_client_config import RestClientConfig

class DependencyInjection():
    def AddRestConfig(services:BaseServiceCollectionFWDI):
        restConfig = RestClientConfig()
        restConfig.server = 'cd-host-va.codev.dom'
        #restConfig.server = 'localhost'
        restConfig.port = 5100
        #restConfig.port = 5000
        restConfig.security_layer = False
        restConfig.username = 'admin'
        restConfig.password = 'admin'
        
        services.AddSingleton(restConfig)
    