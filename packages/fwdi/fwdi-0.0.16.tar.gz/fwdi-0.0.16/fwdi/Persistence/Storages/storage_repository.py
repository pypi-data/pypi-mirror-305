#        _       __        __    __________    _____     __   __     __
#   	/ \	    |  |	  |__|  |__________|  |  _  \   |__|  \ \   / /
#      / _ \	|  |	   __       |  |      | |_)  |   __    \ \_/ /   Alitrix - Modern NLP
#     / /_\ \	|  |	  |  |      |  |      |  _  /   |  |    } _ {    Languages: Python, C#
#    / _____ \	|  |____  |  |      |  |      | | \ \   |  |   / / \ \   http://github.com/Alitrix
#   /_/     \_\	|_______| |__|	    |__|      |_|  \_\  |__|  /_/   \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Alitrix Authors <http://github.com/Alitrix>

from ...Application.Abstractions.base_storage_service import BaseStorageServiceFWDI

class StorageServiceFWDI(BaseStorageServiceFWDI):
    def __init__(self) -> None:
        super().__init__()
        self._storage:str = './temp.log'
    
    def write(self, message:str):
        with open(self._storage, 'w+', encoding="utf-8") as f:
            f.write(message)

    def append(self, message:str):
        with open(self._storage, 'a', encoding="utf-8") as f:
            f.write(f"{message}\n")