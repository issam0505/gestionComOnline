from django.shortcuts import render,redirect
from django.views import View
from .models import sign
# Create your views here.
class signview(View):
    def get(self,request):
        return render(request,'sign/sign.html')
  
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = sign(username=username, email=email, password=password)
        data.save()
        return render(request, 'sign/sign.html', {'message': 'Saved!'})
    
class loginview(View):
        def get(self,request):
            return render(request,'sign/login.html')
        
class loginview(View):
    def get(self, request):
        return render(request, 'sign/login.html')

  
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Vérifier dans DB
        user = sign.objects.filter(username=username, password=password).first()
        
        if user:
            return redirect('consulter')  # Redirection vers la page home
        else:
            return render(request, 'sign/login.html', {'error': 'Invalid username or password!'})