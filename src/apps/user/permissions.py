from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.request import Request


class IsAuthenticatedAndIsActive(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_active


class IsUser(BasePermission):
    def has_permission(self, request: Request, view):
        return request.user
