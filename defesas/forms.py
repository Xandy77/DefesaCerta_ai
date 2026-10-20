

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Defesa


class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="E-mail"
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

        labels = {
            "username": "Nome de usuário",
        }

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data["email"]

        if commit:
            usuario.save()

        return usuario


class DefesaForm(forms.ModelForm):
    class Meta:
        model = Defesa
        fields = [
            "numero_auto",
            "placa",
            "orgao_autuador",
            "estado",
            "artigo_ctb",
            "data_infracao",
            "descricao_fatos",
        ]

        labels = {
            "numero_auto": "Número do auto de infração",
            "placa": "Placa do veículo",
            "orgao_autuador": "Órgão autuador",
            "estado": "UF",
            "artigo_ctb": "Artigo do CTB",
            "data_infracao": "Data da infração",
            "descricao_fatos": "Descrição dos fatos",
        }

        widgets = {
            "data_infracao": forms.DateInput(
                attrs={"type": "date"}
            ),
            "descricao_fatos": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Descreva o que aconteceu..."
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields.values():
            campo.widget.attrs.update({
                "class": "form-control"
            })

