from django.shortcuts import render
from .models import Article

def map_prev(request):
    return render(request, 'map/map_prev.html', {})#'articles':article
