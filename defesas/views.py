
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import CadastroUsuarioForm


def cadastro(request):
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("index")
    else:
        form = CadastroUsuarioForm()

    return render(
        request,
        "defesas/cadastro.html",
        {"form": form}
    )


@login_required
def index(request):
    return render(request, "defesas/index.html")
