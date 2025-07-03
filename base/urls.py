from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('set_wave/',views.set_wave,name="setwave"),
    path('get_wave/',views.get_wave,name="getwave"),
    path('recieve_data/',views.recieve_data,name="recievedata"),
    path('latest_data/',views.latest_data,name="latestdata"),
    path('voltage_render/',views.voltage_render,name="voltagerender")
]