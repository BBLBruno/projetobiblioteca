# Generated by Django 5.1.3 on 2024-11-12 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_genero_cidade_autor_editora_livro_usuario_emprestimo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='editora',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='genero',
        ),
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='editora',
            options={'verbose_name': 'Editora', 'verbose_name_plural': 'Editoras'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AddField(
            model_name='autor',
            name='cpf',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='autor',
            name='data_nasc',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='autor',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='autor',
            name='telefone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='editora',
            name='cnpj',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='editora',
            name='data_fundacao',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='editora',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='editora',
            name='razao_social',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='editora',
            name='telefone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='autor',
            name='cidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cidade'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='editora',
            name='cidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cidade'),
        ),
        migrations.AlterField(
            model_name='editora',
            name='nome',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='editora',
            name='site',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cidade'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_nasc',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Emprestimo',
        ),
        migrations.DeleteModel(
            name='Livro',
        ),
    ]
