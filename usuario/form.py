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
    nome_cadastro = forms.CharField(
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
    # Não funciona
    # def clean_senha_2(self):
    #     senha_1 = self.cleaned_data.get('senha1')
    #     senha_2 = self.cleaned_data.get('senha2')
    #     if senha_1 and senha_2:
            
    #         print(f'Senha1:{senha_1}\nSenha2:{senha_2}')
            
    #         if senha_1 != senha_2:
    #             raise forms.ValidationError('As senhas não são iguais')
    #         else:
    #             return senha_2
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()

            if " " in nome:
                raise forms.ValidationError("Nome de usuario não permitido")
            else:
                return nome
                  
