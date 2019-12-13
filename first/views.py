from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
@login_required


def topic(request, topic):
    topic = Topic.objects.get(pk=topic)
    return render(request,
                  'topic.html',
                  {
                      'title': topic.title,
                      'body': topic.body
                  }
                  )

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_topic(request):

    if request.method == 'POST':
        title = request.POST.get('title', 'Default')
        text = request.POST.get('text', 'Default')

        t = Topic(title=title, body=text)
        t.save()
    return HttpResponse('Ok')