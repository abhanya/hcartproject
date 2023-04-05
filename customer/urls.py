from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('custhome',views.homepage_master,name='chome'),
    path('home',views.custhom,name='customerhome'),
    path('bestof',views.bestof,name='bestof'),
    path('cart',views.cart,name='cart'),
    path('productdet/<int:pid>',views.pdetails,name='product'),
    path('pass',views.custpass,name='cpass'),
    path('cprof',views.custprof,name='cprofile'),
    path('remove_cart/<int:pid>',views.remove_item,name='remove_cart'),
    path('removewishlist/<int:pid>',views.removefromwishlist,name='removefromwishlist'),
    path('clogout',views.c_logout,name='clogout'),
    path('wishlist',views.whishlist,name='wishlist'),
    path('catg',views.custcat,name='custcatg'),
    path('catg/<str:data>',views.custcat,name='catogry'),
    path('addwish/<int:pid>',views.addtowishlist,name='addtowishlist'),
    path('searchproduct',views.search_prod,name="searchproducts"),
    path('total',views.totalprice,name='totalprice'),
    path('chekout',views.checkout,name='checkout'),
    path('qty',views.quantity,name='quantity'),
    path('orders',views.orderpage,name='order'),

]
