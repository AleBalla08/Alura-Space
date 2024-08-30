from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [('NEBULOSA', 'nebulosa'),
                        ('ESTRELA','estrela'), 
                        ('GALÁXIA','galáxia'),
                        ('PLANETA','planeta')]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=20, choices=OPCOES_CATEGORIA, default= '')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_foto = models.DateTimeField(default = datetime.now, blank=False)

    def __str__(self):
        return f'fotografia [nome = {self.nome}]'

# Create your models here.
