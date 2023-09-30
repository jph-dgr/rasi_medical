# Generated by Django 3.2.6 on 2023-09-30 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('edad', models.PositiveIntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contacto_emergencia', models.CharField(max_length=200)),
                ('telefono_emergencia', models.CharField(max_length=15)),
                ('documento', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
