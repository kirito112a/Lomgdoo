
from django.contrib.auth.models import User
from django.http import request
from.models import enturpreneur ,consumer ,User, product_and_service ,category, trial
from django.shortcuts import render , redirect ,get_object_or_404
#เชื่อม Data 



def trial_en(request):
    print("trial show test")
    user_id = request.user.id
    en_id = enturpreneur.objects.get(user = user_id)
    product = product_and_service.objects.all().filter(enturpreneur = en_id )
    print(product) 
    
    return render(request,'trialEnPage.html',{'trial_en_show':product})

def reques_trial (request):

    user_id = request.user.id
    en_id = enturpreneur.objects.get(user = user_id)

    product = product_and_service.objects.all().filter(enturpreneur= en_id )

    
    
    for item in product:
        trial_id = trial.objects.all() 
       
    print(trial_id)
    
    return render(request, 'request_trial.html',{'product':product ,'trial_show':trial_id   })
  
     
   #    for item in product:
    ###      
     #   print('aaaaa')  
     #   context = {
     #       'p':p
     #   }
     #   print(p) 
#
  #/ *  '''

   


def show_enturpreneur(request): #แสดงข้อมูลผู้ประกอบการ
    print("top")
    if request.method == "GET": #ดึงข้อมูล
        user = enturpreneur.objects.filter (enturpreneur_email='123456' ).values() 
        print(user)    
    userData ={'email_name': user[0] ['consumer_email'], 'p_name': user[0] ['consumer_password'], 
    'last_name' : "เจอิอิ"}
    return render (request,'consumer.html',userData)


def en_show(request):

    return render (request,'enshow.html')