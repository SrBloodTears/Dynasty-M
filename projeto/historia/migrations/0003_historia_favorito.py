# Generated by Django 5.1.1 on 2024-12-04 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia', '0002_remove_historia_personagem_remove_historia_preco_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historia',
            name='favorito',
            field=models.BooleanField(default=False),
        ),
    ]
