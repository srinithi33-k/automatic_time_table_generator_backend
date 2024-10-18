from time_table_apis.source.common.common_utils import is_password,is_email
# from psycopg2 import IntegrityError
from time_table_apis.source.common.common_utils import cursor_creater
from time_table_apis.source.common.constants import GOOD_JSON,ERROR_JSON
from base64 import b64encode
from time_table_apis.source.common.query_constants import FETCH_ALL_STAFF_DETAILS,FETCH_CLASSROOM_COURSES,FETCH_TIME_SLOT,FETCH_CLASSROOM,FETCH_SEM
from json import loads
from django.http import JsonResponse
from datetime import datetime
from mysql.connector import IntegrityError

 
class TimeTableGenerator:
    @staticmethod
    def time_table_generator(request):
        try:
            connect,cursor=cursor_creater()
            sample_dict={"sem_no":"3"}
            query0=FETCH_SEM
            cursor.execute(query0)
            record = cursor.fetchone()
            sem_dict={"ODD":[1,3,5,7],
                      "EVEN":[2,4,6,8]}
            if sample_dict["sem_no"] not in sem_dict[record]:
                raise Exception("Generation not allowed! because it impact the current running semester")
            
            
            query=FETCH_CLASSROOM 
            cursor.execute(query)
            classroom=cursor.fetchall()
            query1=FETCH_TIME_SLOT
            cursor.execute(query1)
            timeslot=cursor.fetchall()
            query2=FETCH_ALL_STAFF_DETAILS
            cursor.execute(query2)
            print(timeslot)
            staff=cursor.fetchall()
            # query3=FETCH_CLASSROOM_COURSES
            # cursor.execute(query3)
            # classroom_courses=cursor.fetchall()
            GOOD_JSON["datas"]=classroom,timeslot,staff
            print(GOOD_JSON)
        except Exception as error:
            print( error)     