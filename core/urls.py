from core import views
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('api/dapau', views.dapau),
    path('api/login', views.login),
    path('api/logout', views.logout),
    path('api/whoami', views.whoami),
    path('api/settings', views.settings),

    path('api/list_group_messages', views.list_group_messages),
    path('api/list_atendimento_messages', views.list_atendimento_messages),
    path('api/encerra_atendimento', views.encerra_atendimento),
    path('api/change_user_mode', views.change_user_mode),
]
