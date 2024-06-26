# Generated by Django 5.0.2 on 2024-04-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_rename_descricao_acessorio_nome_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="acessorio",
            old_name="nome",
            new_name="descricao",
        ),
        migrations.RenameField(
            model_name="categoria",
            old_name="nome",
            new_name="descricao",
        ),
        migrations.AddField(
            model_name="marca",
            name="nacionalidade",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="marca",
            name="nome",
            field=models.CharField(max_length=50),
        ),
    ]
