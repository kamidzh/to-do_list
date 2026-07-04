from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def monday(request):
    todo = ['todo1', 'todo2', 'todo3']
    return render(request, 'monday.html', {'todo': todo})


def tuesday(request):
    todo = ['todo1', 'todo2', 'todo3']
    return render(request, 'tuesday.html', {'todo': todo})


def wednesday(request):
    todo = ['todo1', 'todo2', 'todo3']
    return render(request, 'wednesday.html', {'todo': todo})


def thursday(request):
    todo = ['todo1', 'todo2', 'todo3']
    return render(request, 'thursday.html', {'todo': todo})


def friday(request):
    todo = ['todo1', 'todo2', 'todo3']
    return render(request, 'friday.html', {'todo': todo})


def saturday(request):
    todo = ['todo1', 'todo2', 'todo3']
    return render(request, 'saturday.html', {'todo': todo})


def sunday(request):
    todo = ['todo1', 'todo2', 'todo3']
    return render(request, 'sunday.html', {'todo': todo})