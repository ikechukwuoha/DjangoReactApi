from django.shortcuts import render

def homePage(request):
    page = 'home'
    context = {
        'page': page
    }
    return render(request, 'meether_app/home', context)