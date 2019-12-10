from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Topic


def topics(request):

    topics = Topic.objects.all()
    return render(request,
                  'all_topic.html',
                  {
                      'topics': topics,

                  }
                 )


def topic(request, topic):

    topic = Topic.objects.get(pk=topic)
    return render(request,
                  'topic.html',
                  {
                      'title': topic.title,
                      'body': topic.body
                  }
                 )



