from django.urls import path
from . import views

urlpatterns = [
    path("user",views.user),
    path("index",views.index)
]
