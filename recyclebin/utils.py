from threading import current_thread
from django.utils.deprecation import MiddlewareMixin
from django.utils.encoding import force_text
from rest_framework import status
from rest_framework.exceptions import APIException

_requests = {}

def get_current_request():
    t = current_thread()
    if t not in _requests:
        return None
    return _requests[t]


class RequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        _requests[current_thread()] = request


class CustomValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, field, status_code):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_text(detail)}
        else: 
            self.detail = {'detail': force_text(self.default_detail)}