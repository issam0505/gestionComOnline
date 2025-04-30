from django.shortcuts import render
from django.views import View

class homeview(View):
    def get(self,request):
        return render(request,'commande/home.html',{})
