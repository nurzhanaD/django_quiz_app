from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateQuizForm
from .models import Quiz

def home(request):
    quizes = Quiz.objects.all()
    context = {'quizes': quizes}
    return render(request,'quiz/home.html',context)

def create(request):
    if request.method == 'POST':
        form = CreateQuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateQuizForm()
    context = {'form':form}
    return render(request,'quiz/create.html',context)

def vote(request,quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)

    if request.method == 'POST':
        selected_option = request.POST['quiz']
        if selected_option == 'option1':
            quiz.option_one_count += 1
        elif selected_option == 'option2':
            quiz.option_two_count += 1
        elif selected_option == 'option3':
            quiz.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid Form')

        quiz.save()

        return redirect('results', quiz.id)

    context = {
        'quiz':quiz
    }
    return render(request,'quiz/vote.html',context)

def results(request,quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    context = {'quiz':quiz}
    return render(request,'quiz/results.html',context)
