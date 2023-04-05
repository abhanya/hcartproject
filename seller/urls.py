from django.urls import path
from . import views

app_name = 'seller'
urlpatterns = [
    path('sellerhome',views.home,name="sellerhome"),
    path('addproduct',views.addpro,name="addproduct"),
    path('catlog',views.catlog,name="catlog"),
    path('sellpassword',views.sellpassword,name="sellpassword"),
    path('uploadstock',views.upload,name="uploadstock"),
    path('getstock', views.get_stock, name='getstock'),
    path('logout', views.s_logout, name='logout'),
    path('sellerprof', views.sellerprof, name='sellerprof'),

]
