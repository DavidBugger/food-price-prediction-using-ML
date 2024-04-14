from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def main_view(request):
    return render(request, "views/main.html",  {"name": "main"})
