from rest_framework import permissions


class AdminOrReadonly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        # return request.method == 'GET' or admin_permission
        if request.method in permissions.SAFE_METHODS:  # Get Request

            return True
        else:

            return admin_permission


class ReviewUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # Get Request

            # Check permissions for read-only request
            return True
        else:

            # Check permissions for write request
            return obj.review_user == request.user
            # return obj.rating == 1
#
