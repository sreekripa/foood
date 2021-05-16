from . models import sweet
from django import forms

class ModeForm(forms.ModelForm):
    class Meta:
        model = sweet
        fields = ['name','price','desc','img']