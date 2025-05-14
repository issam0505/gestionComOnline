from django.shortcuts import render, redirect
from django.views import View
from .models import sign

# Sign in view
class signview(View):
    def get(self, request):
        return render(request, 'sign/sign.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username or email already exists
        if sign.objects.filter(username=username).exists():
            return render(request, 'sign/sign.html', {'messages': 'Username already exists!'})
        
        if sign.objects.filter(email=email).exists():
            return render(request, 'sign/sign.html', {'messages': 'Email already exists!'})

        # If both are unique, save new user
        new_user = sign(username=username, email=email, password=password)
        new_user.save()
        
        return render(request, 'sign/sign.html', {'message': 'User created successfully!'})

# Login view
class loginview(View):
    def get(self, request):
        return render(request, 'sign/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Try to find user
        user = sign.objects.filter(username=username, password=password).first()

        if user:
            return redirect('consulter')  # Redirect to the consulter page or dashboard
        else:
            return render(request, 'sign/login.html', {'error': 'Invalid username or password!'})
