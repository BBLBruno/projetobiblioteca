# Generated by Django 5.1.3 on 2025-02-04 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_livro_editora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.genero', verbose_name='Gênero'),
        ),
    ]
