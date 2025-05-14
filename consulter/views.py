from django.shortcuts import render
from django.views import View
from .models import produit
import random

class consulterview(View):
    def get(self,request):
        products = list(produit.objects.all())
        produits2 = produit.objects.filter(deals= True , category__name='Vêtements & Mode') 
        random.shuffle(products) 
        return render(request,'consulter/consulter.html',{'pro':products , 'pro2':produits2})
