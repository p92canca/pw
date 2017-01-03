from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the videos index.")
    
def mostrarPrincipal(request):
    r=models.Video.objects.all().filter(privacidad_video=False)
    return render(request,'mostrarResultados.html',{'titulo':"Pagina principal", 'resultados':r})

