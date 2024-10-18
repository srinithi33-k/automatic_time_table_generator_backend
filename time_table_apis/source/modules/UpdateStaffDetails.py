from time_table_apis.source.common.common_utils import is_email,cursor_creater
from time_table_apis.source.common.query_constants import UPDATE_STAFF
from jwt import decode
from time_table_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from django.http import JsonResponse
from json import loads

class UpdateStaffDetails:
    @staticmethod
    def update_staff_details(request):
        try:
            sample_dict={"staff_id":2009,"staff_name":"shannu k"}
            
            
            connect,cursor=cursor_creater()
            
            field=(sample_dict.get("staff_name"),sample_dict.get("staff_id"))
            query1=UPDATE_STAFF % field
            cursor.execute(query1)
            connect.commit()
            
            print(GOOD_JSON)
            
            # return JsonResponse(GOOD_JSON,status=200)
        except Exception as error:
            print( error) 
            # return JsonResponse(ERROR_JSON,status=400)   
