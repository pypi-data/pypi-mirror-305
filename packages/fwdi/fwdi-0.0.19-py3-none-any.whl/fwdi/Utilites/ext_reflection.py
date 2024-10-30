#        _       __        __    __________    _____     __   __     __
#   	/ \	    |  |	  |__|  |__________|  |  _  \   |__|  \ \   / /
#      / _ \	|  |	   __       |  |      | |_)  |   __    \ \_/ /   Alitrix - Modern NLP
#     / /_\ \	|  |	  |  |      |  |      |  _  /   |  |    } _ {    Languages: Python, C#
#    / _____ \	|  |____  |  |      |  |      | | \ \   |  |   / / \ \   http://github.com/Alitrix
#   /_/     \_\	|_______| |__|	    |__|      |_|  \_\  |__|  /_/   \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Alitrix Authors <http://github.com/Alitrix>

from functools import wraps
import inspect
import itertools
from types import FunctionType
from typing import Any, TypeVar, Callable
from abc import ABCMeta, ABC

from .utilities import Utilities
from ..Application.DependencyInjection.resolve_provider import *
from ..Application.Abstractions.base_service import BaseServiceFWDI

T = TypeVar('T')
_C = TypeVar("_C", bound=Callable[..., Any])

class ExtReflection():
    def get_methods_class(cls):
        return set((x, y) for x, y in cls.__dict__.items()
                    if isinstance(y, (FunctionType, classmethod, staticmethod))
                    and not(x.startswith("__") and x.endswith("__")))

    def get_list_parent_methods(cls):
        return set(itertools.chain.from_iterable(
            ExtReflection.get_methods_class(c).union(ExtReflection.get_list_parent_methods(c)) for c in cls.__bases__))

    def list_class_methods(cls, is_narrow:bool):
        methods = ExtReflection.get_methods_class(cls)
        if  is_narrow:
            parentMethods = ExtReflection.get_list_parent_methods(cls)
            return set(cls for cls in methods if not (cls in parentMethods))
        else:
            return methods
    
    def get_handler_method(object:object, name_method:str, *args)->Callable:
        call_method = getattr(object, name_method)
        return call_method
    
    def get_class_info(cls:T)->list:
        if type(cls) is type.__class__:
            class_params = inspect.signature(cls.__init__)
            class_args:list[dict] = []
            for param_name in class_params.parameters:
                param_d = class_params.parameters[param_name]
                type_param = param_d.annotation if not param_d.annotation is inspect._empty else param_d.default if not param_d.default is inspect._empty else cls
                class_args.append({'name':param_name, 'type':type_param})
        
        return class_args

    def get_function_info_v1(fn:Callable[..., Any])->dict:
            if not callable(fn):
                raise Exception(f'{fn.__name__} - Is not callable object.')
            
            fn_datas:dict = {}
            fn_args:list[dict] = []
            
            fn_datas['class'] = inspect._findclass(fn)
            fn_datas['name'] = fn.__name__
            fn_datas['coroutine'] = inspect.iscoroutine(fn)

            fn_params = inspect.signature(fn)
            for index, param_name in enumerate(fn_params.parameters):
                param_d = fn_params.parameters[param_name]
                type_param = param_d.annotation if not param_d.annotation is inspect._empty else param_d.default
                fn_args.append({'arg_pos': index, 'name': param_name, 'type': type_param})

            fn_datas['params'] = fn_args

            return fn_datas
    
    def init_inject(func: _C)-> _C:
        @wraps(func)
        def wrapper(*args, **kwargs)->Any:
            if 'is_inject' not in kwargs:
                fn_datas = ExtReflection.get_function_info_v1(func)
                new_args = list(args)

                for item in fn_datas['params']:
                    if item['name'] != 'self':
                        check_type = item['type']
                        if issubclass(check_type, BaseServiceFWDI):
                            search_service = ResolveProviderFWDI.get_service(item['type'])
                            if search_service != None:
                                new_args.append(search_service)

                result = func(*new_args, **kwargs)
                return result
            else:
                new_args = {}
                for item in [item for item in kwargs if item != 'is_inject']:
                    element = {item:kwargs[item]}
                    new_args.update(element)

                result = func(*args, **new_args)
                return result

        return wrapper
    
    def method_inject_v2(func: _C) -> _C:
        @wraps(func)
        def internal(*args, **kwargs):
            info_method_args = ExtReflection.get_function_info_v1(func)
            if len(args) != len(info_method_args['params']):
                find_args = [item for item in info_method_args['params'] if item['name'] != 'self']
                
                new_kwargs_params:dict[str, any] = {}
                if Utilities.search_key(info_method_args['params'], 'self'):
                    new_kwargs_params['self'] = args[0]
                
                count_args = len(args)
                for item in find_args:
                    arg_pos, arg_name, arg_type = item['arg_pos'], item['name'], item['type']

                    if count_args > 1:
                        if arg_pos < count_args:
                            arg_item = args[arg_pos]
                            if type(arg_item) == arg_type:
                                new_kwargs_params[arg_name] = args[arg_pos]
                            else:
                                if len(kwargs) > 0:
                                    try_get_value = kwargs.get(arg_name)
                                    if try_get_value != None:
                                        new_kwargs_params[arg_name] = try_get_value
                                else:
                                    new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                        else:
                            arg_pos = arg_pos - 1
                            if arg_pos < count_args:
                                arg_item = args[arg_pos]
                                new_kwargs_params[arg_name] = args[arg_pos] if type(arg_item) == arg_type else ResolveProviderFWDI.get_service(arg_type)
                            else:
                                if len(kwargs) > 0:
                                    try_get_value = kwargs.get(arg_name)
                                    new_kwargs_params[arg_name] = try_get_value if try_get_value != None else ResolveProviderFWDI.get_service(arg_type)
                                else:
                                    new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                    else:
                        if len(kwargs) > 0:
                            try_get_value = kwargs.get(arg_name)
                            new_kwargs_params[arg_name] = try_get_value if try_get_value != None else ResolveProviderFWDI.get_service(arg_type)

                _exec = func(**new_kwargs_params)
            else:
                _exec = func(*args, **kwargs)

            return _exec
        
        return internal

    def method_inject_v3(func: _C) -> _C:
        @wraps(func)
        def internal(*args, **kwargs):
            info_method_args = ExtReflection.get_function_info_v1(func)
            if len(args) != len(info_method_args['params']):
                find_args = [item for item in info_method_args['params'] if item['name'] != 'self']
                
                new_kwargs_params:dict[str, any] = {}
                if Utilities.search_key(info_method_args['params'], 'self'):
                    new_kwargs_params['self'] = args[0]
                else:
                    if len(kwargs) == 0:
                       new_kwargs_params[find_args[0]['name']] = args[0]
                       find_args = [item for item in info_method_args['params'] if item['name'] != 'self'][1:]

                    if len(args) > 0:
                        new_kwargs_params[find_args[0]['name']] = args[0]
                        find_args = [item for item in info_method_args['params'] if item['name'] != 'self'][1:]

                
                count_args = len(args)
                for item in find_args:
                    arg_pos, arg_name, arg_type = item['arg_pos'], item['name'], item['type']

                    if count_args > 1:
                        if arg_pos < count_args:
                            arg_item = args[arg_pos]
                            if type(arg_item) == arg_type:
                                new_kwargs_params[arg_name] = args[arg_pos]
                            else:
                                if len(kwargs) > 0:
                                    try_get_value = kwargs.get(arg_name)
                                    if try_get_value != None:
                                        new_kwargs_params[arg_name] = try_get_value
                                else:
                                    if issubclass(arg_type, BaseServiceFWDI):
                                        new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                                    else:
                                        print()
                        else:
                            arg_pos = arg_pos - 1
                            if arg_pos < count_args:
                                arg_item = args[arg_pos]
                                if type(arg_item) == arg_type:
                                    new_kwargs_params[arg_name] = args[arg_pos] 
                                else:
                                    if issubclass(arg_type, BaseServiceFWDI):
                                        new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                                    else:
                                        print()
                            else:
                                if len(kwargs) > 0:
                                    try_get_value = kwargs.get(arg_name)
                                    new_kwargs_params[arg_name] = try_get_value if try_get_value != None else ResolveProviderFWDI.get_service(arg_type)
                                else:
                                    if issubclass(arg_type, BaseServiceFWDI):
                                        new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                                    else:
                                        print()
                    else:
                        if len(kwargs) > 0:
                            try_get_value = kwargs.get(arg_name)
                            if try_get_value != None:
                                new_kwargs_params[arg_name] = try_get_value
                            else:
                                if issubclass(arg_type, BaseServiceFWDI):
                                    new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                                else:
                                    print()

                _exec = func(**new_kwargs_params)
            else:
                _exec = func(*args, **kwargs)

            return _exec
        
        return internal
    
    def method_inject_v4(func: _C) -> _C:
        @wraps(func)
        def internal(*args, **kwargs):
            info_method_args = ExtReflection.get_function_info_v1(func)
            if len(args) != len(info_method_args['params']):
                find_args = [item for item in info_method_args['params'] if item['name'] != 'self']
                
                new_kwargs_params:dict[str, any] = {}
                if Utilities.search_key(info_method_args['params'], 'self'):
                    new_kwargs_params['self'] = args[0]
                else:
                    if len(kwargs) == 0:
                       new_kwargs_params[find_args[0]['name']] = args[0]
                       find_args = [item for item in info_method_args['params'] if item['name'] != 'self'][1:]

                    if len(args) > 0:
                        new_kwargs_params[find_args[0]['name']] = args[0]
                        find_args = [item for item in info_method_args['params'] if item['name'] != 'self'][1:]
                
                count_args = len(args)
                for item in find_args:
                    arg_pos, arg_name, arg_type = item['arg_pos'], item['name'], item['type']

                    if count_args > 1:
                        if arg_pos < count_args:
                            arg_item = args[arg_pos]
                            if type(arg_item) == arg_type:
                                new_kwargs_params[arg_name] = args[arg_pos]
                            else:
                                if len(kwargs) > 0:
                                    try_get_value = kwargs.get(arg_name)
                                    if try_get_value != None:
                                        new_kwargs_params[arg_name] = try_get_value
                                else:
                                    if issubclass(arg_type, BaseServiceFWDI):
                                        new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                                    else:
                                        print()
                        else:
                            if issubclass(arg_type, BaseServiceFWDI):
                                new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                            else:
                                if len(kwargs) > 0:
                                    try_get_value = kwargs.get(arg_name)
                                    new_kwargs_params[arg_name] = try_get_value if try_get_value != None else ResolveProviderFWDI.get_service(arg_type)
                                else:
                                    if issubclass(arg_type, BaseServiceFWDI):
                                        new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                    else:
                        if len(kwargs) > 0:
                            try_get_value = kwargs.get(arg_name)
                            if try_get_value != None:
                                new_kwargs_params[arg_name] = try_get_value
                            else:
                                if issubclass(arg_type, BaseServiceFWDI):
                                    new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                                else:
                                    print()

                _exec = func(**new_kwargs_params)
            else:
                _exec = func(*args, **kwargs)

            return _exec
        
        return internal

    def get_new_arguments(info_method_args:dict)->dict:
        args = info_method_args['args']
        kwargs = info_method_args['kwargs']

        if len(args) != len(info_method_args['params']):
            find_args = [item for item in info_method_args['params'] if item['name'] != 'self']
            
            new_kwargs_params:dict[str, any] = {}
            if Utilities.search_key(info_method_args['params'], 'self'):
                new_kwargs_params['self'] = args[0]
            else:
                if  len([item for item in info_method_args['params'] if item['name'] == 'self']) == 0:
                    if len(args) > 0:
                        new_kwargs_params[find_args[0]['name']] = args[1]
                else:
                    if len(kwargs) == 0:
                        find_args = [item for item in info_method_args['params'] if item['name'] != 'self'][1:]

                    if len(args) > 0:
                        new_kwargs_params[find_args[0]['name']] = args[0]
                        find_args = [item for item in info_method_args['params'] if item['name'] != 'self'][1:]
            
            count_args = len(args)
            for item in find_args:
                arg_pos, arg_name, arg_type = item['arg_pos'], item['name'], item['type']

                if count_args > 1:
                    if arg_pos < count_args:
                        arg_item = args[arg_pos]
                        if type(arg_item) == arg_type:
                            new_kwargs_params[arg_name] = args[arg_pos]
                        else:
                            if len(kwargs) > 0:
                                try_get_value = kwargs.get(arg_name)
                                if try_get_value != None:
                                    new_kwargs_params[arg_name] = try_get_value
                            else:
                                if issubclass(arg_type, BaseServiceFWDI):
                                    new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                    else:
                        if issubclass(arg_type, BaseServiceFWDI):
                            new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                        else:
                            if len(kwargs) > 0:
                                try_get_value = kwargs.get(arg_name)
                                new_kwargs_params[arg_name] = try_get_value if try_get_value != None else ResolveProviderFWDI.get_service(arg_type)
                            else:
                                if issubclass(arg_type, BaseServiceFWDI):
                                    new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                                elif ResolveProviderFWDI.contains(arg_type):
                                    new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)

                else:
                    if len(kwargs) > 0:
                        try_get_value = kwargs.get(arg_name)
                        if try_get_value != None:
                            new_kwargs_params[arg_name] = try_get_value
                        else:
                            if issubclass(arg_type, BaseServiceFWDI):
                                new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                    else:
                        if issubclass(arg_type, BaseServiceFWDI):
                            new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)

        return new_kwargs_params

    def method_inject(func: _C) -> _C:
        @wraps(func)
        def internal_sync(*args, **kwargs)->_C:
            if 'is_inject' not in kwargs:
                info_method_args = ExtReflection.get_function_info_v1(func)
                if len(args) != len(info_method_args['params']):
                    info_method_args['args'] = args
                    info_method_args['kwargs'] = kwargs
                    new_kwargs_params = ExtReflection.get_new_arguments(info_method_args)

                    result = func(**new_kwargs_params)
                else:
                    result = func(*args, **kwargs)

                return result
            else:
                new_args = {}
                for item in [item for item in kwargs if item != 'is_inject']:
                    element = {item:kwargs[item]}
                    new_args.update(element)
                
                result = func(*args, **new_args)
                return result

        @wraps(func)
        async def internal_async(*args, **kwargs)->_C:
            if 'is_inject' not in kwargs:
                info_method_args = ExtReflection.get_function_info_v1(func)
                if len(args) != len(info_method_args['params']):
                    info_method_args['args'] = args
                    info_method_args['kwargs'] = kwargs
                    new_kwargs_params = ExtReflection.get_new_arguments(info_method_args)      

                    result = await func(**new_kwargs_params)
                else:
                    result = await func(*args, **kwargs)

                return result
            else:
                new_args = {}
                for item in [item for item in kwargs if item != 'is_inject']:
                    element = {item:kwargs[item]}
                    new_args.update(element)
                
                result = await func(*args, **new_args)
                return result
        
        return internal_async if inspect.iscoroutinefunction(func) else internal_sync
    
    def is_class(obj)->bool:
        return True if isinstance(obj, type) else False
    
    def is_injectable_init(obj)->bool:
        return True if '__init__' in obj.__dict__ else False