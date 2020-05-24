from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("<h1>Products Home</h1>")
    #1st argument is always the "request parm"
    #2nd argument is always the "html template"
    return render(request, "products/product.html")


# Create your views here.
