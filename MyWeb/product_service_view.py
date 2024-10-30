from MyWeb.models import product_and_service
from django.shortcuts import render , redirect ,get_object_or_404
from.models import category, consumer, product_and_service ,type ,trial
from MyWeb.models import  product_and_service , enturpreneur ,question
from django.core.files.storage import FileSystemStorage
from django.core.checks import messages
from django.contrib import messages

def trial_show (request,):
  if  request.method == "POST": 
      select = trial.objects.all().filter( product = "IPhoneX")
      product = product_and_service.objects.get(product_and_service_name = select)
      return render(request,'trialPage.html',{'product':product})



def index(request,category_slug=None,type_slug=None ):

    
    user_type = request.user.is_staff
    print (user_type)
    products=None
    category_page=None
    type_page =None
    if request.user.is_authenticated:
        if user_type == True: ###ผู้ประกอบการ
            user_id = request.user.id
            print ("user_id",user_id)
            en = enturpreneur.objects.get(user = user_id)
            
            print("enturpreneur_id",en)
            product = product_and_service.objects.all().filter(enturpreneur = en)
            print (product)
        


            return render(request,'index.html',{'products':product})
        else: ###ผู้บริโภค
            print('aaaaaaaaaaaaa')
            user_id = request.user.id
            c = consumer.objects.get(user = user_id)
            print(c)
            cp =(c.consumer_province)
            cg=(c.consumer_gender)
            print(cp)
            productsaa = product_and_service.objects.all().filter(product_option_province = None)
            if category_slug!=None:
                category_page=get_object_or_404(category,cetegory_slug=category_slug)
                print (category)
               
                products = product_and_service.objects.all().filter(cetegory=category_page,product_option_province = cp ,  product_option_gender =cg)|product_and_service.objects.filter(cetegory=category_page,product_option_province = "None" , product_option_gender =cg)|product_and_service.objects.filter(cetegory=category_page,product_option_province = cp , product_option_gender ="None")|product_and_service.objects.filter(cetegory=category_page,product_option_province = "None" , product_option_gender ="None")
                return render(request,'index.html',{'products':products,'category':products,'type':products,'c':c })
                
                
            elif type_slug!=None:
                type_page=get_object_or_404(type,type_slug=type_slug)
                print (type)
                products = product_and_service.objects.all().filter(type_name=type_page,product_option_province = cp ,  product_option_gender =cg)|product_and_service.objects.filter(type_name=type_page,product_option_province = "None" , product_option_gender =cg)|product_and_service.objects.filter(type_name=type_page,product_option_province = cp , product_option_gender ="None")|product_and_service.objects.filter(type_name=type_page,product_option_province = "None" , product_option_gender ="None")
                return render(request,'index.html',{'products':products,'category':products,'type':products,'c':c })
                


            else :
                products = product_and_service.objects.filter(product_option_province = cp , product_option_gender =cg)|product_and_service.objects.filter(product_option_province = "None" , product_option_gender =cg)|product_and_service.objects.filter(product_option_province = cp , product_option_gender ="None")|product_and_service.objects.filter(product_option_province = "None" , product_option_gender ="None")

                return render(request,'index.html',{'products':products,'category':products,'type':products,'c':c })
    else:
        products = product_and_service.objects.all()
        if category_slug!=None:
                category_page=get_object_or_404(category,cetegory_slug=category_slug)
                print (category)
                products = product_and_service.objects.all().filter(cetegory=category_page )

                
                
        elif type_slug!=None:
            type_page=get_object_or_404(type,type_slug=type_slug)
            print (type)
            products = product_and_service.objects.all().filter(type_name=type_page)
        
    
        return render(request,'index.html',{'products':products,'category':products,'type':products})


def productDetail(request,category_slug,product_slug):
    try:
        product= product_and_service.objects.get( cetegory__cetegory_slug = category_slug , product_and_service_slug =product_slug)
        print ('product is a ',product)
        
    except Exception as e :
          raise e
    return render(request,'product_show.html',{'product':product})







def Register_product(request):
    if request.method == "POST": 
        data = request.POST.copy()
        user_id = request.user.id
        en_id = enturpreneur.objects.get(user = user_id)
        product_and_service_slug = data.get ('product_and_service_name')
        product_and_service_name  = data.get ('product_and_service_name')
        product_and_service_deail = data.get ('product_and_service_deail')
        product_and_service_amount = data.get ('product_and_service_amount')
        product_option_gender = data.get('product_option_gender')
        product_option_province = data.get('product_option_province')

        question_single = data.get ('question_single')
        question_number = data.get ('question_number')
        question_tf = data.get ('question_tf')
        question_multiple = data.get ('question_multiple')
        question_multiple_1 = data.get ('question_multi_1')
        question_multiple_2 = data.get ('question_multi_2')
        question_multiple_3 = data.get ('question_multi_3')
        question_multiple_4 = data.get ('question_multi_4')
        question_text = data.get ('question_text')
        cetegory = data.get('cetegory')
        print(cetegory)
       
        type_name = data.get('type_name')
        print(type_name)
        
        
        type_obj = type.objects.get(type_name = type_name)
        category_obj = category.objects.get(cetegory_name = cetegory)
       
        
       # user = consumer.objects.filter()
       # print(user)
        
        newuproduct = product_and_service()
        newuproduct.enturpreneur = en_id
        newuproduct.product_and_service_slug  = product_and_service_slug
        newuproduct.product_and_service_name  = product_and_service_name 
        newuproduct.product_and_service_deail = product_and_service_deail
        newuproduct.product_and_service_image = request.FILES['product_and_service_image']
        newuproduct.product_and_service_amount = product_and_service_amount
        newuproduct.cetegory = category_obj
        newuproduct.type_name=  type_obj
        newuproduct.product_option_province = product_option_province
        newuproduct.product_option_gender = product_option_gender

        

    
        newuproduct.save()
        

        
        product = product_and_service.objects.get(product_and_service_id = newuproduct.product_and_service_id)
        slug = product_and_service.objects.filter(product_and_service_id = newuproduct.product_and_service_id).update(product_and_service_slug ="slug_"+str(newuproduct.product_and_service_id) )
        
        newquestion = question()
        newquestion.product_and_service =  product 
        newquestion.question_single = question_single
        newquestion.question_number =question_number
        newquestion.question_tf = question_tf
        newquestion.question_multiple = question_multiple
        newquestion.question_text = question_text
        newquestion.question_multi_1 = question_multiple_1
        newquestion.question_multi_2 = question_multiple_2
        newquestion.question_multi_3 = question_multiple_3
        newquestion.question_multi_4 = question_multiple_4
        messager =messages.success(request,'ลงทะเบียนสินค้าและบริการสำเร็จ')
        newquestion.save()
        

        






        return render (request,'product_register.html',{'messager': messager}) 
    return render (request,'product_register.html') 




