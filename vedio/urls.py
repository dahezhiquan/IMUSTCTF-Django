from django.urls import path
from . import views


urlpatterns = [
    path('vedios/', views.showved),  # 视频主界面
    path('watchlater/', views.watchlater),  # 最近观看
    path('like/', views.like),  # 收藏夹
    path('showtime/', views.showtime),  # 播放页面
    path('music/', views.music),  # 音乐播放器
]
