from rest_framework.views import APIView
from .response import api_object

class UtilView(APIView):

    endpoint_class = None

    def __init__(self, **views_attrs):
        for key, value in views_attrs.items():
            setattr(self, key, value)

    def _check_endpoint(self, request, *args, **kwargs):
        if self.endpoint_class is None:
            return False
        self.endpoint_class = self.endpoint_class(request, *args, **kwargs)
        return True

    def get(self, request, *args, **kwargs):
        if not self._check_endpoint(request=request, *args, **kwargs):
            return api_object.error("Endpoint not found", status=404)
        return self.endpoint_class.process()
    
    def post(self, request, *args, **kwargs):
        if not self._check_endpoint(request=request, *args, **kwargs):
            return api_object.error("Endpoint not found", status=404)
        return self.endpoint_class.process()

    def put(self, request, *args, **kwargs):
        if not self._check_endpoint(request=request, *args, **kwargs):
            return api_object.error("Endpoint not found", status=404)
        return self.endpoint_class.process()

    def patch(self, request, *args, **kwargs):
        if not self._check_endpoint(request=request, *args, **kwargs):
            return api_object.error("Endpoint not found", status=404)
        return self.endpoint_class.process()

    def delete(self, request, *args, **kwargs):
        if not self._check_endpoint(request=request, *args, **kwargs):
            return api_object.error("Endpoint not found", status=404)
        return self.endpoint_class.process()
    
    def option(self, request, *args, **kwargs):
        if not self._check_endpoint(request=request, *args, **kwargs):
            return api_object.error("Endpoint not found", status=404)
        return self.endpoint_class.process()
