from django.urls import path
from . import views

urlpatterns = [
    path('interview/',views.interview), # 模拟面试
    path('call/',views.call), # 模拟面试童话页面
    path('callapi/',views.callapi), # 语音api
    path('git/',views.git), # Git学习
]
