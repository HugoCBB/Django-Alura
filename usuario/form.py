from django import forms

class LoginForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label="Nome",
        required=True,
        widget= forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Nome"
            }
        )
    )

    senha = forms.CharField(
        max_length=70,
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Senha"
            }
        )
    )


class CadastroForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label="Nome",
        required=True,
        widget= forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite seu nome completo"
            }
        )
    )

    email = forms.EmailField(
        max_length=100,
        label="Email",
        required=True,
        widget= forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite seu melhor email"
            }
        )
    )

    senha1 = forms.CharField(
        max_length=70,
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha"
            }
        )
    )
    senha2 = forms.CharField(
        max_length=70,
        label="Confirme sua senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha novamente"
            }
        )
    )
     