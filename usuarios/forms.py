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

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(label='Nome', required=True, max_length=100, widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":'Ex: João da Silva'
        }
    ))

    email = forms.EmailField(label='Email', required=True, max_length=50, widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ex: joão_silva@gmail.com'
        }
    ))

    senha_1=forms.CharField(label='senha', required=True, max_length=50, widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Digite sua senha',
            
        }
    ))

    senha_2=forms.CharField(label='Confirme sua senha', required=True, max_length=50, widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Digite sua senha novamente'
            
        }
    ))
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if "k" in nome:
                raise forms.ValidationError("Não é possível inserir espaços dentro do campo usuário")
            else:
                return nome
            
   
            
    
