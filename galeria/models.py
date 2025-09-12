from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

# Create your models here.
"""
    Representa uma fotografia na galeria.

    Atributos:
        nome (str): O nome da fotografia.
        legenda (str): A legenda da fotografia.
        descricao (str): Uma descrição detalhada da fotografia.
        foto (ImageField): O arquivo de imagem da fotografia.
        categoria (str): A categoria da fotografia (ex: Nebulosa, Estrela).
        publicado (bool): Indica se a fotografia está publicada.
        data_fotografia (datetime): A data em que a fotografia foi tirada.
        usuario (User): O usuário que publicou a fotografia.
"""


class Fotografia(models.Model):
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIA)
    publicado = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )
    
    def __str__(self):
        return self.nome
