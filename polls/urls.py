from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # ex: /polls/
    path('<int:question_id>/',views.detail,name="detail"), # ex: /polls/1/
    path('<int:question_id>/results',views.results,name="results"), # ex: /polls/1/results
    path('<int:question_id>/vote',views.vote,name="vote"), # ex: /polls/1/results
]
