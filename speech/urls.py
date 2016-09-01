from django.conf.urls import  url
from speech import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^record', views.record, name='record'),
        url(r'^annotate', views.annotate, name='annotate'),
        url(r'^build', views.build, name='build'),
        url(r'^synthesize', views.synthesize, name='synthesize'),

]