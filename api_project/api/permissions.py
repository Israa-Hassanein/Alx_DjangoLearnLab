# api/permissions.py

from rest_framework import permissions

class IsCreatorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.creator or request.user.is_staff:
            return True
        return False
