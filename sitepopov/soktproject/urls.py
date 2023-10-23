from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('record/', views.record, name='record'),
    path('history/', views.history, name='history'),
    path('way/', views.way, name='way'),
    path('photo/', views.photo, name='photo')
]