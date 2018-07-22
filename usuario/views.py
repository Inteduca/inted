from django.shortcuts import render
from usuario.models import Comentarios
from django.http import Http404

def usuario(request, room_name):
    username = None
    chat_text = None
    score_text = None
    horario_text = None
    observaciones_text = None
    room_name = room_name
    if request.user.is_authenticated:
        username=request.user.username
    if username!=room_name and request.user.is_staff is False:
        raise Http404("No estás identificado como el usuario de esta cuenta")

    if request.method=="GET":
        try:
            score_text = Comentarios.objects.values_list('score_text', flat=True).get(username=room_name)
            chat_text = Comentarios.objects.values_list('chat_text', flat=True).get(username=room_name)
            horario_text = Comentarios.objects.values_list('horario_text', flat=True).get(username=room_name)
            observaciones_text = Comentarios.objects.values_list('observaciones_text', flat=True).get(username=room_name)
        except:
            score_text = "Vaya, parece que ha habido un error. Por favor, háznoslo saber contactando con nosotros por correo o móvil."
            horario_text = "Vaya, parece que ha habido un error. Por favor, háznoslo saber contactando con nosotros por correo o móvil."
            observaciones_text = "Vaya, parece que ha habido un error. Por favor, háznoslo saber contactando con nosotros por correo o móvil."

    context = {'room_name': room_name, 'username': username, 'chat_text':chat_text, 'horario_text':horario_text, 'score_text':score_text, 'observaciones_text':observaciones_text}
    return render(request, "usuario.html", context)