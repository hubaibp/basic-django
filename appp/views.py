from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.


class Home(View):
    def get(self,request):
        return render(request,"index.html")
    
class Register(View):
    def get(self,request):
        return render(request,"register.html")   #load template
    
    def post(self,request):
        n=request.POST.get ("items")  #items in form / name in model/ n in django
        c=request.POST.get("cost")
        Product.objects.create(
            name=n,
            pricr=c
        ) #create query 
          
class ProductList(View):
    def get(self,request):
        x=Product.objects.all() #take all from Product Table
        return render (request,"list.html",{"y":x}) #pass objects in x  to Y so we can use it in list.html    