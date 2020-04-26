from django.shortcuts import render, redirect
from .models import *
# Create your views here.

# RENDER TEMPLATES
def index(request):
    notes = Note.objects.all()
    context = {
        'notes': notes,
    }
    return render(request, 'index.html', context)


# HANDLING POST DATA

# add a note
def add_note(request):
    note = Note.objects.create(content=request.POST['content'])
    return redirect('/')
