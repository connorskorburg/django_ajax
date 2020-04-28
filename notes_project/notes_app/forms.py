from django import forms

class NotesForm(forms.Form):
    content = forms.CharField(max_length=255)