#        _       __        __    __________    _____     __   __     __
#   	/ \	    |  |	  |__|  |__________|  |  _  \   |__|  \ \   / /
#      / _ \	|  |	   __       |  |      | |_)  |   __    \ \_/ /   Alitrix - Modern NLP
#     / /_\ \	|  |	  |  |      |  |      |  _  /   |  |    } _ {    Languages: Python, C#
#    / _____ \	|  |____  |  |      |  |      | | \ \   |  |   / / \ \   http://github.com/Alitrix
#   /_/     \_\	|_______| |__|	    |__|      |_|  \_\  |__|  /_/   \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Alitrix Authors <http://github.com/Alitrix>

import uvicorn
from typing import Callable, Any
from fastapi import FastAPI, Depends, Request, Path, Header, Cookie, Body

from ..Application.DependencyInjection.resolve_provider import ResolveProviderFWDI
from ..Application.Abstractions.base_controller import BaseControllerFWDI
from .web_application_builder import WebApplicationBuilder

from ..Application.dependency_injection import DependencyInjection as ApplicationDependencyInjection
from ..Persistence.dependency_injection import DependencyInjection as PersistenceDependencyInjection
from ..Infrastructure.dependency_injection import DependencyInjection as InfrastructureDependencyInjection

class WebApplication():
    def __init__(self, **kwargs):
        self.__debug:bool = kwargs['debug'] if 'debug' in kwargs else ''
        self.__app:FastAPI = FastAPI()
        
        self.resolver:ResolveProviderFWDI = None
        self.Name:str = kwargs['name'] if 'name' in kwargs else ''
        #self.init_default_endpoint()

    @property
    def Debug(self)->bool:
        return self.__debug

    @property
    def app(self)->FastAPI:
        return self.__app

    def map_controller(self, controller:BaseControllerFWDI)->None:
        if hasattr(controller, "routes"):
            self.__app.include_router(controller)
        else:
            raise Exception(f"{controller} has no have attribute routes !")
    
    def map_get(self, path:str, endpoint: Callable[..., Any]):
        response = self.__app.add_api_route(path=path, endpoint=endpoint, methods=["GET"])        
        return response
    
    def map_post(self, path:str, endpoint: Callable[..., Any]):
        response = self.__app.add_api_route(path=path, endpoint=endpoint, methods=["POST"])
        return response

    def map_delete(self, path:str, endpoint: Callable[..., Any]):
        response = self.__app.add_api_route(path=path, endpoint=endpoint, methods=["DELETE"])
        return response

    def map_put(self, path:str, endpoint: Callable[..., Any]):
        response = self.__app.add_api_route(path=path, endpoint=endpoint, methods=["PUT"])
        return response

    @classmethod
    def create_builder(cls, **kwargs)-> WebApplicationBuilder:
        webapp_instance = cls(**kwargs)
        webbuild_instance = WebApplicationBuilder(webapp_instance)
        
        #----------------------DEFAULT SERVICES DEPENDENCY------------------------------------
        
        PersistenceDependencyInjection.AddPersistence(webbuild_instance.services)
        ApplicationDependencyInjection.AddApplication(webbuild_instance.services)
        InfrastructureDependencyInjection.AddInfrastructure(webbuild_instance.services)

        #----------------------/DEFAULT SERVICES DEPENDENCY-----------------------------------

        return webbuild_instance
    
    def run(self, **kwargs):
        uvicorn.run(self.__app, **kwargs)