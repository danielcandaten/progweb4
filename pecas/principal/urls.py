from django.urls import path
from . import views

#Associa a função views.index a url 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('fazer_login/', views.fazer_login, name='fazer_login'),
    path('fazer_logout/', views.fazer_logout, name='fazer_logout'),
    path('<int:id>/excluir/', views.excluir, name='excluir'),
    path('novo_produto', views.novo_produto, name='novo_produto'),
]
