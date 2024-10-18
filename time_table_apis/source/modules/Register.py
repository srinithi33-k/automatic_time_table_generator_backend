from time_table_apis.source.common.common_utils import is_password,is_email
# from psycopg2 import IntegrityError
from time_table_apis.source.common.common_utils import cursor_creater
from time_table_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from base64 import b64encode
from time_table_apis.source.common.query_constants import insert_query_marker,FETCH_AUTHORIZED_USERS
from json import loads
from django.http import JsonResponse
from datetime import datetime
from mysql.connector import IntegrityError

 
class RegisterUser:
    @staticmethod
    def register_user(request):
        try:
        
            # sample_dict={"staff_name":"supriya","password":"Supriya$567","email_id":"supriya@example.com","roll_number":41111494,"role_id":3001}
            
            print(sample_dict)
            sample_dict=loads(request.body)
            if not is_email(sample_dict.get("email_id")):
                raise Exception("invalid email")
            if not is_password(sample_dict.get("password")):
                raise Exception("invalid password")
            encoded_password =b64encode(sample_dict.get("password").encode()).decode()
            sample_dict["roll_number"]=str(sample_dict.get("roll_number"))
            sample_dict["role_id"]=str(sample_dict.get("role_id"))
            sample_dict["password"]=encoded_password
            connect,cursor = cursor_creater()
            field = (sample_dict.get("roll_number"),)
            select_query = FETCH_AUTHORIZED_USERS % field
            cursor.execute(select_query)
            
            if cursor.rowcount == 1:
                sample_dict={key:"'"+ value +"'" for key,value in sample_dict.items()}
                insert_query=insert_query_marker("staff",sample_dict)
                cursor.execute(insert_query)
                connect.commit()
                print(GOOD_JSON)
                return JsonResponse(GOOD_JSON,status=200)
            else:
                raise Exception("user authorization for faculty not allowed! please contact university for more information.")   
        except IntegrityError as error:
            error_message=str(error)
            if 'duplicate key value violates unique constraint' in error_message:
                ERROR_JSON["reason"]="user already exist!"
                return JsonResponse(ERROR_JSON,status=400)
        except Exception as error:
            ERROR_JSON["reason"]=str(error)
            print(ERROR_JSON)  
            return JsonResponse(ERROR_JSON,status=400)  
      
