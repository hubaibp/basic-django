from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.


class Home(View):
    def get(self,request):
        return render(request,"index.html")
    
class Register(View):
    def get(self,request):
        return render(request,"register.html")  
    
    def post(self,request):
        n=request.POST.get ("items")
        c=request.POST.get("cost")
        Product.objects.create(
            name=n,
            pricr=c
        )
        