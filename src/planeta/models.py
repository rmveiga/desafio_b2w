from django.db import models

class Planeta(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    clima = models.CharField(max_length=100, verbose_name='Clima')
    terreno = models.CharField(max_length=100, verbose_name='Terreno')

    class Meta:
        db_table = 'planetas'

    def __str__(self):
        return self.nome
