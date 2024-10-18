from time_table_apis.source.common.common_utils import is_email,cursor_creater
from time_table_apis.source.common.query_constants import FETCH_SELECT_STAFF
from jwt import decode
from time_table_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from django.http import JsonResponse
from json import loads

class GetStaffDetails:
    @staticmethod
    def get_staff_details(request):
        try:
            # sample_dict=loads(request.body)
            sample_dict={"email_id":"srinithi33.k@gmail.com",'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbF9pZCI6InNyaW5pdGhpMzMua0BnbWFpbC5jb20iLCJwYXNzd29yZCI6IlA0cjF0eUBzcmkifQ.UAiTj8WLa1Ety1E6dh1mB33Zt5nPEQahmVA3jc9LDZ4'}
            if not is_email(sample_dict["email_id"]):
                raise Exception ("invalid email_id")
            # if not token_validator(request.headers.get("Authorization"),sample_dict.get("email_id")):
            #     raise Exception("invalid user!")
            connect,cursor=cursor_creater()
            field=sample_dict.get("email_id"),
            query=FETCH_SELECT_STAFF % field
            cursor.execute(query)
            
            record = cursor.fetchone()[0]
            if len(record) == 1:
                GOOD_JSON["data"]=record[0]
                print(GOOD_JSON)
                # return JsonResponse(GOOD_JSON,status=200)
            else:
                raise Exception("Invalid emailid!")      
                
        except Exception as error:
            print( error) 
            # return JsonResponse(ERROR_JSON,status=400)   