from django.db import migrations

def create_poderes(apps, schema_editor):
    Poder = apps.get_model("persona", "Poder")
    from persona.consts import OPCOES_PODERES  # Certifique-se de que esse arquivo existe e contém as opções de poderes
    for codigo, descricao in OPCOES_PODERES:
        Poder.objects.get_or_create(codigo=codigo, descricao=descricao)

class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),  # Define que esta migração depende da inicial
    ]

    operations = [
        migrations.RunPython(create_poderes),  # Executa a função para popular a tabela de poderes
    ]
