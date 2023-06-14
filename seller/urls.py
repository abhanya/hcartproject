from django.urls import path
from . import views

app_name = 'seller'
urlpatterns = [
    path('sellerhome',views.home,name="sellerhome"),
    path('masterpage',views.masterpage,name="master"),
    path('addproduct',views.addpro,name="addproduct"),
    path('catlog',views.catlog,name="catlog"),
    path('sellpassword',views.sellpassword,name="sellpassword"),
    path('uploadstock',views.upload,name="uploadstock"),
    path('getstock', views.get_stock, name='getstock'),
    path('logout', views.s_logout, name='logout'),
    path('sellerprof', views.sellerprof, name='sellerprof'),
    path('orders', views.orders, name='orders'),
    path('deleteproduct/<int:pid>',views.delete_prod,name='deleteproduct'),

    path('orderdetails/<int:customer_id>',views.sellerorderdetails,name='orderdetails'),
    path('delivered/<int:s_id>/<int:o_id>',views.mark_as_delivered,name='delivered'),
]
