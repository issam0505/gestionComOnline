from django.shortcuts import render
from django.views import View

class modificationview(View):
    def get(self,request):
        return render(request,'modification/modification.html',{})
