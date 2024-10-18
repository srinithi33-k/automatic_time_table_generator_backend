from ..service.DbInit import DbInit
from re import search
from psycopg2.extensions import connection
from time_table_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from datetime import datetime
# from jwt import decode

""" 
    #@Python Programs
    #@Name : common_utils.py
    #@Since : 14-01-2024
    #@Author : Srinithi K
    #@Version : 1.0
    #@See : This file contains the commenly needed functions"""

def cursor_creater():
    try:
        # postgres db connection
        connect_obj=db_creater()
        creater_obj = connect_obj.db_connector()
        if not isinstance(creater_obj,connection):
            raise Exception("Db connection failed")
        return creater_obj,creater_obj.cursor()
    except Exception as error:
        ERROR_JSON["error_reason"] = str(error)
        print(ERROR_JSON)

def db_creater():
    try:
        connection_obj=DbInit(data_base="time_table_db",database_username="postgres",password="postgres")
        return connection_obj
    except Exception as error:
        raise Exception(error)    
    
def is_email(element):
    regex = r'^[a-z0-9._-]+@[a-z0-9]+\.[a-z.-_]{2,}$'
    if search(regex,element):
        return True
    else:
        return False
    
def is_password(word):
    regex = r'^(?=.*[A-Z])(?=.*[^a-zA-Z0-9]).{8,}$'
    if search(regex,word):
        return True
    else:
        return False
    
# def token_validator(token,user_id):
#     decoded_token=decode(token,'uoqdoolW0ZPOBI_qGNjpXnlpAPW3iNi3rS3_9NL36xo',algorithms=['HS256'])
#     if decoded_token.get("id")==user_id or decoded_token.get("email")==user_id:
#         return True
#     else:
#         return False
        


