from django.shortcuts import render
from shopapp.models import catdata,proddb

# Create your views here.

def homepage(req):
    cat = catdata.objects.all()
    return render(req,"home.html",{'cat':cat})

def productpage(req):
    pro = proddb.objects.all()
   
    return render(req,"home product.html",{'pro':pro})

def singleprod(req,proid):
    data = proddb.objects.get(id=proid)
    return render(req,"singleproduct.html",{'data':data})

def filteredpage(req,cat_name):
    data = proddb.objects.filter(catname=cat_name)
    return render(req,"Product_filtered.html",{'data' :data})
