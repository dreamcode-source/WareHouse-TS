from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view , name = 'login_view'),
    path('register/', views.register , name = 'register'),
    path('warehouse/admin/', views.admini , name = 'admini'),
    path('warehouse/admin/users/create', views.register_users, name = 'create_user'),
    path('warehouse/admini/customer', views.customer_view, name = 'customer'),
    path('warehouse/admini/sales', views.sales_view, name = 'sales'),
    path('warehouse/admini/shops', views.shop_view, name = 'shops'),
    path('warehouse/admini/expenses', views.expenses_view, name = 'expenses'),
    path('warehouse/admini/customer', views.customer_view, name = 'customer'),
    path('warehouse/admini/supplier', views.supplier_view, name = 'supplier'),
    path('warehouse/admini/warehouse', views.warehouse_view, name = 'warehouse'),
    path('warehouse/admini/goods_master', views.goodmaster_view, name = 'goods_master'),
    path('warehouse/admini/customer', views.customer_view, name = 'customer'),
    path('warehouse/admini/incoming_goods', views.incominggoods_view, name = 'incoming_goods'),
    path('warehouse/admini/outgoing_goods', views.outgoinggoods_view, name = 'outgoing_goods'),
    path('logout/', views.logout_view, name = 'logout'),
]