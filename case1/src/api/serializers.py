from rest_framework import serializers
from rest_framework.exceptions import (
    MethodNotAllowed,
    NotAuthenticated,
    NotFound,
    PermissionDenied,
)


class UnAuthorizedSerializer(serializers.Serializer):
    detail = serializers.CharField(
        default=NotAuthenticated.default_detail, read_only=True
    )
    error = serializers.CharField(default=NotAuthenticated.default_code, read_only=True)
    status = serializers.IntegerField(
        default=NotAuthenticated.status_code, read_only=True
    )


class PermissionDeniedSerializer(serializers.Serializer):
    detail = serializers.CharField(
        default=PermissionDenied.default_detail, read_only=True
    )
    error = serializers.CharField(default=PermissionDenied.default_code, read_only=True)
    status = serializers.IntegerField(
        default=PermissionDenied.status_code, read_only=True
    )


class MethodNotAllowedSerializer(serializers.Serializer):
    detail = serializers.CharField(
        default=MethodNotAllowed.default_detail, read_only=True
    )
    error = serializers.CharField(default=MethodNotAllowed.default_code, read_only=True)
    status = serializers.IntegerField(
        default=MethodNotAllowed.status_code, read_only=True
    )


class NotFoundSerializer(serializers.Serializer):
    detail = serializers.CharField(default=NotFound.default_detail, read_only=True)
    error = serializers.CharField(default=NotFound.default_code, read_only=True)
    status = serializers.IntegerField(default=NotFound.status_code, read_only=True)


class DefaultExceptionSerializer(serializers.Serializer):
    class IssueSerializer(serializers.Serializer):
        path = serializers.CharField(required=False)
        message = serializers.CharField(required=True)

    detail = serializers.CharField(required=False)
    error = serializers.CharField(required=False)
    status = serializers.IntegerField(required=False)
    issues = IssueSerializer(required=False, many=True)
