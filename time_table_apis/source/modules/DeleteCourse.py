from time_table_apis.source.common.common_utils import is_email,cursor_creater
from time_table_apis.source.common.query_constants import DELETE_COURSE,DELETE_CLASSROOM_COURSE
from jwt import decode
from time_table_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from django.http import JsonResponse
from json import loads

class DeleteCourse:
    @staticmethod
    def delete_course(request):
        try:
            sample_dict={"course_id":1000,"role_name":"DEAN"}
            if not sample_dict["role_name"] in ['DEAN','HOD']:
                raise Exception ("invalid request")
            connect,cursor=cursor_creater()
            field=(sample_dict.get("course_id"),)
            query1=DELETE_COURSE % field
            cursor.execute(query1)
            connect.commit()
            query2=DELETE_CLASSROOM_COURSE% field
            cursor.execute(query2)
            connect.commit()
            
            print(GOOD_JSON)
            # return JsonResponse(GOOD_JSON,status=200)
        except Exception as error:
            print( error) 
            # return JsonResponse(ERROR_JSON,status=400)   





   