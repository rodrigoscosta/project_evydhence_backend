# Generated by Django 5.0.3 on 2025-04-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_person_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='observacao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
