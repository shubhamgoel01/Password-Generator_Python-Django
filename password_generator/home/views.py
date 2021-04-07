from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'home/index.html',{'password': 'shubham'})

def password(request): 
    character = list('abcdefghijklmnopqrstuvwxyz')
    length = 10         
    thepassword = ''  
    length = int(request.GET.get('length',12))    
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        character.extend(list('0123456789'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*'))

    length = int(request.GET.get('length',12))    
    for x in range(length):
        thepassword += random.choice(character)
    return render(request,'home/password.html',{'password':thepassword})