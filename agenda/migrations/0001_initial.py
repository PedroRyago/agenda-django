# Generated by Django 4.1.1 on 2022-09-11 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_evento', models.DateTimeField(verbose_name='Data do Evento')),
                ('data_criacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'evento',
            },
        ),
    ]
