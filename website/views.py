from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def stock_tracker(request):
    return render(request, 'stock_tracker.html', {})