# Generated by Django 3.0.2 on 2021-04-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourismm', '0006_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desiredplace',
            field=models.CharField(choices=[('pokhara', 'Pokhara'), ('pokhara', 'Pokhara'), ('pokhara', 'Pokhara'), ('pokhara', 'Pokhara')], default='pokhara', max_length=20),
        ),
    ]
