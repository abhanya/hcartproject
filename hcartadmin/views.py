from django.shortcuts import render,redirect
from hcart.models import Customer,Seller
from seller.models import Product
from customer.models import Oreder,Order_item
import random
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count



# Create your views here.

def adhome(request):
    customers = Customer.objects.all()
    cust_count = customers.count()
    product_list = Product.objects.all()
    prod_count = product_list.count()
    sellers = Seller.objects.all()
    sell_count = sellers.count()
    orders = Oreder.objects.all()
    order_count =orders.count()
    order_list = Order_item.objects.order_by('-id')[:6]

    # top_selling_products = Order_item.objects.values('product_id').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')

    # print(top_selling_products)

    topsellingproduct = Order_item.objects.values('product_id','product__product_name','product__product_image','product__product_price','seller_id','seller__seller_name').annotate(count=Count('product_id')).order_by('-count').values('product__product_name','product__product_image','product__product_price','seller__seller_name')[:3]
    print(topsellingproduct)
    context = {
        'cust_list':customers,
        'sell_list':sellers,
        'prods':product_list,
        'cust_count':cust_count,
        'sell_count':sell_count,
        'prod_count':prod_count,
        'order_count':order_count,
        'order_list':order_list,
        'topselling':topsellingproduct,
    }
    return render(request,'pages/adminhome.html',context)

def approve(request):
    sellers = Seller.objects.filter(approved = False)
    return render(request,'pages/approveseller.html',{'seller_app':sellers})

def viewcust(request):
    customers = Customer.objects.all()
    return render(request,'pages/viewcust.html',{'cust_list':customers})

def viewseller(request):
    sellers = Seller.objects.filter(approved = True)
    return render(request,'pages/viewseller.html',{'seller_list':sellers})

def viewprod(request):
    products = Product.objects.all()
    seller = Seller.objects.all()
    context = {
        'seller_list':seller,
        'prod_list':products,
    }
    return render(request,'pages/viewproduct.html',context)

def sellappr(request,sid):
    seller = Seller.objects.get(id=sid)
    s_username = random.randint(1111,9999)
    seller_pass = 'sel-' + seller.seller_name.lower() + str(s_username)
    
    seller.seller_usr = s_username
    seller.seller_pass = seller_pass

    seller.save()

    message = 'hey ! thank you for joining H-cart family , your username is ' + str(s_username) + ' , and temporary password is ' + seller_pass + '.you can change your username and password from your profile'

    send_mail(
        'login approved',
        message,
        settings.EMAIL_HOST_USER,
        [seller.email,],
    )
    seller.approved = True
    seller.save()
    return redirect('hcartadmin:approve')

def remove_prod(request,pid):
    prod_list = Product.objects.get(id = pid)
    prod_list.delete()
    return redirect('hcartadmin:viewproduct')

def delet_seller(request,sid):
    seller_list = Seller.objects.get(id = sid)
    seller_list.delete()
    return redirect('hcartadmin:approve')

def remove_seller(request,sid):
    seller_list = Seller.objects.get(id = sid)
    seller_list.delete()
    return redirect('hcartadmin:viewseller')

def delet_cust(requst,sid):
    cust_list = Customer.objects.get(id = sid)
    cust_list.delete()
    return redirect('hcartadmin:viewcust')

def master(request):
    return render(request,'pages/adminmaster.html')

def orderlist(request):
    orders = Order_item.objects.all()
    return render(request,'pages/vieworederlist.html',{'order_list':orders})


