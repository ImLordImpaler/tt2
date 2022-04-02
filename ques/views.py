from django.shortcuts import render
from ques.models import *

def index(request):
    return render(request ,  'base.html')


def questionList(request):
    ques = Question.objects.all()
    params = {
        'ques':ques
    }
    return render(request , 'questionList.html', params )


def question(request ,pk):
    ques = Question.objects.get(id=pk)

    params = {
        'ques':ques
    }
    return render(request , 'question.html', params )