from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

def hola(request):

    return render(request, 'hola.html')

def contacta(request):

    return render(request, 'contacta.html')

def funciona(request):

    return render(request, 'funciona.html')