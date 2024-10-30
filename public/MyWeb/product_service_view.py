from MyWeb.models import product_and_service
from django.shortcuts import render , redirect ,get_object_or_404
from.models import category, product_and_service ,type ,trial
from MyWeb.models import  product_and_service , enturpreneur ,question


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
    
    if user_type == True: ###ผู้ประกอบการ
        user_id = request.user.id
        print ("user_id",user_id)
        en = enturpreneur.objects.get(user = user_id)
        
        print("enturpreneur_id",en)
        product = product_and_service.objects.all().filter(enturpreneur = en)
        print (product)
       


        return render(request,'index.html',{'products':product})
    else: ###ผู้บริโภค

        
        if category_slug!=None:
            category_page=get_object_or_404(category,cetegory_slug=category_slug)
            print (category)
            products = product_and_service.objects.all().filter(cetegory=category_page)

            
            
        elif type_page!=None:
            type_page=get_object_or_404(type,type_slug=type_slug)
            print (type)
            products = product_and_service.objects.all().filter(type_name=type_page)
            


        else :
            products = product_and_service.objects.all()
        return render(request,'index.html',{'products':products,'category':products,'type':products})


def index2(request,type_slug ):
    products=None
    type_slug 
    print("aaaaaaaaaa")
        
        
    if type_slug!=None:
        type_page=get_object_or_404(type,type_slug=type_slug)
        print (type)
        products = product_and_service.objects.all().filter(type_name=type_page)

    else :
        products = product_and_service.objects.all()
    return render(request,'index.html',{'products':products,'type':products})




def productDetail(request,category_slug,product_slug):
    try:
        product= product_and_service.objects.get( cetegory__cetegory_slug = category_slug , product_and_service_slug =product_slug)
        print("aaa")
        print(product)
        print("aaa")
        
    except Exception as e :
          raise e
    return render(request,'product_show.html',{'product':product})

def productDetail2(request,type_slug,product_slug):
    try:
        product= product_and_service.objects.get( type__type_slug = type_slug , product_and_service_slug =product_slug)
        print("aaa")
        print(product)
        print("aaa")
        
    except Exception as e :
          raise e
    return render(request,'product_show.html',{'product':product})


def productDelete(request):
     if request.method == "GET": #ดึงข้อมูล
        delete = product_and_service.objects.filter (product_and_service_id ='สินค้าที่จะลบ' ).delete()
        return render (request,'consumer.html',delete)




def Register_product(request):
    if request.method == "POST": 
        
        data = request.POST.copy()
        user_id = request.user.id
        en_id = enturpreneur.objects.get(user = user_id)

        product_and_service_slug = data.get ('product_and_service_name')
        product_and_service_name  = data.get ('product_and_service_name')
        product_and_service_deail = data.get ('product_and_service_deail')
        product_and_service_image = data .get ('product_and_service_image')
        product_and_service_amount = data.get ('product_and_service_amount')

        question_single = data.get ('question_single')
        question_number = data.get ('question_number')
        question_tf = data.get ('question_single')
        question_multiple = data.get ('question_single')
        question_multiple_1 = data.get ('question_multiple_1')
        question_multiple_2 = data.get ('question_multiple_2')
        question_multiple_3 = data.get ('question_multiple_3')
        question_multiple_4 = data.get ('question_multiple_4')
        question_text = data.get ('question_single')
        cetegory = data.get('cetegory')
        print(cetegory)
        print("aa")
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
        newuproduct.product_and_service_image = product_and_service_image
        newuproduct.product_and_service_amount = product_and_service_amount
        newuproduct.cetegory = category_obj
        newuproduct.type_name=  type_obj


        print("quest",question_tf,question_number)

        newquestion = question()
        newquestion.product_and_service = product_and_service_slug
        newquestion.question_single = question_single
        newquestion.question_number =question_number
        newquestion.question_tf = question_tf
        newquestion.question_multiple = question_multiple
        newquestion.question_text = question_text
        newquestion.question_multiple_1 = question_multiple_1
        newquestion.question_multiple_2 = question_multiple_2
        newquestion.question_multiple_3 = question_multiple_3
        newquestion.question_multiple_4 = question_multiple_4
        
        newquestion.save()
        newuproduct.save()

        






        return render (request,'product_register.html') 
    return render (request,'product_register.html') 



def show_product(request): #แสดงข้อมูลสินค้า
    print("top")
    if request.method == "GET": #ดึงข้อมูล
        select_product = product_and_service.objects.filter (product_or_service='Product' ).values() 
        print(select_product)    
    show_productData1 ={'email_name': select_product[0] ['service_status'], 'p_name': user[0] ['service_deail'], 
    'last_name' : "เจอิอิ"}
  
    return render (request,'consumer.html',show_productData1)



def show_service(request): #แสดงข้อมูลบริการ
    print("top")
    if request.method == "GET": #ดึงข้อมูล
        select_service = product_and_service.objects.filter (product_or_service='Service' ).values() 
        print(select_service)    
    show_productData1 ={'email_name':select_service[0] ['service_status'], 'p_name': user[0] ['service_deail'], 
    'last_name' : "เจอิอิ"}
    return render (request,'consumer.html',show_productData1)

def show_product_and_service1(request): #แสดงข้อมูลที่เป็นทั้งสินค้าด้วยบริการด้วย
    print("top")
    if request.method == "GET": #ดึงข้อมูล
        select_product_service = product_and_service.objects.filter (product_or_service='Product and service'  ).values() 
        print(select_product_service)    
    show_product_serviceData1 ={'email_name': select_product_service[0] ['service_status'], 'p_name': user[0] ['service_deail'], 
    'last_name' : "เจอิอิ"}
    return render (request,'consumer.html',show_product_serviceData1)

def show_all(request): #แสดงข้อมูลสินค้าและบริการทั้งหมด
    print("top")
    if request.method == "GET": #ดึงข้อมูล
        select_product_service = product_and_service.objects.filter (product_or_service='*' ).values() 
        print(select_product_service)    
    show_productData1 ={'email_name': select_product_service[0] ['service_status'], 'p_name': user[0] ['service_deail'], 
    'last_name' : "เจอิอิ"}
    return render (request,'consumer.html',show_productData1)



def Register_product1(request):
    return render (request,'ProductRegister.html') 