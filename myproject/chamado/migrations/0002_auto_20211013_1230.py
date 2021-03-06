# Generated by Django 3.2.7 on 2021-10-13 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chamado', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='tipo',
            name='categoria',
        ),
        migrations.AddField(
            model_name='categoria',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chamado.tipo'),
        ),
        migrations.AddField(
            model_name='tipo',
            name='equipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chamado.equipe'),
        ),
        migrations.RemoveField(
            model_name='equipe',
            name='pessoa',
        ),
        migrations.AddField(
            model_name='equipe',
            name='pessoa',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='procedimentos',
        ),
        migrations.AddField(
            model_name='ticket',
            name='procedimentos',
            field=models.ManyToManyField(to='chamado.Procedimento'),
        ),
    ]
