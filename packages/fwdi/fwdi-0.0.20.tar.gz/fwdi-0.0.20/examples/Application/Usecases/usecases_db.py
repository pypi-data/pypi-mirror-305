import pandas as pd
from Utills.ext_path import ExtPath
from lsi_lda_vector import create_lsi_lda_matrix_store
from request_llm_about_question import create_vector_db
from webparse import parse_web
from shutil import move
from create_logger import get_logger

logger = get_logger(__name__)



class Usecases():

    def upload_and_safe_web():
        pass
        #data = parse_web()
        #data_old = pd.read_pickle(Embedding_Service.path_pickle).to_dict('records')
        #if len(data) != len(data_old):
        #    Usecases.update_db(data)
        #else:
        #    for i in range(len(data)):
        #        if data[i]['hash'] != data_old[i]['hash']:
        #            Usecases.update_db(data)
        #            break

    def update_db(data):
        pass
        
        #Embedding_Service.create_pickle(lst_parse=data)
        #create_vector_db()
        #create_lsi_lda_matrix_store(flag_update=True)
        #Embedding_Service.works = True
        #move('Databases/vectorstore/temp/index.faiss', 'Databases/vectorstore/index.faiss')
        #Embedding_Service.works = False

    def init_app():
        pass
        #Embedding_Service.works = True
        #flag = False
        #if not ExtPath.exists_file(Embedding_Service.path_pickle):
        #    flag = True
        #    data = parse_web()
        #    Embedding_Service.create_pickle(lst_parse=data)

        #if not ExtPath.exists_file('Databases/vectorstore/index.faiss'):
        #    flag = True
        #    create_vector_db()
        #    move('Databases/vectorstore/temp/index.faiss', 'Databases/vectorstore/index.faiss')
        #if not ExtPath.exists_file(Embedding_Service.path_lsi_lda):
        #    flag = True
        #    create_lsi_lda_matrix_store(flag_update=False, path='Databases/lsi_lda_store_bsp')

        #Embedding_Service.works = False
        #return flag
