from time_table_apis.source.common.common_utils import is_email,cursor_creater
from time_table_apis.source.common.query_constants import UPDATE_COURSE
from jwt import decode
from time_table_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from django.http import JsonResponse
from json import loads

class UpdateCoursesDetails:
    @staticmethod
    def update_courses_details(request):
        try:
            sample_dict={"course_id":1001,"course_name":"software development",'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbF9pZCI6InNyaW5pdGhpMzMua0BnbWFpbC5jb20iLCJwYXNzd29yZCI6IlA0cjF0eUBzcmkifQ.UAiTj8WLa1Ety1E6dh1mB33Zt5nPEQahmVA3jc9LDZ4'}
            # if not token_validator(request.headers.get("Authorization"),sample_dict.get("email_id")):
            #     raise Exception("invalid user!")
            
            connect,cursor=cursor_creater()
            
            field=(sample_dict.get("course_name"),sample_dict.get("course_id"))
            query1=UPDATE_COURSE % field
            cursor.execute(query1)
            connect.commit()
            
            print(GOOD_JSON)
            
            # return JsonResponse(GOOD_JSON,status=200)
        except Exception as error:
            print( error) 
            # return JsonResponse(ERROR_JSON,status=400)   
