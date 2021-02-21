from django.urls import path
from . import views

urlpatterns = [
    # root path, view function
    path('', views.index)
]
