
from django.contrib.auth.models import User
from django.http import request
from.models import enturpreneur ,consumer ,User, product_and_service ,category, trial
from django.shortcuts import render , redirect ,get_object_or_404
#เชื่อม Data 
from django.core.checks import messages
from django.contrib import messages


def trial_conf(request,trial_id):
   
    print(trial_id)
    trial_confirm  = trial.objects.filter(trial_id = trial_id).update(trial_status =4)
    messager =messages.success(request,'ยืนยันสำเร็จ')
    print("message" , messager)
    return render (request,'index.html',{'messager': messager}) 


def trial_witdraw (request,trial_id):
    messager =messages.success(request,'ยกเลิกสำเร็จ')
    
    trial_confirm  = trial.objects.filter(trial_id = trial_id).update(trial_status = 0)
    return render (request,'index.html',{'messager': messager}) 

def trial_delete (request,trial_id):
    messager =messages.success(request,'ลบรายการสำเร็จ')
    print(trial_id)
    trial_confirm  = trial.objects.filter(trial_id = trial_id).delete()
    
    return render (request,'index.html',{'messager': messager}) 


def trial_(request,trial_id):
    messager =messages.success(request,'ลบรายการสำเร็จ')
    print(trial_id)
    trial_confirm  = trial.objects.filter(trial_id = trial_id).update(trial_status = 0)
    return render (request,'index.html',{'messager': messager}) 

def trial_en(request):
    print("trial show test")
    user_id = request.user.id
    en_id = enturpreneur.objects.get(user = user_id)
    product = product_and_service.objects.all().filter(enturpreneur = en_id )
    
    
    return render(request,'trialEnPage.html',{'trial_en_show':product})

def request_trial_all (request):
    if request.method == "GET": 
        user_id = request.user.id
        en_id = enturpreneur.objects.get(user = user_id)
        trial_id = trial.objects.all().filter(enturpreneur= en_id )
        if trial_id is None:
            return render(request, 'request_trial.html')
        return render(request, 'request_trial.html',{'trial_show':trial_id   })
    return render(request, 'request_trial.html')


def request_trial1 (request):

    user_id = request.user.id
    en_id = enturpreneur.objects.get(user = user_id)
    
    product = product_and_service.objects.all().filter(enturpreneur= en_id )

    
    
    for item in product:
        trial_id = trial.objects.all() 
       
    print(trial_id)
    
    return render(request, 'request_trial1.html',{'product':product ,'trial_show':trial_id   })




def request_trial2 (request):

    user_id = request.user.id
    en_id = enturpreneur.objects.get(user = user_id)

    product = product_and_service.objects.all().filter(enturpreneur= en_id )

    
    
    for item in product:
        trial_id = trial.objects.all() 
       
    print(trial_id)
    
    return render(request, 'request_trial2.html',{'product':product ,'trial_show':trial_id   })


def request_trial3 (request):

    user_id = request.user.id
    en_id = enturpreneur.objects.get(user = user_id)

    product = product_and_service.objects.all().filter(enturpreneur= en_id )

    
    
    for item in product:
        trial_id = trial.objects.all() 
       
    print(trial_id)
    
    return render(request, 'request_trial3.html',{'product':product ,'trial_show':trial_id   })


    
def request_trial0 (request):

    user_id = request.user.id
    en_id = enturpreneur.objects.get(user = user_id)

    product = product_and_service.objects.all().filter(enturpreneur= en_id )

    
    
    for item in product:
        trial_id = trial.objects.all() 
       
    print(trial_id)
    
    return render(request, 'request_trial3.html',{'product':product ,'trial_show':trial_id   })



  
     
   #    for item in product:
    ###      
     #   print('aaaaa')  
     #   context = {
     #       'p':p
     #   }
     #   print(p) 
#
  #/ *  '''



def edit_product(request,product_and_service_id):
    print("eiei")
    
    print("aaa")
    print("bbb1")
    data = request.POST.copy()
    product_and_service_id  = data.get ('product_and_service_id ')
    product_and_service_name  = data.get ('product_and_service_name')
    product_and_service_deail = data.get ('product_and_service_deail')
    product_and_service_image = data .get ('product_and_service_image')
    product_and_service_amount = data.get ('product_and_service_amount')
    cetegory = data.get('cetegory')
    type_name = data.get('type_name')
    print(product_and_service_amount)
    print("nnnnn")
    if product_and_service_name is not None:
        product = product_and_service.objects.filter(product_and_service_id = product_and_service_id).update(product_and_service_name = product_and_service_name)
    if product_and_service_deail is not None:
        product = product_and_service.objects.filter(product_and_service_id = product_and_service_id).update(product_and_service_deail = product_and_service_deail)
    if product_and_service_image is not None:
        product = product_and_service.objects.filter(product_and_service_id = product_and_service_id).update(product_and_service_image = product_and_service_image)
    if product_and_service_amount  is not None:
        product = product_and_service.objects.filter(product_and_service_id = product_and_service_id).update(product_and_service_amount =  product_and_service_amount )
    '''if type_name  is not None:
        product = product_and_service.objects.filter(product_and_service_id = product_and_service_id).update(type_name  = type_name)
    if cetegory  is not None:
        product = product_and_service.objects.filter(product_and_service_id = product_and_service_id).update(cetegory_name =cetegory)
    print("aaa")'''
    print (product_and_service_name)
    print (product_and_service_amount)
    product1 = product_and_service(product_and_service_id =product_and_service_id)


    

    
  
    
    
    
    



    return render (request,'edit_product.html')
   


