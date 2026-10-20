
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CadastroUsuarioForm, DefesaForm
from .models import Defesa


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
    defesas = Defesa.objects.filter(
        usuario=request.user
    ).order_by("-data_criacao")

    return render(
        request,
        "defesas/index.html",
        {"defesas": defesas}
    )


@login_required
def criar_defesa(request):
    if request.method == "POST":
        form = DefesaForm(request.POST)

        if form.is_valid():
            defesa = form.save(commit=False)
            defesa.usuario = request.user
            defesa.save()

            messages.success(
                request,
                "Defesa cadastrada com sucesso!"
            )
            return redirect("index")
    else:
        form = DefesaForm()

    return render(
        request,
        "defesas/defesa_form.html",
        {
            "form": form,
            "titulo": "Cadastrar nova defesa",
        }
    )


@login_required
def detalhar_defesa(request, pk):
    defesa = get_object_or_404(
        Defesa,
        pk=pk,
        usuario=request.user
    )

    return render(
        request,
        "defesas/defesa_detalhe.html",
        {"defesa": defesa}
    )


@login_required
def editar_defesa(request, pk):
    defesa = get_object_or_404(
        Defesa,
        pk=pk,
        usuario=request.user
    )

    if request.method == "POST":
        form = DefesaForm(request.POST, instance=defesa)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Defesa atualizada com sucesso!"
            )
            return redirect("index")
    else:
        form = DefesaForm(instance=defesa)

    return render(
        request,
        "defesas/defesa_form.html",
        {
            "form": form,
            "titulo": "Editar defesa",
        }
    )


@login_required
def excluir_defesa(request, pk):
    defesa = get_object_or_404(
        Defesa,
        pk=pk,
        usuario=request.user
    )

    if request.method == "POST":
        defesa.delete()

        messages.success(
            request,
            "Defesa excluída com sucesso!"
        )
        return redirect("index")

    return render(
        request,
        "defesas/defesa_confirmar_exclusao.html",
        {"defesa": defesa}
    )

