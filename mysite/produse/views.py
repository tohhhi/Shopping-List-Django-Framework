from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Products
from .forms import ProductsForm

# Create your views here.

# products = [
#     {
#         'id':1,
#         'nume':'paine',
#         'cumparat':True
#     },
#     {
#         'id':2,
#         'nume':'oua',
#         'cumparat':False
#     },
#     {
#         'id':3,
#         'nume':'lapte',
#         'cumparat':False
#     }
# ]

def home(requets):
    #return HttpResponse("<h2>Aici va fi lista de produse</h2>")
    if requets.method == "POST":
        form = ProductsForm(requets.POST or None)
        if form.is_valid():
            form.save()
            form = ProductsForm()
            products = Products.objects.all() 
            context = {'form':form, 'products':products}
            return render(requets,'produse/home.html', context)
    else:
        form = ProductsForm()
        products = Products.objects.all()
        context = {'form':form,'products':products}
        return render(requets,'produse/home.html', context)

def delete(requets, id):
    product = Products.objects.get(pk=id)
    product.delete()
    return redirect('home')

def change_status(requets, id):
    product = Products.objects.get(pk=id)
    if product.cumparat:
        product.cumparat = False
        product.save()
    else:
        product.cumparat = True
        product.save()
    return redirect('home')

    


def about(requets):
    #return HttpResponse("<h2>About my app</h2>")
    return render(requets,'produse/about.html')
