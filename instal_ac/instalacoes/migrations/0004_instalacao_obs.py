# Generated by Django 4.0 on 2022-01-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instalacoes', '0003_instalacao_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalacao',
            name='obs',
            field=models.TextField(blank=True, max_length=450, null=True),
        ),
    ]
