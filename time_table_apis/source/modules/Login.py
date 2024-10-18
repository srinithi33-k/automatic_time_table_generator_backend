from time_table_apis.source.common.common_utils import cursor_creater
from base64 import b64decode
from time_table_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from jwt import encode
from json import loads
from django.http import JsonResponse
from time_table_apis.source.common.query_constants import FETCH_LOGIN_USERS
from json import loads


class LoginUser:
    @staticmethod
    def login_user(request):
        try:
            # sample_dict={"email_id":"srinithi33.k@gmail.com","password":"P4r1ty@sri"}
            sample_dict=loads(request.body)
            # sample_dict={key:"'"+ value +"'" for key,value in sample_dict.items()}
            field=(sample_dict.get("email_id"),)
            select_query = FETCH_LOGIN_USERS % field
            # print(select_query)
            connect,cursor=cursor_creater()
            cursor.execute(select_query)
            if cursor.rowcount == 1:
                record=cursor.fetchone()[0][0]
                # print(record)
                decoded_crtpassword = b64decode(record.get("password")).decode()
                if decoded_crtpassword==sample_dict.get("password"):
                    token=encode(sample_dict,'uoqdoolW0ZPOBI_qGNjpXnlpAPW3iNi3rS3_9NL36xo',algorithm='HS256')
                    GOOD_JSON["token"]=token
                    print(GOOD_JSON)
                    return JsonResponse(GOOD_JSON,status=200)
                else:
                    raise Exception("Invalid email_id or password!")   
        
            else:
                raise Exception("user does not exist! try to signup")        
        except Exception as error:
            ERROR_JSON["reason"]=str(error)
            print(ERROR_JSON)
            return JsonResponse (ERROR_JSON,status=400)       
