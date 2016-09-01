# -*- coding: utf-8 -*-
from .auth_helpers import process_login, process_logout


def auth_callback(request):
    return process_login(request)

def log_out(request):
    return process_logout(request)
