from django.shortcuts import render

# Create your views here.

def get_start(request):
    return render(request, 'quiz/start.html', {})