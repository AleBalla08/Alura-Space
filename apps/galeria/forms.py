from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels = {
            'descricao':'Descrição',
            'nome':'Nome',
            'data_foto':'Data de publicação',
            'usuario': 'Usuário',
            'legenda':'Legenda',
            'categoria':'Categoria',



        }

        widgets = {
            'nome' : forms.TextInput(attrs={'class' : 'form-control'}),
            'legenda' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'aonde está presente / órgão reponsável / Fotografo'}),
            'categoria' : forms.Select(attrs={'class' : 'form-control'}),
            'descricao' : forms.Textarea(attrs={'class' : 'form-control'}),
            'foto' : forms.FileInput(attrs={'class' : 'form-control'}),
            'data_foto' : forms.DateInput(format = '%d/%m/%Y',
                attrs={'class' : 'form-control', 'type':'date',}),
            'usuario' : forms.Select(attrs={'class' : 'form-control'}),

        }
