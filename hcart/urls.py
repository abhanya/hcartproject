from django.urls import path
from . import views

app_name = 'hcart'
urlpatterns = [
    path('login',views.cart_login,name='clogin'),
    path('cat',views.catg,name='catgry'),
    path('pass',views.cart_password,name='pass'),
    path('',views.cust_home,name='home'),
    path('custsignup',views.cust_signup,name='signup'),
    path('card',views.card_signup,name='card'),
    path('sellersignup',views.signup,name="s_signup"),
    path('sellerlogin',views.sellerlog,name="sellerlog"),
    path('emailexist',views.email_exist,name="emailexist"),
    path('emailexist',views.seller_email_exist,name="selleremailexist"),
    path('bestof',views.bestof,name='bestof'),

]
