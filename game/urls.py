from django.urls import path
from . import views

urlpatterns = [
    path('bear/', views.bear),  # 小熊游戏
]
