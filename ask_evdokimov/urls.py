from django.urls import path
from ask_evdokimov import views

urlpatterns = [
    path('', views.index, name="index"),
    path('question/<question_id>', views.question, name="question"),
    path('tag/<tag_name>', views.tag, name="tag"),
    path('ask', views.ask_question, name="ask_question"),
    path('login', views.login, name="login"),
    path('reg', views.registration, name="registration"),
    path('user', views.user_settings, name="user"),
    path('hot', views.hot, name="hot")
]
