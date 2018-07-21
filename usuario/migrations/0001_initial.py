# Generated by Django 2.0.6 on 2018-07-20 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('matematicas', models.CharField(default='f', max_length=10)),
                ('fisica', models.CharField(default='f', max_length=10)),
                ('quimica', models.CharField(default='f', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_text', models.TextField(default='¡Vaya! Parece que todavía no tienes un seguimiento. Contacta con tutor y lo tendrás pronto.')),
                ('horario_text', models.TextField(default='¡Vaya! Parece que todavía no tienes un horario. Contacta con tutor y lo tendrás pronto.')),
                ('observaciones_text', models.TextField(default='¡Vaya! Parece que todavía no tienes ninguna observación.')),
                ('username', models.CharField(max_length=30)),
            ],
        ),
    ]
