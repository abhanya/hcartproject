from django.shortcuts import render,redirect
from hcart.models import Seller
from . models import Product
from django.http import JsonResponse


# Create your views here.



def home(request):
    msg =""
    seller = Seller.objects.get(id = request.session['seller']) 
    seller_products = Product.objects.filter(seller = request.session['seller'])
    
    if request.method=='POST':
            # seller = Seller.objects.get(id = request.session['seller'])

            seller_name = request.POST['s_name']
            seller_email = request.POST['s_email']
            seller_address = request.POST['s_address']
            seller_phon = request.POST['s_number']
            seller_gender = request.POST['s_gender']
            business_name = request.POST['businame']
            acc_num = request.POST['acc_number']
            ifsc = request.POST['ifsc']
            sellerimg = request.FILES['sellimg']


            seller.seller_name = seller_name
            seller.email = seller_email
            seller.seller_add = seller_address
            seller.seller_pho = seller_phon
            seller.seller_gen = seller_gender
            seller.comp_name = business_name
            seller.acc_num = acc_num
            seller.ifsc = ifsc
            seller.seller_pic = sellerimg

            seller.save()
            msg = 'Profile updated successfully'
    context = {
                'data': seller,
                'product':seller_products,
                'msg':msg
                }

    return render(request,'pages/sellerhome.html',context)

def addpro(request):
    seller_data = Seller.objects.get(id = request.session['seller']) 
    product_data = Product.objects.filter(seller=request.session['seller'])
    seller_products = Product.objects.filter(seller = request.session['seller'])

    msg = ''
    if request.method == 'POST':
        pname = request.POST['pro_name']
        pdesc = request.POST['pro_det']
        pnum = request.POST['pro_num']
        currnt = request.POST['pro_curr']
        prodimg = request.FILES['pro_img']
        proprice = request.POST['pro_price']
        proplace = request.POST['pro_place']
        prodcat = request.POST['prodtcat']


        new_product = Product(product_name = pname, product_details = pdesc, product_number = pnum, current_stock = currnt, 
        product_image = prodimg, product_place = proplace, product_price = proprice, product_category = prodcat,seller_id = request.session['seller'])

        new_product.save()
        msg='product added succesfully'

    context = {'prod_data': product_data,
                'data': seller_data,
                'product':seller_products,
                'msg':msg,
                }

    return render(request,'pages/addprod.html',context)

def catlog(request):
    seller_products = Product.objects.filter(seller = request.session['seller'])
    seller_data = Seller.objects.get(id=request.session['seller'])
    context ={'product':seller_products,
                'data': seller_data,
                }

    return render(request, 'pages/catlog.html',context)

def sellpassword(request):
    msg =''
    seller_data = Seller.objects.get(id=request.session['seller'])
    if request.method == 'POST':
        seller = Seller.objects.get(id = request.session['seller'])

        current_pass = request.POST['current_pass'] 
        new_pass = request.POST['new_pass'] 
        confirm_pass = request.POST['confirm_pass']

        if seller.seller_pass == current_pass:

            if new_pass == confirm_pass:
                 seller.seller_pass = new_pass
                 seller.save()
                 msg = 'Password changed succesfully'

            else:
                msg = 'Password does not match'

        else:
            msg = 'Incorrect Password'
    context =  {'msg':msg,
                'data': seller_data,
                }
    return render(request,'pages/spassword.html',context)

def sellerprof(request):
        msg = ""
        seller_data = Seller.objects.get(id = request.session['seller']) 
        
        
        context = {
        
        }
        return render(request,'pages/sellerprof.html',context)

def s_logout(request):
    del request.session['seller']
    request.session.flush() 
    return redirect('hcart:sellerlog')


def upload(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    product_data =  Product.objects.filter(seller = request.session['seller'])

    if request.method == 'POST':
        new_stock = request.POST['new_stock']
        product_id = request.POST['productid']
        new_price = request.POST['new_price']

        product = Product.objects.get(id=product_id)
        product.current_stock = product.current_stock + int(new_stock)
        product.product_price = new_price

        product.save()

    context = {'prod_data': product_data,
                    'data': seller_data,
                    }
    return render(request,'pages/stockupload.html',context)

def get_stock(request):

    id = request.POST['id']
    product = Product.objects.get(id=id)

    product_name = product.product_name
    current_stock = product.current_stock
    product_price = product.product_price
    product_id = product.id
    return JsonResponse({'pname':product_name,'stock':current_stock,'pro_id':product_id,'p_price':product_price,})

def orders(request):
     return render(request,'pages/orders.html')