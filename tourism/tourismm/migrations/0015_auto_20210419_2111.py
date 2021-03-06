# Generated by Django 3.0.2 on 2021-04-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourismm', '0014_auto_20210419_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250, null=True)),
                ('Hotel', models.CharField(choices=[('Buddha Airlines', 'Buddha Airlines')], default='pokhara', max_length=100)),
                ('No_Of_People', models.CharField(max_length=100, null=True)),
                ('Check_In_Date', models.DateField(max_length=100, null=True)),
                ('Email', models.EmailField(max_length=100, null=True)),
                ('Number', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='checkindate',
            new_name='Check_In_Date',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='number',
            new_name='Number',
        ),
        migrations.AlterField(
            model_name='book',
            name='Package',
            field=models.CharField(choices=[('HeavenView Hotel', 'HeavenView Hotel'), ('NepStay', 'NepStay')], default='pokhara', max_length=100),
        ),
    ]
