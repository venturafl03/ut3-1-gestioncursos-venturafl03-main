# Generated by Django 5.1.3 on 2024-12-14 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_estudiante_app.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_estudiante_app.estudiante')),
            ],
        ),
    ]
