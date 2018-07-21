from django.shortcuts import render

def usuario(request, room_name):
    username = None
    if request.user.is_authenticated:
        username=request.user.username

    context = {'username': username}
    return render(request, "usuario.html", context)