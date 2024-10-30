

from django.contrib.auth.models import UserManager , User 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group,User
from django.contrib.auth import login , authenticate,logout

from django.http import request
from MyWeb.models import consumer ,enturpreneur , language
from django.shortcuts import render , redirect
from.models import consumer #เชื่อม Data
from MyWeb.froms import SignUpForm
import stripe
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django import template
from django.contrib.auth.models import Group 
from django.contrib.auth.hashers import make_password
from django.core.checks import messages
register = template.Library()
from .product_service_view import *
from django.contrib import messages
from .product_service_view import *


@register.filter(name='has_group')
def has_group(user, group_name): 
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False



def help_longdoo(request):
    print("top")

    return render(request , "help.html")




def signInView(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else :
                return redirect('signUp')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})


def signOutView(request):
    logout(request)
    return redirect('home')


def eng(request):
    user_id = request.user.id
    if user_id is not None:
     en = language.objects.all().filter(user = user_id).update(language_name = "EN")
    user_type = request.user.is_staff
    print (user_type)
    products=None
    if user_type == True: ###ผู้ประกอบการ
        user_id = request.user.id
        print ("user_id",user_id)
        en = enturpreneur.objects.get(user = user_id)
        print("enturpreneur_id",en)
        product = product_and_service.objects.all().filter(enturpreneur = en)
        print (product)
        return render(request,'index.html',{'products':product})
    else: ###ผู้บริโภค
        c = consumer.objects.get(user = user_id)
        cp =(c.consumer_province)
        cg=(c.consumer_gender)
        products = product_and_service.objects.filter(product_option_province = cp , product_option_gender =cg)|product_and_service.objects.filter(product_option_province = "None" , product_option_gender =cg)|product_and_service.objects.filter(product_option_province = cp , product_option_gender ="None")|product_and_service.objects.filter(product_option_province = "None" , product_option_gender ="None")
        return render(request,'index.html',{'products':products})



def th(request):
    user_id = request.user.id
    if user_id is not None:
     th = language.objects.all().filter(user = user_id).update(language_name = "TH")
    user_type = request.user.is_staff
    print (user_type)
    products=None
    if user_type == True: 
        user_id = request.user.id
        print ("user_id",user_id)
        en = enturpreneur.objects.get(user = user_id)
        print("enturpreneur_id",en)
        product = product_and_service.objects.all().filter(enturpreneur = en)
        print (product)
        return render(request,'index.html',{'products':product})
    else: ###ผู้บริโภค
        c = consumer.objects.get(user = user_id)
        cp =(c.consumer_province)
        cg=(c.consumer_gender)
        products = product_and_service.objects.filter(product_option_province = cp , product_option_gender =cg)|product_and_service.objects.filter(product_option_province = "None" , product_option_gender =cg)|product_and_service.objects.filter(product_option_province = cp , product_option_gender ="None")|product_and_service.objects.filter(product_option_province = "None" , product_option_gender ="None")
        return render(request,'index.html',{'products':products})
    











