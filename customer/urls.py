from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('custhome',views.homepage_master,name='chome'),
    path('home',views.custhom,name='customerhome'),
    path('cart',views.cart,name='cart'),
    path('shop',views.shop,name='shop'),
    path('productdet/<int:pid>',views.pdetails,name='product'),
    path('pass',views.custpass,name='cpass'),
    path('cprof',views.custprof,name='cprofile'),
    path('remove_cart/<int:pid>',views.remove_item,name='remove_cart'),
    path('removewishlist/<int:pid>',views.removefromwishlist,name='removefromwishlist'),
    path('clogout',views.c_logout,name='clogout'),
    path('wishlist',views.whishlist,name='wishlist'),
    path('catg',views.custcat,name='custcatg'),
    path('crafts',views.craft_page,name='crafts'),
    path('catg/<str:data>',views.custcat,name='catogry'),
    path('addwish',views.addtowishlist,name='addtowishlist'),
    path('addtocart/<int:pid>',views.addtocartfromwishlist,name='addtocart'),
    path('searchproduct',views.search_prod,name="searchproducts"),
    path('total',views.totalprice,name='totalprice'),
    path('chekout',views.checkout,name='checkout'),
    path('placeorder',views.place_order,name='placeorder'),
    path('qty',views.quantity,name='quantity'),
    path('payonline',views.payonline,name='payonline'),
    path('orders',views.orderpage,name='order'),

]
