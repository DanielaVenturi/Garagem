# Generated by Django 5.0.2 on 2024-04-01 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_cor"),
    ]

    operations = [
        migrations.RenameField(
            model_name="acessorio",
            old_name="descricao",
            new_name="nome",
        ),
        migrations.RenameField(
            model_name="categoria",
            old_name="descricao",
            new_name="nome",
        ),
        migrations.RenameField(
            model_name="marca",
            old_name="descricao",
            new_name="nome",
        ),
    ]
