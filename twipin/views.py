from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Twip,Curtida
from django.views.decorators.csrf import csrf_exempt

def index(request):
   contexto = {} 
   return render(request, 'twipin/index.html', contexto)

@csrf_exempt
def api_twips_id(request, id):
    if request.method == "DELETE":
      twip = Twip.objects.get(id=id)
      twip.delete()

      jt = {"mensagem": "ok"}
      return JsonResponse(jt)

@csrf_exempt
def api_coracao(request, id):

    c = 0 #número de curtidas

    if request.method == "POST":
      t = Twip.objects.get(id=id)
      u = User.objects.get(username='admin')
      curtida = Curtida(autor=u, twip=t)
      curtida.save()
      c = t.curtida_set.count()
    elif request.method == "DELETE":
      t = Twip.objects.get(id=id)
      u = User.objects.get(username='admin')
      curtida = Curtida.objects.get(autor=u, twip=t)
      curtida.delete()
      c = t.curtida_set.count()

    jt = {"mensagem": "ok", "curtidas": c}
    return JsonResponse(jt)

@csrf_exempt
def api_twips(request):
   if request.method == "GET":
      twips = Twip.objects.all()
      u = User.objects.get(username='admin')

      jt = {"lista":[]} 

      for t in twips:
         curtiu = t.curtida_set.filter(autor_id = u.id).count() > 0
         temp = {"id": t.id, "texto": t.texto, "autor": t.autor.username, "curtidas": t.curtida_set.count(), "curtiu": curtiu}
         jt["lista"].append(temp)   
       
      return JsonResponse(jt)
   elif request.method == "POST":

      #Salva no banco
      t = request.POST["texto"]
      u = User.objects.get(username='admin')
      twip = Twip(autor=u, texto = t)
      twip.save()
      
      jt = {"mensagem": "ok", "id": twip.id, "usuario": u.username}
      return JsonResponse(jt)
 
