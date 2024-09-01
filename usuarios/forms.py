from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(label='Nome de login', required=True, max_length=100, widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":'Ex: João da Silva'
        }
    ))

    senha=forms.CharField(label='senha', required=True, max_length=50, widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Digite sua senha',
            
        }
    ))
