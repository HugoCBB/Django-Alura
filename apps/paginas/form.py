from django import forms
from . models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada']

        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'descricao':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'descricao':forms.TextInput(attrs={'class':'form-control'}),
            'foto':forms.FileInput(attrs={'class':'form-control'}),
            'data':forms.DateTimeInput(
                format='%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'}),
            'usuario':forms.Select(attrs={'class':'form-control'}),
        }
