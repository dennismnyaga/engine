from django.urls import path
from . import views



from .views import  MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('products/', views.all_products, name='products'),
    path('prods/', views.all_prods, name='prod'),
    path('check_product_exists/', views.check_product_exists, name='check-product-exists'),
    path('employees/', views.all_emplyees, name='employees'),
    path('cart/', views.all_cart, name='cart'),
    path('colors/', views.all_colors, name='colors'),
    path('materials/', views.all_material, name='material'),
    path('prosize/', views.all_productsize, name='pro-size'),
    path('productnames/', views.all_productsNames, name='pro-names'),
    path('customers/', views.all_customers, name='customer'),
    path('stockprop/', views.all_stock_prop, name='stock-prop'),
    path('works/', views.all_on_work, name='works'),
    path('addcart/', views.create_or_update_cart, name='works'),
    path('updatecart/<str:pk>/', views.update_cart, name='updatecart'),
    path('createproduct/', views.create_product, name='create-product'),
    path('addproduct/', views.add_product, name='add-product'),
    path('addproductpro/', views.add_product_pro, name='add-product-pro'),
    path('createstock/', views.create_stock, name='create-stock'),
    path('createemployee/', views.create_employee, name='create-employee'),
    path('deleteemployee/<str:pk>/', views.delete_employee, name='delete-employee'),
    path('updateemployee/<str:pk>/', views.update_employee, name='update-employee'),
    path('complete/<str:pk>/', views.update_work, name='update-work'),
    path('updateproduct/<str:pk>/', views.update_product, name='update-product'),
    path('updateproductpro/<str:pk>/', views.update_product_pro, name='update-product'),
    path('updateproductproquantity/<str:pk>/', views.update_product_pro_quantity, name='update-product'),
    path('updatestock/<str:pk>/', views.update_stock, name='update-stock'),
    path('reset/<str:pk>/', views.reset_expense, name='update-expense'),
    path('createprogress/', views.create_progress, name='create_progress'),
    path('expenses/', views.all_expenses, name='expenses'),
    path('createexpenses/', views.create_or_update_expenses, name='create-expenses'),
    path('salesanalysis/', views.sales_analysis, name='sales-analysis'),
    path('register/', views.user_registration, name='user-registration'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('deleteeproduct/<str:pk>/', views.delete_product, name='delete-productpro'),
    path('deleteeproductpro/<str:pk>/', views.delete_productpro, name='delete-productpro'),
    path('updateallstocks/<str:pk>/', views.update_all_stock, name='all-stocks-update'),
    path('deleteallstock/<str:pk>/', views.delete_all_stock, name='delete-all-stock'),
    path('deposit/<str:pk>/', views.add_deposit, name='add-deposit'),
    path('cancelorder/<str:pk>/', views.deleteCart, name='delete-cart')
]