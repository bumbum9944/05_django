from django.shortcuts import render, redirect
from .models import Question, Answer

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    user = request.GET.get('user')
    title = request.GET.get('title')
    content = request.GET.get('content')
    question = Question(user=user, title=title, content=content)
    question.save()
    return redirect('/questions/')

def index(request):
    questions = Question.objects.all()
    answer = Answer.objects.all()
    context = {
        'questions': questions,
        'answer': answer,
    }
    return render(request, 'index.html', context)

def answer_create(request, question_id):
    content = request.GET.get('content')
    question = Question.objects.get(id=question_id)

    answer = Answer(content=content, question=question)
    answer.save()

    return redirect('/questions/')