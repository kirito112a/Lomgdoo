from django.http.response import HttpResponsePermanentRedirect, HttpResponseRedirect

from django.shortcuts import get_object_or_404, render , redirect
from.models import  product_and_service,trial
from django.db import models
from MyWeb.models import   trial





def cart_list (request):
    if  request.method == "POST": 
        cart_item = request.session.get('cart_item') or []
        for t in cart_item:
            totol_qty = totol_qty +t.get('qty')
            
        request.sesion['cart_qty'] = totol_qty
        return render (request , 'product/Home.html', {
             'cart_item' : cart_item,
         })

def cart_delete(request,product_and_service_id):
    if  request.method == "POST": 
        cart_item = request.session.get('cartitem') or []
        for i in range (len (cart_item)):
            if cart_item [i]['product_and_service_id'] == product_and_service_id :
             del cart_item
             break

        request.session['cart_item'] = cart_item
        return HttpResponseRedirect (reversed('product:cart_list',kwargs = {}))