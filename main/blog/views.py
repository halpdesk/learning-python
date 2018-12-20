from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# def users(request=<HttpRequest object>, question_id=34):
#     return detail()

def index(request):
    post_list = Post.objects.order_by('-created_at')[:5]
    output = ', '.join([q.title for q in post_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
