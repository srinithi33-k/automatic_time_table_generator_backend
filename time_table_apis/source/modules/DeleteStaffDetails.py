from time_table_apis.source.common.common_utils import is_email,cursor_creater
from time_table_apis.source.common.query_constants import DELETE_STAFF,DELETE_AUTHORIZED_STAFF,DELETE_STAFF_COURSES
from jwt import decode
from time_table_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from django.http import JsonResponse
from json import loads

class DeleteStaffDetails:
    @staticmethod
    def delete_staff_details(request):
        try:
            sample_dict={"email_id":"supriya@example.com","staff_id":2008,"role_name":"DEAN"}
            if not sample_dict["role_name"] in ['DEAN','HOD']:
                raise Exception ("invalid request")
            connect,cursor=cursor_creater()
            field=(sample_dict.get("staff_id"),)
            query1=DELETE_STAFF_COURSES % field
            cursor.execute(query1)
            connect.commit()
            query2=DELETE_STAFF % field
            cursor.execute(query2)
            connect.commit()
            field2=(sample_dict.get("email_id"),)
            query3=DELETE_AUTHORIZED_STAFF% field2
            cursor.execute(query3)
            connect.commit()
            print(GOOD_JSON)
            
            # return JsonResponse(GOOD_JSON,status=200)
        except Exception as error:
            print( error) 
            # return JsonResponse(ERROR_JSON,status=400)   








