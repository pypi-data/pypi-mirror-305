from abc import ABCMeta, abstractmethod
from sentence_transformers import SentenceTransformer
from Utilites.ext_sys import ExtSys
from fwdi.Application.Abstractions.base_service import BaseServiceFWDI


class BaseEmbedding_Model(BaseServiceFWDI, metaclass=ABCMeta):
    ...

class Embedding_Model():
    if ExtSys.is_debug():
        encoder:SentenceTransformer = SentenceTransformer("intfloat/multilingual-e5-large", device='cpu')
        print('Запускается на cpu.')
        #logger.info('Запускается на cpu.')
    else:
        encoder:SentenceTransformer = SentenceTransformer("intfloat/multilingual-e5-large", device='cuda')
        #logger.info('Запускается на cuda.')
        print('Запускается на cuda.')
