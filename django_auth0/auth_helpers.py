# -*- coding: utf-8 -*-
import json
import requests
import sys
sys.path.append('../')

from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import redirect
from .utils import get_config
from .auth_backend import Auth0Backend
from speech.views import index


def process_login(request):
    """
    Default handler to login user
    :param request: HttpRequest
    """
    code = request.GET.get('code', '')
    config = get_config()
    json_header = {'content-type': 'application/json'}
    token_url = 'https://%s/oauth/token' % config['AUTH0_DOMAIN']

    token_payload = {
        'client_id': config['AUTH0_CLIENT_ID'],
        'client_secret': config['AUTH0_SECRET'],
        'redirect_uri': config['AUTH0_CALLBACK_URL'],
        'code': code,
        'grant_type': 'authorization_code'
    }

    token_info = requests.post(token_url,
                               data=json.dumps(token_payload),
                               headers=json_header).json()

    url = 'https://%s/userinfo?access_token=%s'
    user_url = url % (config['AUTH0_DOMAIN'],
                      token_info.get('access_token', ''))

    user_info = requests.get(user_url).json()

    # We're saving all user information into the session
    request.session['profile'] = user_info
    return redirect('/speech/')
    #index(request)
    # return redirect('/speech')
    # auth0backend = Auth0Backend()
    # user = auth0backend.authenticate(**user_info)
    #
    # if user:
    #     login(request, user)
    #     return redirect(config['AUTH0_SUCCESS_URL'])
    #
    # return HttpResponse(status=400)

# def is_login(request):
#     if request.session._session.get('profile'):
#         return [True, request.session._session['profile']]
#     else:
#         return None

def process_logout(request):
    user = request.session.pop('profile')
    client_id = user['clientID']
    return redirect('https://shjd.auth0.com/v2/logout?returnTo=http://127.0.0.1:8000/speech/&client_id={}'.format(client_id))