# Generated by Django 5.0.3 on 2024-04-23 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='idClient',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
