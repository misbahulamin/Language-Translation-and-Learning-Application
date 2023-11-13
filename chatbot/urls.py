







from django.urls import path
from .views import Mybot

# app_name = 'translation'

urlpatterns = [
    
    
    path('mybot/', Mybot.as_view(), name='mybot'),
   
    # Add other URL patterns as needed
    
]
