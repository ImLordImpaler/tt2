from django.urls import path
from .views import *
urlpatterns = [
    path('', articleList, name="articleList" ),
    path('article/<str:pk>', article , name='article'),
    path('newComment/<str:pk>' , newComment, name='newComment')
]