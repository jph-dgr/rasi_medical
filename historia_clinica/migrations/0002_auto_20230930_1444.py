# Generated by Django 2.1.5 on 2023-09-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia_clinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adenda',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cirugia',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='condicioncronica',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
