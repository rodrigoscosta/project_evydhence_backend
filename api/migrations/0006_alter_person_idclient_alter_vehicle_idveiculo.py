# Generated by Django 5.0.3 on 2024-05-01 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_person_idclient_alter_person_rg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='idClient',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='idVeiculo',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
