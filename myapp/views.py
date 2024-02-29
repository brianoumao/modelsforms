from django.shortcuts import render
from myapp.forms import StudentForm


def home(request):
    mimi = StudentForm
    return render(request, 'index.html', {'form': mimi})
