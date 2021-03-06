# Generated by Django 3.0.2 on 2021-04-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourismm', '0007_auto_20210417_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desiredplace',
            field=models.CharField(choices=[('Fewa Tal', 'Fewa Tal'), ('Begnas Tal', 'Begnas Tal'), ('Devis Fall', 'Devis Fall'), ('Shree Bindhyabasini Temple', 'Shree Bindhyabasini Temple'), ('Mahendra Gufa', 'Mahendra Gufa'), ('Tal Barahi Temple', 'Tal Barahi Temple'), ('Rupa Tal', 'Rupa Tal'), ('International Mountain Museum', 'International Mountain Museum'), ('Pokhara Lake Side', 'Pokhara Lake Side'), ('Gupteshwor Mahadev Cave', 'Gupteshwor Mahadev Cave'), ('Chamero Gufa', 'Chamero Gufa'), ('Gorkha Memorial Museum', 'Gorkha Memorial Museum'), ('World Peace Pagoda', 'World Peace Pagoda'), ('Sarangkot', 'Sarangkot'), ('Canyoning', 'Canyoning'), ('Bungee Jumping', 'Bungee Jumping'), ('Zipline', 'Zipline'), ('Paragliding', 'Paragliding'), ('Ultra Light Flight', 'Ultra Light Flight'), ('Boating', 'Boating'), ('Night Life Exploration', 'Night Life Exploration'), ('Local Food Tour', 'Local Food Tour')], default='pokhara', max_length=100),
        ),
    ]
