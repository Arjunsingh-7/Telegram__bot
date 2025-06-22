from django.urls import path
from .views import public_api, protected_api

urlpatterns = [
    path('public/', public_api, name='public'),
    path('protected/', protected_api, name='protected'),
]
