from django.urls import path
from .views import welcome, info, join_us

urlpatterns= [
    path("", welcome),
    path('ask-us/', info),
    path("let-us-in/", join_us),
    
]