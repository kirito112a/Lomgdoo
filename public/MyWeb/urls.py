

import django
from django.urls import path
from .consumer_view import  Search, Trial ,Trial_cart,review
from .views import signInView ,signOutView ,signUp_consumer ,signUp_enturpreneur
from .enturpreneur_view import *
from .product_service_view import Register_product,  index, index2, productDetail ,productDetail2
from django.conf.urls.static import static
from django.conf import settings
#from .sentiment_views import *




urlpatterns = [
    path('',index,name= "home"),
    path('category/<slug:category_slug>',index,name="product_by_category"), #C
    path('product/<slug:category_slug>/<slug:product_slug>',productDetail,name='product_detail'), #C
    path('type/<slug:type_slug>',index2,name="product_by_type"), #C
    path('product/<slug:type_slug>/<slug:product_slug>',productDetail2, name = 'product_detail'), #C


    
    path('trial/<int:product_and_service_id>',Trial,name= 'trial'), #กดลงทะเบียนทดลองใช้ C
    path('trialshow',Trial_cart,name= 'trial_show'), #สินค้าที่ผู้บริโภคขอทดลอง C
    path('review',review ,name = 'review'), #รีวิว C
    path('longdoo/createConsumer',signUp_consumer,name="signupConsumer"),#สมัคสมาชิกผู้บริโภค 
    path('longdoo/login',signInView,name="login"),
    path('longdoo/logout',signOutView,name="logout"),
    path('longdoo/createEnturpreneur',signUp_enturpreneur,name="signupEnturpreneur"), #สมัคสมาชิกผู้ประกอบการ
    path('en',en_show ,name = 'en'),
    path('Ten',trial_en ,name = 'trial_en_show'), #สินค้าของผู้ประกอบการที่ผู้บริโภคลงทะเบียนทดลองแล้ว E
    path('ReqEn',reques_trial ,name = 'reques_trial'),
   # path('sen',sentimen ,name = 'sen'),

    
    path('rp',Register_product, name='rp'), #ลงทะเบียนสินค้าและบริการ E
    path('search/',Search ,name= 'search'), #ค้นหา C
    



]

if settings.DEBUG :
    urlpatterns+= static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)