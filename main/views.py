from django.shortcuts import render, redirect
from .models import Contact

#Create your views here
def home(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        return redirect('/')

    return render(request, 'index.html')