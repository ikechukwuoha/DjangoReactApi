from django.shortcuts import render
from django.contrib.auth import get_user_model


def landingPage(request):
    page = 'landingpage'
    context = {
        'page': page,
    }
    return render(request, 'users/landingpage.html', context)