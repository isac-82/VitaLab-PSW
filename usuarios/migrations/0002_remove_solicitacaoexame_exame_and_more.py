# Generated by Django 4.2.5 on 2023-10-04 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitacaoexame',
            name='exame',
        ),
        migrations.RemoveField(
            model_name='solicitacaoexame',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='PedidosExames',
        ),
        migrations.DeleteModel(
            name='SolicitacaoExame',
        ),
        migrations.DeleteModel(
            name='TiposExames',
        ),
    ]
