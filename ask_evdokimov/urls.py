from django.urls import path
from ask_evdokimov import views

urlpatterns = [
    path('', views.index, name="index"),
    path('1', views.question, name="question")
]
