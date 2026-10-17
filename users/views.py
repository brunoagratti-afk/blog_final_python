from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import RegistroForm


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("lista_posts")

    else:
        form = RegistroForm()

    return render(
        request,
        "users/registro.html",
        {
            "form": form
        }
    )


def cerrar_sesion(request):
    logout(request)
    return redirect("lista_posts")