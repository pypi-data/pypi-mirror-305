from Utils.errors import MissingParameterException, WrongTypeException, ForbiddenException
from Utils.enum.method import Method
from .response import api_object
from .errors import BaseException
from Utils.view import UtilView

class Endpoint(object):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.method = self._get_method()
        self.params = request.query_params
        self.body = request.data
        self.api_object = api_object
        self.m_args = {}
        self.args = args
        self.kwargs = kwargs
        self.setup_parameters()
        

    def _get_method(self):
        return Method.get_method(self.request.method)
    
    def setup_parameters(self):
        pass

    def _add_parameters(self, key, required=False, methods=None, default=None, type=None):
        if (isinstance(methods, list)):
            if isinstance(required, bool):
                required = [required] * len(methods)
            elif isinstance(required, list):
                if len(required) != len(methods):
                    raise ValueError("required and method must have the same length")
            
            if isinstance(type, list):
                if len(type) != len(methods):
                    raise ValueError("type and method must have the same length")
            elif type is not None:
                type = [type] * len(methods)
            else:
                type = [None] * len(methods)

            for m in methods:
                method = Method.get_method(m)
                if (method not in self.m_args):
                    self.m_args[method] = []
                self.m_args[method].append(
                    {
                        "key": key,
                        "required": required[methods.index(m)],
                        "default": default,
                        "type": type[methods.index(m)]
                    }
                )
        else:
            if isinstance(required, list):
                raise ValueError("required must be a boolean")
            if isinstance(type, list):
                raise ValueError("type must be a class")
            method = Method.get_method(method)
            if (method not in self.m_args):
                self.m_args[method] = []
            self.m_args[method].append(
                {
                    "key": key,
                    "required": required,
                    "default": default,
                    "type": type
                }
            )

    @classmethod
    def as_view(cls, *initkwargs):
        views_attr = {
            "endpoint_class": cls
        }
        for attr in dir(cls):
            if attr.startswith("view_"):
                views_attr[attr.split("view_")[1]] = getattr(cls, attr)
        return UtilView.as_view(**views_attr)

    def _validate_parameters(self):
        to_validate = []
        if None in self.m_args:
            to_validate = self.m_args[None]
        if self.method in self.m_args:
            to_validate += self.m_args[self.method]
        for param in to_validate:
            if param["required"] and (param["key"] not in self.params and param["key"] not in self.body) and param["default"] is None:
                raise MissingParameterException(param)
            elif param["key"] in self.params:
                setattr(self, param["key"], self.params[param["key"]])
            elif param["key"] in self.body:
                setattr(self, param["key"], self.body[param["key"]])
            else:
                setattr(self, param["key"], param["default"])

            if param["type"] is not None and param["required"]:
                if type(getattr(self, param["key"])) != param["type"]:
                    raise WrongTypeException(param, param["type"].__name__, type(getattr(self, param["key"])).__name__)

    def process_get(self):
        return self.api_object.error("invalid_method", detail="Method not allowed", status=405)

    def process_post(self):
        return self.api_object.error("invalid_method", detail="Method not allowed",status=405)

    def process_put(self):
        return self.api_object.error("invalid_method", detail="Method not allowed", status=405)

    def process_patch(self):
        return self.api_object.error("invalid_method", detail="Method not allowed", status=405)

    def process_delete(self):
        return self.api_object.error("invalid_method", detail="Method not allowed", status=405)

    def process_option(self):
        return self.api_object.error("invalid_method", detail="Method not allowed", status=405)

    def _check_permissions(self):
        if hasattr(self, "permission_classes"):
            for permission in self.permission_classes:
                if not permission().has_permission(self.request, self):
                    raise ForbiddenException()

    def process(self):
        try:
            self._validate_parameters()
            self._check_permissions()
            if self.method == Method.OPTIONS:
                return self.process_option(*self.args, **self.kwargs)
            if self.method == Method.GET:
                return self.process_get(*self.args, **self.kwargs)
            elif self.method == Method.POST:
                return self.process_post(*self.args, **self.kwargs)
            elif self.method == Method.PUT:
                return self.process_put(*self.args, **self.kwargs)
            elif self.method == Method.PATCH:
                return self.process_patch(*self.args, **self.kwargs)
            elif self.method == Method.DELETE:
                return self.process_delete(*self.args, **self.kwargs)
            else:
                return self.api_object.error("invalid_method", detail="Invalid method", status=405)

        except Exception as e:
            print("exception", e)
            if isinstance(e, BaseException):
                return self.api_object.error(**e.err_args)
            return self.api_object.error("invalid_parameters", detail="Invalid parameters", status=400)
