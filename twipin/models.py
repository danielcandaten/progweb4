from django.db import models
from django.utils import timezone

class Twip(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    texto = models.CharField(max_length=140)
    data_criacao = models.DateTimeField(default=timezone.now)
    #adicionar outros campos relevantes aqui

    def __str__(self):
        return self.texto
    
class Curtida(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    twip = models.ForeignKey('Twip', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.twip) 
    
