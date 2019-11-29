from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def new_article(request):

    return HttpResponse("Hello world")


def new_comment(request):

    return HttpResponse("Create comment")


def all_article(request):
    return HttpResponse("all_article")


