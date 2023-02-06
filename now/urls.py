from django.urls import path
from . import views

app_name = 'now'

urlpatterns = [
    path('loginway/', views.login_way),  # 登录
    path('registerinput/', views.register),  # 注册
    path('login/', views.loginin),  # 登录检验
    path('person/', views.person),  # 个人主页
    path('logout/', views.logoutout),  # 退出登录
    path('setdata/', views.setdata),  # 设置个人信息表单
    path('setdatabase/', views.setdatabase),  # 将表单数据存入数据库
]
