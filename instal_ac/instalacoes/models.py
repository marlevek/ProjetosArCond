from django.db import models

# Create your models here.

class Instalacao(models.Model):
    marca = models.CharField(max_length=25, null=False, blank=False)
    tipo = models.CharField(max_length=200, null=False, blank=False, help_text='exemplo: Hi Wall, Multi Split, Cassete')
    tecnologia = models.CharField(max_length=100, null=False, blank=False, help_text='inverter ou convencional')
    capacidade = models.CharField(max_length=100, null=False, blank=False)
    dist_tubulacao = models.IntegerField(null=False, blank=False, help_text='preecha somente o número de metros')
    fluido = models.CharField(max_length=50, null=False, blank=False)
    cliente = models.CharField(max_length=250, null=False, blank=False, default='cliente')
    valor_instal = models.FloatField(max_length=20, null=False, blank=False)
    obs = models.TextField(max_length=450, null=True, blank=True)

    class Meta:
        ordering = ['marca']
        verbose_name = 'Instalações'

    def __str__(self):
        return self.marca



