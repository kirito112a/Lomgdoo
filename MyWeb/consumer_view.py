
from django.contrib import auth 
from django.contrib.auth.models import UserManager , User 
from django.contrib.auth import authenticate, login
from django.http import request
from MyWeb.models import consumer ,product_and_service, question
from django.shortcuts import render, render,get_object_or_404,redirect
from.models import answer, consumer, enturpreneur, trial
from django.conf import settings
from django.core.checks import messages
from django.contrib import messages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pythainlp.corpus.common import thai_stopwords
from pythainlp import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import requests
from io import StringIO
thai_stopwords = list(thai_stopwords())


sume = 0



def Search (request):  

    user_type = request.user.is_staff
    if user_type == True: ###ผู้ประกอบการ
        user_id = request.user.id
        en = enturpreneur.objects.get(user = user_id)
        a = request.GET['title']
        product_search = product_and_service.objects.all().filter(product_and_service_name__icontains  = a,enturpreneur = en )



    a = request.GET['title']
    product_search = product_and_service.objects.all().filter(product_and_service_name__icontains  = a)
    


    return render (request, 'index.html', {'products' :  product_search})




def review (request,product_and_service_id):
    
    
   
    
   
    df = pd.read_csv('https://raw.githubusercontent.com/jaypong440/longdoo_sentiment/main/sentiment.csv', sep=',', names=['text', 'sentiment'], header=None)
    print(df)

    top = df['sentiment'].value_counts()
    print(top)
    thai_stopwords
    def text_process(text):
        final = "".join(u for u in text if u not in ("?", ".", ";", ":", "!", '"', "ๆ", "ฯ","answer_7"))
        final = word_tokenize(final)
        final = " ".join(word for word in final)
        final = " ".join(word for word in final.split() 
                        if word.lower not in thai_stopwords)
        return final
    df['text_tokens'] = df['text'].apply(text_process)
    
    X = df[['text_tokens']]
    y = df['sentiment']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
    

    from sklearn.feature_extraction.text import CountVectorizer
    cvec = CountVectorizer(analyzer=lambda x:x.split(' '))
    cvec.fit_transform(X_train['text_tokens'])
    cvec.vocabulary_

    train_bow = cvec.transform(X_train['text_tokens'])
    pd.DataFrame(train_bow.toarray(), columns=cvec.get_feature_names(), index=X_train['text_tokens'])







    user_id = request.user.id
    consumer_id = consumer.objects.get(user = user_id)
    

   
    product = product_and_service.objects.get(product_and_service_id =product_and_service_id)
    
    questions = question.objects.filter(product_and_service = product_and_service_id)
    

   

    if request.method == "POST": 
        trial_id = trial.objects.filter(product = product_and_service_id ,consumer = consumer_id).update(trial_status = 3)
        data = request.POST.copy()
        
        answer_single = data.get ('answer_single')
        answer_tf =data.get('answer_tf')
        answer_text = data.get ('answer_text')
        answer_multiple = data.get ('answer_multiple')
        answer_number = data.get ('answer_number')
        answer_other = data.get ('answer_other')


        awnser = answer()
        awnser.answer_single = answer_single
        awnser.answer_tf = answer_tf
        awnser.answer_number = answer_number
        awnser.answer_multiple = answer_multiple
        awnser.answer_text = answer_text
        awnser.answer_other = answer_other

        awnser.consumer = consumer_id
        
        lr = LogisticRegression()
        lr.fit(train_bow, y_train)
        print('sentiment = ')
        my_text = answer_other
        my_tokens = text_process(my_text)
        my_bow = cvec.transform(pd.Series([my_tokens]))
        my_predictions = lr.predict(my_bow)
        print(my_predictions)
        if my_predictions =='pos' :
            print('111')
            awnser.answer_sentiment = 1
        elif my_predictions =='neg' :
            awnser.answer_sentiment = 2
        awnser.product_and_service= product 
        awnser.save()
        messager = messages.success(request,'รีวิวสำเร็จ')
        return render (request,'index.html',{'messager': messager}) 








    return render (request,'Review.html',{'questions':questions} )



def Trial(request,product_and_service_id):
    if request.method == "GET": 
    
        user_id = request.user.id
        consumer_id = consumer.objects.get(user = user_id)
        print ('consumer_id',consumer_id)

       
        product1 = product_and_service.objects.get(product_and_service_id = product_and_service_id)
        p =product1.enturpreneur
        
    

        cart_trial = trial.objects.all().filter(product = product1 ,consumer = consumer_id)

        print("cart",cart_trial)
        print("cart",cart_trial)
        print('trial',cart_trial)
        if (cart_trial.count() >0 ) :
            messager =messages.info(request,'ลงทะเบียนขอทดลองไม่สำเร็จ')
            return render (request,'index.html',{'messager': messager}) 
        else:
            print ('trial')
            print('test 2')
            product = product_and_service.objects.filter(product_and_service_id = product_and_service_id).update(product_and_service_amount =product1.product_and_service_amount-0.5) 
            consumer_id =consumer.objects.get (user= user_id )
            newtrial = trial()  
            newtrial.trial_status = 1
            newtrial.consumer = consumer_id
            newtrial.product = product1
            newtrial.trial_amoun = 1
            newtrial.enturpreneur = p
            messager =messages.success(request,'ลงทะเบียนขอทดลองสำเร็จ')
            newtrial.save() 
            
        
        
    return render (request,'index.html',{'messager': messager}) 
 


def consumer_conf(request,product_and_service_id):  
    user_id = request.user.id
    consumer_id = consumer.objects.get(user = user_id)
    trial_id = trial.objects.filter(product = product_and_service_id ,consumer = consumer_id).update(trial_status = 2)
    messager =messages.success(request,'ยืนยันสำเร็จ')
    print("message" , messager)
    return render (request,'index.html',{'messager': messager}) 


def Trial_cart(request):
    print("trial show test")
    user_id = request.user.id
    consumer_id = consumer.objects.get(user = user_id)
    trial1 = trial.objects.all().filter(consumer = consumer_id)
    show = trial1
    return render(request,'trialCart.html',{'trialshow':show})




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