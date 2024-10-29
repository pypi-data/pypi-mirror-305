from fastapi import Depends, Security
from Application.Abstractions.base_composit import BaseComposit

from fwdi.Application.Abstractions.base_controller import BaseControllerFWDI
from fwdi.Application.Abstractions.meta_service import MetaServiceFWDI
from fwdi.Application.DTO.Auth.model_user import User
from fwdi.Infrastructure.JwtService.jwt_service import JwtServiceFWDI

from pydantic import BaseModel
class MyData(BaseModel):
    Text:str

class UserController(BaseControllerFWDI, metaclass=MetaServiceFWDI):
    def __init__(self, composite:BaseComposit, base_path:str='/'):
        super().__init__(base_path)
        self.__composite:BaseComposit = composite
    
    async def get(self, my_data:MyData, current_user: User = Security(JwtServiceFWDI.get_current_active_user, scopes=["user"]),):
        result_composit_test = self.__composite.run_once()
        return {
            "Controller": self.__class__.__name__,
            "Method 'GET'": "Hello from KSU Flat Web Dependency Injection platform",
            "Composite result":result_composit_test,
            "Current user": {
                "Login": current_user.username,
                "Email": current_user.email,
                },
            'MyData': my_data
            }
    
    async def post(self, my_data:MyData, current_user: User = Security(JwtServiceFWDI.get_current_active_user, scopes=["user"]),):
        result_composit_test = self.__composite.run_once()
        return {
            "Controller": self.__class__.__name__,
            "Method 'GET'": "Hello from KSU Flat Web Dependency Injection platform",
            "Composite result":result_composit_test,
            "Current user": {
                "Login": current_user.username,
                "Email": current_user.email,
                },
            'MyData': my_data
            }