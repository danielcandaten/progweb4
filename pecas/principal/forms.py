from django import forms
from .models import Fornecedor


#class FormPost(forms.Form):
#   titulo = forms.CharField(label='Seu nome',max_length=200)
#   texto = forms.CharField(widget=forms.Textarea, max_length=1000)

class FormLogin(forms.Form):
   username = forms.CharField(max_length=20)
   password = forms.CharField(widget=forms.PasswordInput, max_length=10)


class FormProduto(forms.Form):
   nome_produto = forms.CharField(max_length=100)
   aplicacao = forms.CharField(max_length=200)
   fornecedor = forms.CharField(max_length=200)##forms.ModelChoiceField(Fornecedor.objects.order_by('nome_fornecedor'))





