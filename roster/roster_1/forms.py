from .models import Ros
from django.forms import ModelForm, TextInput, Textarea






class RosForm(ModelForm):
    class Meta:
        model = Ros
        fields = ['nazv', 'form', 'r']

        widgets = {'nazv': TextInput(attrs={'class': "form-control", 'placeholder': "название"}),
                   'form': TextInput(attrs={'class': "form-control", 'placeholder': "формат"}),
                   'r': Textarea(attrs={'class': "form-control", 'placeholder': "ростер", 'cols': "50", 'rows': "13"})}

