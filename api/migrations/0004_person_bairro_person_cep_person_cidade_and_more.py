# Generated by Django 5.0.3 on 2025-03-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_schedule_horaagendamento_schedule_localagendamento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='bairro',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='cep',
            field=models.CharField(default='', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='cidade',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='complemento',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='estado',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='logradouro',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='numeroResidencia',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='uf',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
