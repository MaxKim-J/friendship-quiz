from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages 
from .forms import QuizSetForm, QuizFormSet
from .models import QuizSet, Quiz, Answer
from django.contrib import messages

# Create your views here.

def get_start_page(request):
    return render(request, 'quiz/startPage.html', {})


def get_generate_page(request):
    if request.method == 'POST':
        quiz_set_form = QuizSetForm(request.POST)
        quiz_form_set = QuizFormSet(request.POST)
        post_ctx = {
            'quiz_set_form': quiz_set_form,
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
             messages.error(request, '다 채워지지 않은 문제, 답안, 정답 입력을 확인해 주세요.')
             return render(request, 'quiz/generatePage.html', post_ctx)
    else:
        quiz_set_form = QuizSetForm()
        quiz_form_set = QuizFormSet(queryset=Quiz.objects.none())
        return render(request, 'quiz/generatePage.html', {
            'quiz_set_form': quiz_set_form,
            'quiz_form_set': quiz_form_set
        })


def get_generate_result_page(request, quiz_set_id):
    return render(request, 'quiz/generateResultPage.html', {
        'quiz_set_id': quiz_set_id,
    })


def get_solve_page(request, quiz_set_id):
    quizes = Quiz.objects.filter(quiz_set_id = quiz_set_id)
    previous_checked = [0 for x in range(7)]
    if request.method == 'POST':

        if len(request.POST) < 9 or request.POST['guestname'] == None:
            messages.error(request,'이름과 모든 문제의 답을 입력해주세요.')
            for i in range(1,8):
                if str(i) in dict(request.POST).keys():
                    previous_checked[i-1] = int(request.POST[str(i)])
            return render(request, 'quiz/solvePage.html', {'quiz_set_id':quiz_set_id,'quizes':zip(quizes,previous_checked), 'guestname': request.POST['guestname']})

        quiz_set = get_object_or_404(QuizSet, pk=quiz_set_id)
        point = 0
        cnt = 1
        for quiz in quizes:
            if quiz.answer == int(request.POST[str(cnt)]):
                point += 1
            cnt += 1
    
        new_anwer = Answer()
        new_anwer.quiz_set_id = quiz_set
        new_anwer.guest = request.POST['guestname']
        new_anwer.points = point
        new_anwer.save()

        return redirect(f'/result/{quiz_set_id}/{new_anwer.id}')

    return render(request, 'quiz/solvePage.html', {'quiz_set_id':quiz_set_id,'quizes':zip(quizes,previous_checked)})


def get_result_page(request, quiz_set_id, result_id):
    quiz_set = QuizSet.objects.get(id=quiz_set_id)
    host = quiz_set.host
    answer = Answer.objects.get(id=result_id)
    points = answer.points
    guest = answer.guest
    result_sets = Answer.objects.filter(quiz_set_id=quiz_set_id).order_by('-points')[:5]
    return render(request, 'quiz/resultPage.html', {'quiz_set_id':quiz_set_id,'result_id':result_id, 'points':points, 'host': host, 'guest':guest, 'result_sets':result_sets})

