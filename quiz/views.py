from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages 
from .forms import QuizSetForm, QuizFormSet
from .models import QuizSet, Quiz
from django.contrib import messages

# Create your views here.

def get_start_page(request):
    return render(request, 'quiz/startPage.html', {})

def get_generate_page(request):
    if request.method == 'POST':
        quiz_set_form = QuizSetForm(request.POST)
        quiz_form_set = QuizFormSet(request.POST)
        post_ctx = {
            'quiz_set_form':quiz_set_form,
            'quiz_form_set': quiz_form_set
        }
        if quiz_set_form.is_valid() and quiz_form_set.is_valid():
            quiz_set = quiz_set_form.save()
            quizzes = quiz_form_set.save(commit=False)
            if len(quizzes) < 7:
                messages.error(request, '7문제의 선택지와 답을 모두 입력해주세요.')
                return render(request, 'quiz/generatePage.html', post_ctx)
            for quiz in quizzes:
                quiz.quiz_set_id = quiz_set
            quiz_form_set.save()
            return redirect(f'/generate/{quiz_set}')
        else:
             messages.error(request, '문제 혹은 이름 입력을 확인해 주세요.')
             return render(request, 'quiz/generatePage.html', post_ctx)
    else:
        quiz_set_form = QuizSetForm()
        quiz_form_set = QuizFormSet(queryset=Quiz.objects.none())
        return render(request, 'quiz/generatePage.html', {
            'quiz_set_form':quiz_set_form,
            'quiz_form_set': quiz_form_set
        })

def get_generate_result_page(request, quiz_set_id):
    return render(request, 'quiz/generateResultPage.html', {'quiz_set_id':quiz_set_id})

def get_solve_page(request, quiz_set_id):
    quizes = Quiz.objects.filter(quiz_set_id = quiz_set_id)
    return render(request, 'quiz/solvePage.html', {'quiz_set_id':quiz_set_id,'quizes':quizes})
def get_result_page(request, quiz_set_id, result_id):
    return render(request, 'quiz/resultPage.html', {'quiz_set_id':quiz_set_id,'result_id':result_id})