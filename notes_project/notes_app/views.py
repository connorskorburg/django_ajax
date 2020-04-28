from django.shortcuts import render, redirect
from .models import *
from .forms import NotesForm
# Create your views here.

# RENDER TEMPLATES
def index(request):
    notes = Note.objects.all()
    notes_form = NotesForm()
    context = {
        'notes': notes,
        'notes_form': notes_form
    }
    return render(request, 'index.html', context)


# HANDLING POST DATA

# add a note
def add_note(request):
    print(request.POST)
    if request.method == "POST":
        bound_form = NotesForm(request.POST)
        if bound_form.is_valid():
            Note.objects.create(content=request.POST['content'])
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'posts_index.html', context)
