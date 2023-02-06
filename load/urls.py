from django.urls import path, include
from . import views

urlpatterns = [

    # 自研军火
    path('imusttools/', views.imusttools),  # 自研军火主页
    path('resimusttools/', views.res_imusttools),  # ICP备案信息查询

    # 军火库展示页面
    path('ctftools/', views.ctftools),
    # 权限工具下载页面
    path('toolcheck/', views.toolcheck),
    # 文件下载
    path('upload/', views.upload),

]
