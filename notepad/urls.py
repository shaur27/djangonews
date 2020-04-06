from django.urls import path
from .views import create_view
#from .views import list_view

urlpatterns = [
    path('create/', create_view, name="create"),
  #  path('list/', list_view, name="list"),
]
