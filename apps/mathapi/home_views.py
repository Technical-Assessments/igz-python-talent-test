from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, "index.html")


def documentation(request, *args, **kwargs):
    return render(request, "documentation.html")