from django.shortcuts import render, HttpResponse, redirect
from email import message
from django.contrib import messages #import messages
from pyexpat.errors import messages
from traceback import print_tb
from urllib import request
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from fypapp.models import Blog
from fypapp import models
from .AQI_API import *


AQI_LEVELS=['GOOD','MODERATE','UNHEALTHY FOR SENSITIVE','UNHEALTHY','Very UNHEALTHY','HAZARDOUS']

# Create your views here.
def index(request):
    return render(request, 'fypapp/includes/index.html')

def signup(request):
    return render(request, 'fypapp/includes/signup.html')

def Contact_Us(request):
        if request.method=='POST':
            name = request.POST['name']
            email = request.POST['email']
            number = request.POST.get('number')
            desc = request.POST.get('desc')
            # print(name, email, number, desc)
            ins = models.Contact(name=name, email=email, phone=number, desc=desc)
            ins.save()
            print('The data has been written to the db.')
        return render(request, 'fypapp/includes/contact.html')

def blog(request):
    allposts = models.Blog.objects.all()
    context = {'allposts':allposts}
    return render(request, 'fypapp/includes/blog.html', context)

def singleBlog(request, slug):
    post= models.Blog.objects.filter(slug=slug).first()
    context={"post":post}
    #return render(request, "myapp/includes/blog-details/", context)
    return render(request, "myapp/includes/singleblog.html", context)

def Signup(request):
    if request.method=='POST':
        sfname = request.POST['sfname']
        slname = request.POST['slname']
        susername = request.POST['susername']
        semail = request.POST['semail']
        spassword = request.POST['spassword']
        scpassword = request.POST['scpassword']
 
        #Check for Errors
        # if len(susername) < 4:
        #     messages.error(request,"username must be over 4 characters")
        #     return redirect('index')
       
        #Passwords should match
        if spassword != scpassword:
            messages.error(request, "passwords do not match")
            return redirect("/")
 
        #Create the User
        myuser = User.objects.create_user(susername,semail,spassword)
        myuser.first_name = sfname
        myuser.last_name = slname
        myuser.save()
        return redirect('index')
       
    return render(request, 'fypapp/includes/signup.html')


def Login(request):
   
    if request.method=='POST':
        lusername = request.POST['lusername']
        lpassword = request.POST['lpassword']
 
        user = authenticate(username=lusername,password=lpassword)
        if user is not None:
            login(request, user)
            # messages.success(request, 'Login Successful!') NOT WORKING
            return redirect('/')
        else:
            # messages.error(request, 'Invalidate Credentials, Try Again') NOT WORKING
            return redirect('/')
   
    return HttpResponse("404- Not found")


def Logout(request):
    logout(request)
    # messages.success(request, "Successfully logged out") NOT WORKING
 
    return redirect('/')
 


#Hamza 

def GetWeatherResult(request):
    if request.method == 'POST':
        PostData=request.POST.copy()
        location=PostData['data']
        sat_count,map_count=Satellite_View(location)
        print(sat_count,map_count)
        aqi_1=predict(1,location)
        fday1=str(aqi_1)+"  ("+ AQI_LEVELS[aqi_1]+")"
        aqi_15=predict(15,location)
        fday15=str(aqi_15)+"  ("+ AQI_LEVELS[aqi_15]+")"
        aqi_30=predict(15,location)
        fday30=str(aqi_30)+"  ("+ AQI_LEVELS[aqi_30]+")"
        context={'location':location,'aqi':5,'covered_area':map_count,'sat_covered_area':sat_count,'fday1':fday1,'fday15':fday15,'fday30':fday30}
    return render(request,'fypapp/includes/Result.html',context)