from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

# def index(request):
#     return HttpResponse('ola mundo. voce esta no index da aplicação polls.')

def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:10]
    context = {
        'latest_question_list':latest_questions_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
	response = f'voce esta olhando para os resutados da questão {question_id}'
	return HttpResponse(response)

def vote(request, question_id):
	return HttpResponse(f'voce esta votando na questão {question_id}')