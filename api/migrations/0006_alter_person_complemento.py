# Generated by Django 5.0.3 on 2025-03-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_person_complemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='complemento',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
