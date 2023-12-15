from . import views
from django.urls import path


urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('enter/', views.enter, name='enter'),
    path('not_succes/', views.not_succes, name='not_succes'),
    path('registrate/', views.register, name='register'),
    path('send-confirmation/', views.send_and_verify_code, name='enter_email'),
    path('enter_code/', views.check_confirmation_code, name='enter_code'),
    path('if_not_right_code/', views.not_right_code, name='not_right_code'),
    path('if_code_right/', views.right_code, name='right_code'),
    path('user_cabinet/', views.user_cabinet, name='user_cabinet'),
]