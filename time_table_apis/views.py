from rest_framework.decorators import api_view
from time_table_apis.source.modules.Register import RegisterUser
from time_table_apis.source.modules.Login import LoginUser
# from time_table_apis.source.modules.NominationDetails import NominationDetails
# from time_table_apis.source.modules.EventRegister import EventRegister


@api_view(['post'])
def register_user_view(request):
    return RegisterUser.register_user(request)

@api_view(['post'])
def login_user_view(request):
    return LoginUser.login_user(request)

