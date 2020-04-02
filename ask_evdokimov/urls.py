from django.urls import path
from ask_evdokimov import views

urlpatterns = [
    path('', views.index, name="index"),
    path('1', views.question, name="question"),
    path('tag', views.tag, name="tag"),
    path('ask', views.ask_question, name="ask_question")
]
