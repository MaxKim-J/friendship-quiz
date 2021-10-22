from django.shortcuts import render

# Create your views here.

def get_start_page(request):
    return render(request, 'quiz/startPage.html', {})

def get_generate_page(request):
    return render(request, 'quiz/generatePage.html', {})

def get_generate_result_page(request, quiz_set_id):
    return render(request, 'quiz/generateResultPage.html', {'quiz_set_id':quiz_set_id})

def get_solve_page(request, quiz_set_id):
    return render(request, 'quiz/solvePage.html', {'quiz_set_id':quiz_set_id})

def get_result_page(request, quiz_set_id, result_id):
    return render(request, 'quiz/resultPage.html', {'quiz_set_id':quiz_set_id,'result_id':result_id})