from django.urls import path
from . import views as meet_app


app_name = 'meether_app'


urlpatterns = [
    path('meether_app/', meet_app.homePage, name='homePage'),
]