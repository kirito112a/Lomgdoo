
from django.contrib.auth.models import User
from django.http import request
from.models import  question, trial , answer,product_and_service ,consumer
from django.shortcuts import render , redirect ,get_object_or_404
from datetime import date
birthyear = 1996
birthmonth = 8
birthday = 10

daynow = date.today().strftime('%Y-%m-%d').split('-')
age_y = int(daynow[0])-int(birthyear)
age_m = int(daynow[1])-int(birthmonth)
age_d = int(daynow[2])-int(birthday)



def bord(request,product_and_service_id):



    product = product_and_service.objects.get(product_and_service_id = product_and_service_id)
    print('product.',product)

    
    answer_id = answer.objects.filter(product_and_service = product_and_service_id )
    answer_pos = answer.objects.filter(product_and_service = product_and_service_id,answer_sentiment = 1).values('answer_sentiment').count()
    answer_neg = answer.objects.filter(product_and_service = product_and_service_id,answer_sentiment = 2).values('answer_sentiment').count()
    sentiment = [answer_pos,answer_neg]
    consumer_m = answer.objects.filter(product_and_service = product_and_service_id,consumer__consumer_gender= "Male").count()
    consumer_f = answer.objects.filter(product_and_service = product_and_service_id,consumer__consumer_gender= "Female").count()
    consumer_o = answer.objects.filter(product_and_service = product_and_service_id,consumer__consumer_gender= "Other").count()
    answer_single1 =answer.objects.filter(product_and_service = product_and_service_id , answer_single = 1).count()
    answer_single2 =answer.objects.filter(product_and_service = product_and_service_id , answer_single = 2).count()
    answer_single3 =answer.objects.filter(product_and_service = product_and_service_id , answer_single = 3).count()
    answer_single4 =answer.objects.filter(product_and_service = product_and_service_id , answer_single = 4).count()
    answer_single5=answer.objects.filter(product_and_service = product_and_service_id , answer_single = 5).count()

    answer_dob=list()
    
    print (answer_dob)
    
    question_id = question.objects.filter(product_and_service = product_and_service_id)

    answer_amount = answer.objects.filter(product_and_service = product_and_service_id ).count()
    answer_tf0 = answer.objects.filter(product_and_service = product_and_service_id , answer_tf = 0).count()
    answer_tf1 = answer.objects.filter(product_and_service = product_and_service_id , answer_tf = 1).count()
    
    
    return render(request,'sentiment.html',{'answer1': answer_id,'answer_pos': answer_pos,'sentiment': sentiment,'answer_neg': answer_neg,
    'consumer_m': consumer_m,'consumer_f': consumer_f , "answer_single1":answer_single1,"answer_single2":answer_single2,"answer_single3":answer_single3,
    "answer_single4":answer_single4,"answer_single5":answer_single5,"question":question_id,'consumer_o':consumer_o,'answer_amount':answer_amount, 'answer_tf0':answer_tf0
    , 'answer_tf1':answer_tf1
    
    
    
    
    
    
    })
