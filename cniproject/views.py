"""views to handle errors """
from django.shortcuts import render


def handler404(request, exception):
    """ error handler 404 - page not found """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ error handler 500 - internal server error """    
    return render(request, "errors/500.html", status=500)