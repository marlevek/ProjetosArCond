# Generated by Django 4.0 on 2022-01-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instalacoes', '0002_alter_instalacao_valor_instal'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalacao',
            name='cliente',
            field=models.CharField(default='cliente', max_length=250),
        ),
    ]