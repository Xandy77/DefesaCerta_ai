
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="E-mail"
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        labels = {
            "username": "Nome de usuário",
        }

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data["email"]

        if commit:
            usuario.save()

        return usuario
