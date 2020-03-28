from django.urls import path
from . import views

urlpatterns = [
    path('create.html', views.create_view, name="create"),
]
