from django.http import  HttpResponse
from django.shortcuts import redirect, render 
spassword ='aliajmal'
semail='aliajmal173@gmail.com'
def index(request):
    content = 'Fail'
    my_bytes = content.encode('utf-8')
    # return HttpResponse(my_bytes)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email== semail and  password == spassword:
            # request.session['prem'] =prem
            print('\t\t\t\t\t\ttrue')
            prems ={'email':email,'password':password};
            return  render(request,'home.html', prems)
            # return  redirect('/home')
        else:
            return  HttpResponse(my_bytes)
    return  render(request,'index.html')

    
    
    
    
    

def fail(request):

    content = 'Auth Fail'
    my_bytes = content.encode('utf-8')
    return HttpResponse(my_bytes)
def home(request):

    # content = 'About Ali'
    # my_bytes = content.encode('utf-8')
    # return HttpResponse(my_bytes)
    return  render(request,'home.html')