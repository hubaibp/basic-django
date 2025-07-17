from django.shortcuts import render,redirect
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
        return redirect("list")
          
class ProductList(View):
    def get(self,request):
        x=Product.objects.all() #take all from Product Table
        return render (request,"list.html",{"y":x}) #pass objects in x  to Y so we can use it in list.html
    
class Productview(View):
    def get(self,request,*args,**kwargs):
        d=kwargs.get("id")  #fetch  the  id  from the url on clilkg it
        v=Product.objects.get(id=d) #ORM to get details of that fetched  id from table
        return render(request,"detail.html",{"det":v})
        
class Productdlt(View):
    def get(self,request,*args,**kwargs):
        m=kwargs.get("id")
        n=Product.objects.get(id=m)
        n.delete()
        return redirect("list") #give name in  url for that template page