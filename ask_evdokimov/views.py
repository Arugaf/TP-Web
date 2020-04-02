from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def question(request):
    return render(request, 'question.html')


def tag(request):
    return render(request, 'tag.html')


def ask_question(request):
    return render(request, 'ask_question.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')
