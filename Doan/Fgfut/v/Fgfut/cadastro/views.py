from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic import TemplateView


def telacadastro(request):
    return HttpResponse('cadastro ')
