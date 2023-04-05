from django.urls import path
from . import views

app_name = 'hcartadmin'

urlpatterns = [
    path('admin',views.adhome,name='adhome'),
    path('master',views.master,name='master'),
    path('approve',views.approve,name='approve'),
    path('viewcust',views.viewcust,name='viewcust'),
    path('viewseller',views.viewseller,name='viewseller'),
    path('viewprod',views.viewprod,name='viewproduct'),
    path('removeproduct/<int:pid>',views.remove_prod,name='removeproduct'),
    path('sellapprov/<int:sid>',views.sellappr,name="sepprove"),
    path('deletseller/<int:sid>',views.delet_seller,name="dispprove"),
    path('remseller/<int:sid>',views.remove_seller,name="removeseller"),
    path('deletcust/<int:sid>',views.delet_cust,name="delet_cust"),
    path('orderlist',views.orderlist,name="orderlist"),

]
