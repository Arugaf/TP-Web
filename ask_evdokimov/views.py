from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# TODO: Нужна ли вьюшка для популярных тегов и лучших юзеров? Как организовать выборку и подстановку ссылок?

def index(request, is_hot=False):
    questions = [{
        'title': 'question' + str(i),
        'id': i,
        'text': '''Lorem ipsum dolor sit amet, consectetur 
               adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim 
               veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
               irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur 
               sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum '''
                + str(i),
        'tags': ['tag1', 'tag2']
    } for i in range(0, 20)]

    context = {'questions': questions}
    if is_hot is True:
        context['hot'] = True

    return render(request, 'index.html', context)


def hot(request):
    return index(request, True)


def question(request, question_id):
    answers = [{
        'id': i,
        'text': '''Lorem ipsum dolor sit amet, consectetur 
               adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim 
               veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
               irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur 
               sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum '''
                + str(i),
    } for i in range(0, 7)]

    context = {'title': 'Question#' + str(question_id),
               'tags': ['tag1', 'tag2', 'tag3'],
               'text': '''Ambitioni dedisse scripsisse iudicaretur. Cras mattis iudicium purus sit amet fermentum. 
               Donec sed odio operae, eu vulputate felis rhoncus. Praeterea iter est quasdam res quas ex communi. At 
               nos hinc posthac, sitientis piros Afros. Petierunt uti sibi concilium totius Galliae in diem certam 
               indicere. Cras mattis iudicium purus sit amet fermentum. Lorem ipsum dolor sit amet, consectetur 
               adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim 
               veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
               irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur 
               sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'''
                       + str(question_id),
               'answers': answers}
    return render(request, 'question.html', context)


def tag(request, tag_name):
    questions = [{
        'title': 'question' + str(i),
        'id': i,
        'text': '''Ambitioni dedisse scripsisse iudicaretur. Cras mattis iudicium purus sit amet fermentum. Donec 
                sed odio operae, eu vulputate felis rhoncus. Praeterea iter est quasdam res quas ex communi. At nos hinc 
                posthac, sitientis piros Afros. Petierunt uti sibi concilium totius Galliae in diem certam indicere. Cras 
                mattis iudicium purus sit amet fermentum. ''' + str(i),
        'tags': ['tag1', 'tag2']
    } for i in range(0, 20)]

    context = {'questions': questions, 'tag': tag_name}
    return render(request, 'index.html', context)


@login_required
def ask_question(request):
    return render(request, 'ask_question.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')


@login_required
def user_settings(request):
    return render(request, 'user.html')
