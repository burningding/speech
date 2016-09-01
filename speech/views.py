from django.shortcuts import render
from django.http import HttpResponse
#from django_auth0.auth_backend import Auth0Backend
#from django_auth0.auth_helpers import process_login

def index(request):
    #process_login(request)
    #authback = Auth0Backend()
    #if authback.authenticate():
    #    context_dict = {'boldmessage': "Authenticate!"}
    #else:
    #    context_dict = {'boldmessage': "I am bold font from the context"}

    if request.session._session.get('profile'):
        profile = request.session._session['profile']
        context_dict = {'boldmessage': profile['name']}
    else:
        context_dict = {'boldmessage': "Hello"}
    return render(request, 'speech/index.html', context_dict)

def record(request):
    infotext = "The voiced dental fricative is pronounced with the tip of the tongue against the teeth, while your glottis vibrates. This is a rare sound that does not exist in most European and Asian languages"
    context_dict = {'infotext': infotext}
    return render(request, 'speech/record.html', context_dict)

def annotate(request):
    return render(request, 'speech/annotate.html')

def build(request):
    return render(request, 'speech/build.html')

def synthesize(request):
    return render(request, 'speech/synthesize.html')

# Create your views here.
