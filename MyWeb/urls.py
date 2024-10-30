

import django
from django.urls import path
from .consumer_view import  *
from .views import *
from .enturpreneur_view import *
from .product_service_view import *
from django.conf.urls.static import static
from django.conf import settings
from .sentiment_views import *
from .context_processors import *
#from .sentiment_views import *




urlpatterns = [
    #index
    path('',index,name= "home"),
    path('longdoo/login',signInView,name="login"),
    path('longdoo/logout',signOutView,name="logout"),
    path('longdoo/createEnturpreneur',signUp_enturpreneur,name="signupEnturpreneur"), #สมัคสมาชิกผู้ประกอบการ
    path('longdoo/createConsumer',signUp_consumer,name="signupConsumer"),#สมัคสมาชิกผู้บริโภค 
    path('category/<slug:category_slug>',index,name="product_by_category"),
    path('type/<slug:type_slug>',index,name="product_by_type"), 
    path('help', help_longdoo ,name = "help"),
    
    #ผู้ประกอบการ
    path('trial_witdraw/<int:trial_id>',trial_witdraw ,name = 'trial_witdraw'), #ยกเลิกการให้ทดลอง E
    path('trial_delete/<int:trial_id>',trial_delete ,name = 'trial_delete'), #ยกเลิกการให้ทดลอง E
    path('myProduct',trial_en ,name = 'trial_en_show'), #ดูรายละเอียดสินค้าของผู้ประกอบการที่ผู้บริโภคลงทะเบียนทดลองแล้ว E
    path('trial_request',request_trial_all ,name = 'trial_status_all'),#รายการทดลองทั้งหมด
    path('Edit/Product',edit_product,name="Edit"),#ปุ่มแก้ไขสินค้า
    path('trial_conf/<int:trial_id>',trial_conf ,name = 'trial_conf'), #ยืนยันการให้ทดลอง E
    path('product_register',Register_product, name='rp'), #ลงทะเบียนสินค้าและบริการ E
    path('sentiment/<int:product_and_service_id>',bord ,name = 'sentiment'), #รายงานเชิงลึก
   
    #ผู้บริโภค
    path('trial_consumer_conf/<int:product_and_service_id>',consumer_conf ,name = 'consumer_conf'), #ผู้บริโภคยืนยันการรับสินค้า
    path('trial_cart',Trial_cart,name= 'trial_show'), #สินค้าที่ผู้บริโภคขอทดลอง C
    path('product/<slug:category_slug>/<slug:product_slug>',productDetail,name='product_detail'), #C ดุรายละเอียดสินค้า
    path('trial/<slug:product_slug>/',Trial,name='trialD'), ##กดลงทะเบียนทดลองใช้ C
    path('trial/<int:product_and_service_id>',Trial,name= 'trial'), #กดลงทะเบียนทดลองใช้ C
    path('review/<int:product_and_service_id>',review ,name = 'review'), #รีวิวสินค้า
    path('search/',Search ,name= 'search'), #ค้นหา C
    path('eng',eng,name = 'eng'),
    path('th',th,name = 'th'),
]

if settings.DEBUG :
    urlpatterns+= static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)