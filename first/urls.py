from django.urls import path

from .views import new_article, new_comment, all_article

urlpatterns = [
    path('article/', new_article),
    path('comment/', new_comment),
    path('all_article/', all_article),

]