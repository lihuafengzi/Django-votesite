from django.http import HttpResponse
from .models import Question


def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    ouput = ', '.join([q.question_text for q in last_question_list])
    # return HttpResponse("hello world. You are at the polls index")
    return HttpResponse(ouput)


def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)


def results(request, question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
