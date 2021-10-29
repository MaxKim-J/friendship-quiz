from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages 
from .forms import QuizSetForm, QuizFormSet
from .models import QuizSet, Quiz


# Create your views here.

def get_start_page(request):
    return render(request, 'quiz/startPage.html', {})

def get_generate_page(request):
    if request.method == 'POST':
        quiz_set_form = QuizSetForm(request.POST)
        quiz_form_set = QuizFormSet(request.POST)
        if quiz_set_form.is_valid() and quiz_form_set.is_valid():
            quiz_set = quiz_set_form.save()
            quizzes = quiz_form_set.save(commit=False)
            for quiz in quizzes:
                quiz.quiz_set_id = quiz_set
            quiz_form_set.save()
            return redirect(f'/generate/{quiz_set}')
        else:
            # with 에러 메시지
             return render(request, 'quiz/generatePage.html', {
                'quiz_set_order':[i for i in range(1,8)],
                'quiz_set_form':quiz_set_form,
                'quiz_form_set': quiz_form_set
            })
    else:
        quiz_set_form = QuizSetForm()
        quiz_form_set = QuizFormSet(queryset=Quiz.objects.none())
        return render(request, 'quiz/generatePage.html', {
            'quiz_set_order':[i for i in range(1,8)],
            'quiz_set_form':quiz_set_form,
            'quiz_form_set': quiz_form_set
        })

def get_generate_result_page(request, quiz_set_id):
    return render(request, 'quiz/generateResultPage.html', {'quiz_set_id':quiz_set_id})

def get_solve_page(request, quiz_set_id):
    return render(request, 'quiz/solvePage.html', {'quiz_set_id':quiz_set_id})

def get_result_page(request, quiz_set_id, result_id):
    return render(request, 'quiz/resultPage.html', {'quiz_set_id':quiz_set_id,'result_id':result_id})