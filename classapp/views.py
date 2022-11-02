from django.shortcuts import render,HttpResponse, redirect
from . models import Category,Product
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render (request,'index.html',context)

def products(request):

    product = Product.objects.all()
    context = {
        'product': product
    }
    return render (request,'products.html',context)


def categories(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render (request,'categories.html',context)


def singlecategory(request,id):
    product = Product.objects.filter(category_id =id)
    context = {
        'product':product
    }
    return render (request,'singlecategory.html',context)


def details(request,id):
    details =Product.objects.get(pk=id)
    context = {
        'details': details
    }
    return render(request,'new.html',context)

def shopcart(request):
    if request.method == 'POST':
        quantity = request.POST['quantity']
        phoneid = request.POST['phoneid']
        detail = Product.objects.get(pk=phoneid)
    return redirect('product')


#authentication system


def signin(request):
    if request.method == 'POST':
        name = request.POST['username']
        passw = request.POST['password']
        user = authenticate(username = name,password = passw)
        if user:
            login(request, user)
            messages.success(request, 'signin Successful!')
            return redirect('index')
        else:
            messages.warning(request,'username/password incorrect')
            return redirect('signin')
 
    return render (request,'signin.html')
     #authentication system done

def signup(request):
    return render (request,'signup.html')

def signout(request):
    return redirect('signin')