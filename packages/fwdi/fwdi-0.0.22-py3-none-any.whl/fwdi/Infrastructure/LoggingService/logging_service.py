#        _       __        __    __________    _____     __   __     __
#   	/ \	    |  |	  |__|  |__________|  |  _  \   |__|  \ \   / /
#      / _ \	|  |	   __       |  |      | |_)  |   __    \ \_/ /   Alitrix - Modern NLP
#     / /_\ \	|  |	  |  |      |  |      |  _  /   |  |    } _ {    Languages: Python, C#
#    / _____ \	|  |____  |  |      |  |      | | \ \   |  |   / / \ \   http://github.com/Alitrix
#   /_/     \_\	|_______| |__|	    |__|      |_|  \_\  |__|  /_/   \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Alitrix Authors <http://github.com/Alitrix>

from datetime import datetime


from ...Application.Abstractions.base_logging_service import BaseLoggingServiceFWDI
from ...Application.Abstractions.base_storage_service import BaseStorageServiceFWDI

class LoggingServiceFWDI(BaseLoggingServiceFWDI):
    def __init__(self) -> None:
        super().__init__()
        self._storage:BaseStorageServiceFWDI = None
    
    @classmethod
    def create(cls, storage:BaseStorageServiceFWDI):
        inst = cls()
        inst._storage = storage
    
    def info(self, msg:str)->None:
        self._storage.append(f"{datetime.now()}::INFO::{msg}")

    def alert(self, msg:str)->None:
        self._storage.append(f"{datetime.now()}::ALERT::{msg}")
    
    def warning(self, msg:str)->None:
        self._storage.append(f"{datetime.now()}::WARN::{msg}")

    def error(self, msg:str)->None:
        self._storage.append(f"{datetime.now()}::ERROR::{msg}")