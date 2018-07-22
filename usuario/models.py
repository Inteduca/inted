from django.db import models

class Comentarios(models.Model):
    score_text = models.TextField(default="¡Vaya! Parece que todavía no tienes un seguimiento. Contacta con tutor y lo tendrás pronto.")
    horario_text = models.TextField(default="¡Vaya! Parece que todavía no tienes un horario. Contacta con tutor y lo tendrás pronto.")
    observaciones_text=models.TextField(default="¡Vaya! Parece que todavía no tienes ninguna observación.")
    chat_text=models.TextField(default="Habla con tu profesor por este chat.")
    username = models.CharField(max_length=30)
