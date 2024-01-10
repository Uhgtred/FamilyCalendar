#!/usr/bin/env python3
# @author      Markus Kösters

from django.urls import path, include

urlpatterns = [
    path('', include(('api.urls', 'api'), namespace='api')),
]
