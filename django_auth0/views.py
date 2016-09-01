# -*- coding: utf-8 -*-
from .auth_helpers import process_login
from django.shortcuts import redirect


def auth_callback(request):
    return process_login(request)

def log_out(request):
    user = request.session.pop('profile')
    client_id = user['clientID']
    return redirect('https://shjd.auth0.com/v2/logout?returnTo=http://127.0.0.1:8000/speech/&client_id={}'.format(client_id))

def log_in(request):
    return redirect('https://shjd.auth0.com/authorize?response_type=code&scope=openid%20profile&client_id=GfnvKP8rFiGCaBXauuNEulqY8EapxJmp&redirect_uri=http://127.0.0.1:8000/auth/callback/?&connection=Username-Password-Authentication')
