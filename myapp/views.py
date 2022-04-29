from random import shuffle
import csv
import io

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Question, Result, Topic, Answer

def home(request):
    topics = Topic.objects.all()
    context = {
        'topics':topics,
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def question(request, slug):
    quiz = Topic.objects.get(slug=slug)
    questions = Question.objects.filter(topic = quiz)
    answers = Answer.objects.filter(question__in=questions)
    answers = list(answers)
    questions = list(questions)
    shuffle(answers)
    shuffle(questions)
    if request.method == 'POST':
        correct = 0
        wrong = 0
        for q in questions:
            if request.POST.get(q.name) == "True":
                correct += 1
            else:
                wrong += 1
        Result.objects.create(
            user=User.objects.get(username=request.user.username),
            total_question=len(questions),
            correct=correct,
            topic=quiz,
        )
        context = {
            'questions': questions,
            'answers': answers,
            'correct': correct,
            'wrong': wrong,
            'total_question': len(questions),
            'user': request.user.username,
            'total': round(correct*100/len(questions), 2),
        }
        return render(request, 'result.html',context)
    context = {
        'questions': questions,
        'answers': answers,
    }
    return render(request, 'question.html', context)

def result_list(request):
    results = Result.objects.all()
    context = {
        'results':results,
    }
    return render(request, 'result_list.html', context)

def users_upload(request):
    users = User.objects.all()
    if request.method == "POST":
        csv_file = request.FILES['users']
        file_data = csv_file.read().decode("utf-8")
        io_string = io.StringIO(file_data)
        next(io_string)
        for row in csv.reader(io_string, delimiter=','):
            User.objects.create_user(first_name=row[0], last_name=row[1],
                                     username=row[2], password=row[3],
                                     email=row[4])

    return render(request, 'users_upload.html', {'users':users})