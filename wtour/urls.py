from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('poll_state', views.poll_state,name='poll_state'),
    path('test', views.test,name='test'),
]