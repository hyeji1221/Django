from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-create_date') # -는 역방향을 의미
    context = {'question_list': question_list}

    # render는 파이썬 데이터를 HTML로 변환한다.
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    # pybo 내용 출력
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)