from fwdi.Application.Abstractions.base_service_collection import BaseServiceCollectionFWDI
from Utilites.tools import TextTools_v1, PostProccessingText

class DependencyInjection():
    def AddUtils(services:BaseServiceCollectionFWDI):
        services.AddTransient(TextTools_v1)
        services.AddTransient(PostProccessingText)
