
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Api.as_view())
    
]

