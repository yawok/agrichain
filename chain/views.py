from django.shortcuts import render

def index(request):
    template = "chain/index.html"
    
    return render(request, template)