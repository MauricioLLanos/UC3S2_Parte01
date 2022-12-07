from django.shortcuts import render, HttpResponse

# Create your views here.


def inicio(request):
    msn = """
           
            <p>Bienvenidos</p>
    
    """
    return HttpResponse(msn)


def uc3(request):
    msn = """
           
    """
    return HttpResponse(msn)


def noticia(request):
    msn = """
           
    
    """
    return HttpResponse(msn)
