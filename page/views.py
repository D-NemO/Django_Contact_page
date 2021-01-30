from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request)
    name = request.POST.get('name','')
    email = request.POST.get('email','')
    message = request.POST.get('message','')
    print(name,email,message)

    return render(request, 'contact.html')