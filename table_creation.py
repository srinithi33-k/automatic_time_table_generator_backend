from source.common.common_utils import cursor_creater
from source.common.constants import GOOD_JSON,ERROR_JSON
from source.common.query_constants import STAFF,COURSE,TIME_SLOT,ROLE,CLASSROOM,CLASSROOM_COURSES,STAFF_TEACHING_COURSES,AUTHORIZED_STAFF,TIME_SLOT_BOOKING


connect,cursor =cursor_creater()
cursor.execute(TIME_SLOT_BOOKING)
connect.commit()
# # connect,cursor =cursor_creater()
cursor.execute(CLASSROOM)
connect.commit()
# connect,cursor =cursor_creater()
cursor.execute(STAFF)
connect.commit()
# connect,cursor =cursor_creater()
cursor.execute(COURSE)
connect.commit()
# connect,cursor =cursor_creater()
cursor.execute(TIME_SLOT)
connect.commit()
# connect,cursor =cursor_creater()
cursor.execute(CLASSROOM_COURSES)
connect.commit()
# connect,cursor =cursor_creater()
cursor.execute(STAFF_TEACHING_COURSES)
connect.commit()
cursor.execute(AUTHORIZED_STAFF)
connect.commit()