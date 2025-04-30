from django.shortcuts import render
from django.views import View
from .models import produit

class consulterview(View):
    def get(self,request):
        return render(request,'consulter/consulter.html',{'pro':produit.objects.all()})
