from rest_framework.views import exception_handler
from Utils.response import api_object

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    # if not response:
    #     return api_object.error(status=500, error="Internal Server Error")
    detail = response.data['detail'] if "detail" in response.data else None
    data = response.data["messages"] if "messages" in response.data else None
    code = response.data['detail'].code if "detail" in response.data else None
    return api_object.error(status=response.status_code, error=code
                            , detail=detail, data=data)
