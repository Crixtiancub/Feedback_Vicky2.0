# Generated by Django 3.2.3 on 2021-05-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicky', '0003_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntas_vicky',
            name='sugerencia',
            field=models.TextField(default='null', max_length=100),
        ),
    ]
