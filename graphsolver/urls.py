from django.urls import path
from . import views
from django.conf.urls import url

app_name='graphsolver'
urlpatterns = [
    path("", views.index, name="index"),
]