from rest_framework.permissions import BasePermission
from Common.models import Member

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == Member.Role.ADMIN)

class IsExpert(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == Member.Role.EXPERT)
    
class IsEditor(BasePermission):
    def has_permission(self, request, view):
        print(request.user.is_editor)
        return bool(request.user and request.user.is_authenticated and (request.user.is_editor or request.user.role == Member.Role.ADMIN))
