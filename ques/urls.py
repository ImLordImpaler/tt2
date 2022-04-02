from django.urls import path
from .views import *
urlpatterns = [
    path('' , index , name='index' ),

    path('questionList' , questionList , name='questionList'),
    path('question/<str:pk>/' , question , name='question')
]