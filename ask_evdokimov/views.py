from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request, is_hot=False):
    questions = [{
        'title': 'question' + str(i),
        'id': i,
        'text': '''Ambitioni dedisse scripsisse iudicaretur. Cras mattis iudicium purus sit amet fermentum. Donec 
            sed odio operae, eu vulputate felis rhoncus. Praeterea iter est quasdam res quas ex communi. At nos hinc 
            posthac, sitientis piros Afros. Petierunt uti sibi concilium totius Galliae in diem certam indicere. Cras 
            mattis iudicium purus sit amet fermentum. ''' + str(i),
        'tag': ['tag1', 'tag2']
    } for i in range(0, 20)]

    context = {'questions': questions}
    if is_hot is True:
        context['hot'] = True

    return render(request, 'index.html', context)


def hot(request):
    return index(request, True)


def question(request, question_id):
    return render(request, 'question.html')


def tag(request, tag_name):
    context = {}
    questions = []
    for i in range(1, 5):
        questions.append(
            {'title': 'question' + str(i), 'id': i, 'text': '''mnogo texta lol''', 'tag': ['tag1', 'tag2']})
    context['questions'] = questions
    context['tag'] = tag_name
    return render(request, 'index.html', context)


@login_required
def ask_question(request):
    return render(request, 'ask_question.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')


def user_settings(request):
    return render(request, 'user.html')