def signUp_enturpreneur(request): #สมัคสมาชิกผู้ประกอบการ
    if request.method == "POST": 
        data = request.POST.copy()
        bissiness_name = data.get ('bissiness_name')
        enturpreneur_fname = data.get ('enturpreneur_fname')
        enturpreneur_lname = data.get ('enturpreneur_lname')
        enturpreneur_password = data.get('enturpreneur_password')
        enturpreneur_repassword = data.get('enturpreneur_repassword')
        enturpreneur_email = data.get('enturpreneur_email')
        enturpreneur_idcard = data.get('enturpreneur_idcard')
        enturpreneur_address = data.get('enturpreneur_address')
        enturpreneur_province = data.get ('enturpreneur_province')
        enturpreneur_postal = data.get('enturpreneur_postal')
        enturpreneur_phone = data.get('enturpreneur_phone')
        juristic_code = data.get('juristic_code')
        juristic_document = data.get('juristic_document')
        print(enturpreneur_fname, enturpreneur_lname , enturpreneur_email,
        enturpreneur_province,enturpreneur_postal,enturpreneur_phone)
       # user = consumer.objects.filter()
       # print(user)
        
        
        if enturpreneur_password == enturpreneur_repassword:
            make = make_password (enturpreneur_password)
            print(make)
            username =request.POST['enturpreneur_email']
            email =request.POST['enturpreneur_email']
            password =make_password(enturpreneur_password)
            first_name =request.POST['enturpreneur_fname']
            last_name =request.POST['enturpreneur_lname']

            user = User.objects.create(
                username = username ,
                email= email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_staff = True
            )
            user.save()


            newlanguage = language()
            newlanguage.language_name = "TH"
            newlanguage.user = user
            newlanguage.save()


            newenturpreneur = enturpreneur()
            newenturpreneur.enturpreneur_email  = enturpreneur_email
            newenturpreneur.bissiness_name  = bissiness_name
            newenturpreneur.enturpreneur_fname = enturpreneur_fname
            newenturpreneur.enturpreneur_lname = enturpreneur_lname
            
            newenturpreneur.enturpreneur_idcard = enturpreneur_idcard
            newenturpreneur.enturpreneur_province =enturpreneur_province
            newenturpreneur.enturpreneur_postal =enturpreneur_postal
            newenturpreneur.enturpreneur_phone = enturpreneur_phone
            newenturpreneur.enturpreneur_address = enturpreneur_address
            newenturpreneur.juristic_code = juristic_code
            newenturpreneur.juristic_document = juristic_document
            newenturpreneur.user = user
            newenturpreneur.save()
            messager = messages.success(request,'สมัคสมาชิกสำเร็จ')
            return render (request,'register_enturpreneur.html',{'messager': messager}) 
            
        else:
            messager = messages.info(request,'สมัครสมาชิกไม่สำเร็จ โปรดตรวจสอบข้อมูล')
            return render (request,'register_enturpreneur.html',{'messager': messager}) 








    return render (request,'register_enturpreneur.html') 


def signUp_consumer(request):
    if request.method == "POST": 
        data = request.POST.copy()
        data = request.POST.copy()
        consumer_fname = data.get ('consumer_fname')
        consumer_lname = data.get ('consumer_lname')
        consumer_email = data.get ('consumer_email')
        consumer_password = data.get ('consumer_password')
        consumer_reassword = data.get ('consumer_repassword')
        consumer_dob = data.get('consumer_dob')
        consumer_gender = data.get('consumer_gender')
        consumer_address = data.get('consumer_address')
        consumer_province = data.get ('consumer_province')
        consumer_postal = data.get('consumer_postal')
        consumer_phone = data.get('consumer_phone')
        print(consumer_fname, consumer_lname , consumer_email ,consumer_dob ,consumer_gender,
        consumer_province,consumer_postal,consumer_phone)
        #user = consumer.objects.filter()
        #print(user)
        
       
        
        if consumer_password == consumer_reassword:

            make= make_password(consumer_password)
            print(make)

            username =request.POST['consumer_email']
            email =request.POST['consumer_email']
            password =make_password(consumer_password)
            first_name =request.POST['consumer_fname']
            last_name =request.POST['consumer_lname']

            user = User.objects.create(
                username = username ,
                email= email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()



            newlanguage = language()
            newlanguage.language_name = "TH"
            newlanguage.user = user
            newlanguage.save()


            newuconsumer = consumer()
            newuconsumer.consumer_email = consumer_email 
            newuconsumer.consumer_fname = consumer_fname
            newuconsumer.consumer_lname = consumer_lname
            
            newuconsumer.consumer_dob = consumer_dob
            newuconsumer.consumer_gender = consumer_gender
            newuconsumer.consumer_address = consumer_address
            newuconsumer.consumer_province =consumer_province
            newuconsumer.consumer_postal =consumer_postal
            newuconsumer.consumer_phone = consumer_phone
            newuconsumer.user = user
            
            
            messager =messages.success(request,'สมัคสมาชิกสำเร็จ')
            
            newuconsumer.save()
            return render (request,'register_consumer.html',{'messager': messager})
        else:
            print("Nin Non Non Non Non")
            messager =messages.info(request,'สมัครสมาชิกไม่สำเร็จ โปรดตรวจสอบข้อมูล')
            
            return render (request,'register_consumer.html',{'messager': messager}) 



  
    return render (request,'register_consumer.html') 







