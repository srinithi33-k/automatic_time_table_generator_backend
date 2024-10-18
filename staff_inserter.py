from json import load
from source.common.common_utils import cursor_creater
from source.common.query_constants import insert_query_marker
from source.common.common_utils import cursor_creater

with open ("source_data.json") as json_file:
    staff_data=load(json_file)
connect,cursor = cursor_creater()    
for i in staff_data:
    i={key:"'"+ value +"'" for key,value in i.items()}
    insert_query=insert_query_marker("authorized_staff",i)
    cursor.execute(insert_query)
    connect.commit()
    