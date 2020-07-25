
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     path('', include("home.urls")),
    path('addrecord/', include("addrecord.urls")),
    path('showrecord/', include("showrecord.urls")),
]
