from django.shortcuts import render
from usuario.models import Comentarios

def usuario(request, room_name):
    username = None
    score_text = None
    horario_text = None
    observaciones_text = None
    if request.user.is_authenticated:
        username=request.user.username
    room_name=room_name
    if request.method=="GET":
        try:
            score_text = Comentarios.objects.values_list('score_text', flat=True).get(username=username)
            horario_text = Comentarios.objects.values_list('horario_text', flat=True).get(username=username)
            observaciones_text = Comentarios.objects.values_list('observaciones_text', flat=True).get(username=username)
        except:
            score_text = "Vaya, parece que ha habido un error. Por favor, háznoslo saber contactando con nosotros por correo o móvil."
            horario_text = "Vaya, parece que ha habido un error. Por favor, háznoslo saber contactando con nosotros por correo o móvil."
            observaciones_text = "Vaya, parece que ha habido un error. Por favor, háznoslo saber contactando con nosotros por correo o móvil."

    context = {'room_name': room_name, 'username': username, 'horario_text':horario_text, 'score_text':score_text, 'observaciones_text':observaciones_text}
    return render(request, "usuario.html", context)