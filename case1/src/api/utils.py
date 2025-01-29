import logging
import traceback

from rest_framework.exceptions import APIException, ErrorDetail, ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def dijii_exception_handler(exc, context: dict):
    response = exception_handler(exc, context)
    tb = traceback.extract_tb(exc.__traceback__)
    file_name, line_number, func_name, line_code = tb[-1]

    if response is not None:
        # DRF Exceptions
        if isinstance(exc, APIException):
            pre_response = {
                "detail": exc.detail,
                "status": exc.status_code,
                "error": exc.default_code,
            }
            # Validation Error
            if isinstance(exc, ValidationError):
                pre_response["detail"] = "Validation error please contact with support."
                issues: list[dict[str, str]] = []
                for k in response.data:  # type: ignore
                    if isinstance(k, ErrorDetail):
                        messages = k
                        k = "non_field_errors"
                    else:
                        messages = response.data[k]  # type: ignore

                    if not isinstance(messages, list):
                        messages = [messages]

                    for message in messages:
                        if k == "non_field_errors":
                            issues.append({"message": message})
                        else:
                            issues.append({"path": k, "message": message})

                pre_response["issues"] = issues

        # Non-DRF Exceptions
        else:
            logger.error(
                f"{exc.__class__.__name__} at {file_name}:{line_number} in '{func_name}()' -> {line_code}\nException Detail: {exc}"
            )
            pre_response = {
                "detail": "Internal Server Error",
                "status": 500,
                "error": "server_error",
            }

        response.data = pre_response

    else:
        logger.error(
            f"{exc.__class__.__name__} at {file_name}:{line_number} in '{func_name}()' -> {line_code}\nException Detail: {exc}"
        )
        response = Response(
            {
                "detail": str(exc),
                "status": 500,
                "error": "server_error",
            },
            status=500,
        )
    return response
