from rest_framework.response import Response
from Utils.settings import settings

class APIObject:
    def __init__(self, name, version, url):
        self.name = name
        self.version = version
        self.url = url

    @property
    def response(self):
        return self.Reponse(self)
    
    @property
    def error(self):
        return self.Error(self)

    class Reponse:
        def __init__(self, api_object):
            self.api_object = api_object
            self.res = {"api": {"name": api_object.name, "version": api_object.version, "url": api_object.url}}

        def __call__(self, message=None, detail=None, data=None, status=200, code=None):
            if message is not None:
                self.res["message"] = message

            if detail is not None:
                self.res["detail"] = detail

            if data is not None:
                self.res["data"] = data

            if code is not None:
                self.res["code"] = code

            self.res["status"] = status
            self.res["type"] = "response"

            return Response(self.res, status=status)

        def raw(self):
            return self.res
    
    class Error:
        def __init__(self, api_object):
            self.api_object = api_object
            self.res = {"api": {"name": api_object.name, "version": api_object.version, "url": api_object.url}}

        def __call__(self, error, detail=None, status=400, data=None, type="error"):
            if detail is not None:
                self.res["detail"] = detail
            if data is not None:
                self.res["data"] = data
            
            self.res["error"] = error
            self.res["type"] = type
            self.res["status"] = status

            return Response(self.res, status=status)

        def raw(self):
            return self.res

    def __str__(self):
        return f"APIObject {self.name} ({self.version}) : {self.url}"
    
    def __repr__(self):
        return f"APIObject {self.name} ({self.version}) : {self.url}"
    
api_object = APIObject(settings.APP_NAME, settings.APP_VERSION, settings.APP_URL)
