from rest_framework import permissions


class IsRead(permissions.BasePermission):
    def has_permission(self, request, view):  # noqa: ARG002 unused-method-argument
        return request.method in permissions.SAFE_METHODS


class IsUpdate(permissions.BasePermission):
    def has_permission(self, request, view):  # noqa: ARG002 unused-method-argument
        return request.method in ("PUT", "PATCH")


class IsPatch(permissions.BasePermission):
    def has_permission(self, request, view):  # noqa: ARG002 unused-method-argument
        return request.method == "PATCH"


class IsPost(permissions.BasePermission):
    def has_permission(self, request, view):  # noqa: ARG002 unused-method-argument
        return request.method == "POST"


class IsWrite(permissions.BasePermission):
    def has_permission(self, request, view):  # noqa: ARG002 unused-method-argument
        return request.method not in permissions.SAFE_METHODS
