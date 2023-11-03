from django.shortcuts import render,redirect
from shopapp.models import catdata,proddb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.
def indexpage(req):
    return render(req,"index.html")
    

def addcat(req):
    return render(req,"addcategory.html")

def catdb(req):
        if req.method == "POST":
            na =req.POST.get('name')
            des =req.POST.get('des')
            img =req.FILES['img']
            obj = catdata(name=na,description=des,profileimg=img)
            obj.save()
            messages.success(req,"Category Saved Successfully....!")
            return redirect(addcat)
        
def dis(req):
    data = catdata.objects.all()
    return render(req,"display.html",{'data':data})

def edit(req,dataid):
    data=catdata.objects.get(id=dataid)
    return render(req,"edit.html",{'data':data})

def updatecate(req,dataid):
     if req.method == "POST":
            na =req.POST.get('name')
            des =req.POST.get('des')
            try: 
                img =req.FILES['img']
                fs = FileSystemStorage()
                file = fs.save(img.name,img)
            except MultiValueDictKeyError:
                file = catdata.objects.get(id=dataid).profileimg
            catdata.objects.filter(id=dataid).update(name=na,description=des,profileimg=file)
            messages.success(req,"Category Edited Successfully....!")
            return redirect(dis)
     
def delete(req,dataid):
    data = catdata.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"Category Deleted Successfully....!")
    return redirect(dis)

def addpro(req):
    catname = catdata.objects.all()
    return render(req,"product.html",{'catname':catname})


def prodb(req):
     if req.method == "POST":
        na = req.POST.get('cat')
        pna = req.POST.get('pname')
        des = req.POST.get('des')
        pri = req.POST.get('price')
        img =req.FILES['img']
        obj = proddb(catname=na,proname=pna,description=des,price=pri,productimage=img)
        obj.save()
        return redirect(addpro)
     
def disprod(req):
    data = proddb.objects.all()
    return render(req,"display_pro.html",{'data':data})
        

def editprod(req,pro_id):
    category = catdata.objects.all()
    pro = proddb.objects.get(id=pro_id)
    return render(req,"editpro.html",{'category':category, 'pro':pro })

def deletepro(req,dataid):
    data = proddb.objects.filter(id=dataid)
    data.delete()
    return redirect(disprod)

def updateprod(req,dataid):
     if req.method == "POST":
            na = req.POST.get('cat')
            pna = req.POST.get('pname')
            des = req.POST.get('des')
            pri = req.POST.get('price')
            try: 
                img =req.FILES['img']
                fs = FileSystemStorage()
                file = fs.save(img.name,img)
            except MultiValueDictKeyError:
                file = prodb.objects.get(id=dataid).productimage
            proddb.objects.filter(id=dataid).update(catname=na,proname=pna,description=des,price=pri,productimage=file)
            return redirect(disprod)
     
def adminlogin(req):
     return render(req,"AdminLogin.html")   

def admin_Login(request):
     if request.method == "POST":
          un = request.POST.get('x')
          pwd = request.POST.get('y')

          if User.objects.filter(username__contains=un).exists():
                user = authenticate(username=un,password=pwd)
                if user is not None:
                    login(request,user)
                    request.session['username']=un
                    request.session['password']=pwd
                    return redirect(indexpage)
                    
                else:
                   return redirect(adminlogin)
          else:
               return redirect(adminlogin)
          
def admin_logout(request):
     del request.session['username']
     del request.session['password']
     return redirect(adminlogin)



