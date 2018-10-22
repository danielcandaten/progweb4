from django.db import models
from django.utils import timezone


class Fornecedor(models.Model):
   usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
   nome_fornecedor = models.CharField(max_length=200) 
   endereco = models.TextField()
   data_cadastro = models.DateTimeField(default=timezone.now)

   def __str__(self):
       return self.nome_fornecedor


class Produto(models.Model):
   usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
   nome_produto = models.CharField(max_length=200) 
   fornecedor = models.ManyToManyField(Fornecedor)
   aplicacao = models.TextField()
   data_cadastro = models.DateTimeField(default=timezone.now)

   def __str__(self):
       return self.nome_produto



