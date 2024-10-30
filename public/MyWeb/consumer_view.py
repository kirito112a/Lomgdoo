
from django.contrib import auth 
from django.contrib.auth.models import UserManager , User 
from django.contrib.auth import authenticate, login
from django.http import request
from MyWeb.models import consumer ,product_and_service
from django.shortcuts import render, render,get_object_or_404,redirect
from.models import answer, consumer, trial
from django.conf import settings

sume = 0



def Search (request):  
    a = request.GET['title']
    print (a)
    product_search = product_and_service.objects.all().filter(product_and_service_name__icontains  = a)


    return render (request, 'index.html', {'products' :  product_search})




def review (request):
    print("review 1234")
    if request.method == "POST": 
        print('5678')
        data = request.POST.copy()
        question_1 = data.get ('question_1')
        question_2 = data.get ('question_2')
        question_3 = data.get ('question_3')
        question_4 = data.get ('question_4')
        question_5 = data.get ('question_5')
        question_6 = data.get ('question_6')
        question_7 = data.get ('question_7')


        awnser = answer()
        awnser.answer_1 = question_1
        awnser.answer_2 = question_2
        awnser.answer_3 = question_3
        awnser.answer_4 = question_4
        awnser.answer_5 = question_5
        awnser.answer_6 = question_6
        awnser.answer_7 = question_7
        awnser.save()



    return render (request,'Review.html' )



def Trial(request,product_and_service_id):
    if request.method == "GET": 
    
        user_id = request.user.id
        consumer_id = consumer.objects.get(user = user_id)
        print ('consumer_id',consumer_id)

        
        product1 = product_and_service.objects.get(product_and_service_id = product_and_service_id)
        print('product_id',product1 )

        cart_trial = trial.objects.all().filter(product = product1 ,consumer = consumer_id)

        print("cart",cart_trial)
        print("cart",cart_trial)
        print('trial',cart_trial)
        if (cart_trial.count() >0 ) :
           
            return render (request,'en_show.html') 
        else:
            print ('trial')
            print('test 2')
            consumer_id =consumer.objects.get (user= user_id )
            newtrial = trial()  
            newtrial.consumer = consumer_id
            newtrial.product = product1
            newtrial.trial_amoun = 1
            newtrial.save() 
        
        
    return render (request,'en_show.html')
 



def Trial_cart(request):
    print("trial show test")
    user_id = request.user.id
    consumer_id = consumer.objects.get(user = user_id)
    trial1 = trial.objects.all().filter(consumer = consumer_id)
    show = trial1
    return render(request,'trialPage.html',{'trialshow':show})




def SignInV(request):
    if request.method=='POST':
        data = request.POST.copy()
        form=consumer(data)
        if form.is_valid():
            consumer_email=request.POST['consumer_email']
            consumer_password=request.POST['consumer_password']
            user=authenticate(consumer_email=consumer_email,consumer_password=consumer_password)
            print(user)
            print(consumer_email)
            if consumer_email is not None :
                print('login')
                login(request,user)
                return render (request,'Home.html')
            else :
                return render (request,'register_consumer.html')
    else:
        form=consumer()
    return render (request,'SignIn.html')




def Consumer(request):  #แสดงข้อมูลผู้บริโภค
    print("top")
    if request.method == "GET": 
        user = consumer.objects.filter (consumer_password='123456' ).values() 
        print(user)    
    userData ={'email_name': user[0] ['consumer_email'], 'p_name': user[0] ['consumer_password'], 
    'last_name' : "เจอิอิ"}
    return render (request,'consumer.html',userData)


def Consumer(request):  #แสดงข้อมูลผู้บริโภค
    print("top")
    if request.method == "GET": 
        user = consumer.objects.filter (consumer_password='123456' ).values() 
        print(user)    
    userData ={'email_name': user[0] ['consumer_email'], 'p_name': user[0] ['consumer_password'], 
    'last_name' : "เจอิอิ"}
    return render (request,'consumer.html',userData)


def Login(request):
    if request.method == "POST": 
        data = request.POST.copy()
        consumer_email1 = data.get ('consumer_email')
        consumer_password1 = data.get ('consumer_password')
        user = auth.authenticate(consumer_email = consumer_email1 ,consumer_password  =consumer_password1 )
        print(consumer.consumer_email)
        if user is not None:
            auth.login(request,user)
            return render (request,'Home.html')
        else:
            print('ผิด')
            return render (request,'register_consumer.html')
    return render (request,'SignIn.html')