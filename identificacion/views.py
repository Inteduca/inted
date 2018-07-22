from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from usuario.models import Comentarios


def login(request):
    if request.method=='POST':
        username=request.POST.get('name')
        password=request.POST.get('password')
        #try:
        user2=authenticate(request, username=username, password=password)
        if user2 is not None:
            auth_login(request, user2)
            return HttpResponseRedirect('/usuario' + '/' + username)
            #else:
                #raise Http404("ERROR interno")
        #except:
            #raise Http404("ERROR contraseña o usuario")

    return render(request, 'login.html')

def registrar(request):
    if request.method=='POST':
        username=request.POST.get('name')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        if password!=password2:
            Http404("Las contraseñas no coinciden")
        else:
            try:
                user=User.objects.create_user(username=username, password=password, email=email)
            except:
                raise Http404("Nombre cogido")
            try:
                user.save()
            except:
                raise Http404("Error interno")
            try:
                d=Comentarios(username=username)
                d.save()
            except:
                raise Http404("error comentarios")
            try:
                user2=authenticate(request, username=username, password=password)
                if user2 is not None:
                    login(request, user2)
                    return HttpResponseRedirect('/usuario/' + username)
                else:
                    raise Http404
            except:
                raise Http404

    return render(request, 'register.html')