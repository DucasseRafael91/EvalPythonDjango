from django.shortcuts import render

def index(request):
    return render(request, "competences/index.html")