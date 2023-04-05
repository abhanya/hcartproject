from django.shortcuts import render,redirect
from . models import Customer,Seller
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse


# Create your views here.
def catg(request):
    return render(request,'pages/category.html')
def cart_login(request):
    msg = ''
    if request.method == 'POST':
        cmail = request.POST['cusmail']
        cpas = request.POST['cstpass']

        try:
            customer = Customer.objects.get(customer_email = cmail, cust_pass = cpas)
            request.session['customer'] = customer.id
            return redirect('customer:customerhome')
        except:
            msg ='Incorrect Username or password !'
    return render(request,'pages/clogin.html',{'msg':msg})
    
def cart_password(request):
    return render(request,'pages/password.html')

def cust_home(request):
    msg = ''
    if request.method == 'POST':
        cphon = request.POST['cpho']
        try:
            customer = Customer.objects.get(cust_phone = cphon)
            request.session['customer'] = customer.id
            return redirect('customer:cart')
        except:
            msg ='sign up now !'

    return render(request,'pages/custhome.html',{'msg':msg})

def cust_signup(request):
    msg = ""
    if request.method == 'POST':
        csname = request.POST['cust_name']
        addr = request.POST['cust_add']
        gend = request.POST['gen']
        phn = request.POST['cust_ph']
        cmail = request.POST['cust_em']
        cpassw = request.POST['cust_passwrd']

        new_customer = Customer(customer_name = csname ,address = addr , customer_email = cmail , gender = gend
         , cust_phone = phn , cust_pass = cpassw)

        new_customer.save()
        msg = "thank you for signuping !"
        return redirect('hcart:clogin')

    return render(request,'pages/cust_signup.html',{'msg':msg})

def card_signup(request):
    return render(request,'pages/signupcard.html')

def signup(request):
    msg = ""
    if request.method == 'POST':
        sell_name = request.POST['s_name']
        sell_add = request.POST['s_add']
        sell_gen = request.POST['gender']
        sell_pho = request.POST['s_ph']
        com_name = request.POST['c_name']
        acc_holdr = request.POST['acc_h']
        ifsc = request.POST['ifsc']
        brnch = request.POST['branch']
        acc_numb = request.POST['acc_n']
        s_email = request.POST['email']
        # s_username = random.randint(1111,9999)
        # seller_pass = 'sel-' + sell_name.lower() + str(s_username)
        sellerimg = request.FILES['sellimg']


        new_seller = Seller(seller_name = sell_name, seller_add = sell_add, seller_gen = sell_gen,
                    seller_pho = sell_pho, comp_name = com_name, acc_hold = acc_holdr, ifsc = ifsc,
                    branch = brnch, acc_num = acc_numb, email = s_email, seller_pic = sellerimg)
        
        new_seller.save()
        msg = 'we have sent mail !'

    return render(request,'pages/s_signup.html',{'msg':msg})

def sellerlog(request):
    msg = ""
    if request.method == 'POST':
        susername = request.POST['susrname']
        spassword = request.POST['spassw']
        try:
            seller =Seller.objects.get(seller_usr = susername, seller_pass = spassword,approved = True)
            request.session['seller'] = seller.id
            return redirect('seller:sellerhome')
        except:
            msg = 'incorrect username or password'
    return render(request,'pages/slogin.html',{'msg':msg})

def email_exist(request):
    email = request.POST['email']   

    status = Customer.objects.filter(customer_email = email).exists()

    return JsonResponse({'status':status})