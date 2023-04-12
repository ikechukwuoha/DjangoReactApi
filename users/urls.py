from django.urls import path
from . import views as users_view

app_name = 'users'

urlpatterns = [
    path('', users_view.landingPage, name='landingpage')
]