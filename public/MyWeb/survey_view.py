from MyWeb.models import product
from django.shortcuts import render , redirect
from.models import product, question_type , survey ,answer_type
from django.db import models
from MyWeb.models import  product ,service, question_type 




def Survey(request):
    if  request.method == "POST": 
        print("bbb1")
        data = request.POST.copy()
        survey_id = request.POST ('survey_id')
        survey_question = request.POST ('survey_question')
        survey_answer = request.POST ('survey_answer')
    
        
        print("bbb2")
       # user = consumer.objects.filter()
       # print(user)
        
        newuser = survey()
        newuser.survey_id   = survey_id 
        newuser.survey_question = survey_question
        newuser.survey_answer= survey_answer
        newuser.save()
        return redirect ('/') 

def Question_type(request):
    if  request.method == "POST": 
        print("bbb1")
        data = request.POST.copy()
        question_id = request.POST ('question_id')
        question_type_text = request.POST ('question_type_single')
        question_type_number = request.POST ('question_type_single')
        question_type_single = request.POST ('question_type_single')
        question_type_multiple = request.POST ('question_type_single')
    
        
        print("bbb2")
       # user = consumer.objects.filter()
       # print(user)
        
        newuser = question_type()
        newuser.question_id  = question_id
        newuser.question_type_text = question_type_text
        newuser.question_type_number  = question_type_number
        newuser.question_type_single = question_type_single
        newuser.question_type_multiple = question_type_multiple


        newuser.save()
        return redirect ('/') 


def Answer_type(request):
    if  request.method == "POST": 
        print("bbb1")
        data = request.POST.copy()
        answer_id = request.POST ('question_id')
        answer_type_text = request.POST ('question_type_single')
        answer_type_number = request.POST ('question_type_single')
        answer_type_single = request.POST ('question_type_single')
        answer_type_multiple = request.POST ('question_type_single')
        
        print("bbb2")
       # user = consumer.objects.filter()
       # print(user)
        
        newuser = answer_type()
        newuser.answer_id  = answer_id
        newuser.answer_type_text = answer_type_text
        newuser.answer_type_number  = answer_type_number
        newuser.answer_type_single = answer_type_single
        newuser.answer_type_multiple = answer_type_multiple

        newuser.save()
        return redirect ('/') 