from django.shortcuts import render


def index(request):
    return render(request, 'diary/main.html')