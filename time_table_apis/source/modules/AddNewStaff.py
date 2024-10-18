from time_table_apis.source.common.common_utils import is_email,cursor_creater
from time_table_apis.source.common.query_constants import insert_query_marker
from jwt import decode
from time_table_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from django.http import JsonResponse
from json import loads

class AddStaffDetails:
    @staticmethod
    def add_staff_details(request):
        try:
            sample_dict={"role_name":"DEAN","staff_name":"kaviyapriya","roll_number":"4111987","email_id":"kaviyapriya@gamil.com"}
            if not sample_dict["role_name"] in ['DEAN','HOD']:
                raise Exception ("invalid request")
            sample_dict.pop("role_name")
            connect,cursor=cursor_creater()
            sample_dict={key:"'"+ value +"'" for key,value in sample_dict.items()}
            insert_query=insert_query_marker("authorized_staff",sample_dict)
            cursor.execute(insert_query)
            connect.commit()
            
            print(GOOD_JSON)
            
            # return JsonResponse(GOOD_JSON,status=200)
        except Exception as error:
            print( error) 
            # return JsonResponse(ERROR_JSON,status=400)   
