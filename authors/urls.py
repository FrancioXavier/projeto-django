from django.urls import path

from . import views

urlpatterns = [
    path('register/', view=views.register_view, name='register')
]