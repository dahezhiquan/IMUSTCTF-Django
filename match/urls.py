from django.urls import include, path
from master import views as msgviews  # 主页
from feedback import views as back  # 反馈留言板

# url路径配置

urlpatterns = [
    # path('admin/', admin.site.urls),        # 后台管理模块，暂时未使用
    path('', msgviews.homeproc),  # 主页
    path('misc/', msgviews.misc),  # misc练习
    path('subflag/', msgviews.subflag),  # 题目提交flag页面
    path('testflag/', msgviews.textflag),  # 检验flag
    path('faq/', msgviews.faq),  # 帮助
    path('ranking/', msgviews.ranking),  # 排行榜（积分榜）
    path('feedback/', back.feedMain),  # 反馈留言板
    path('getback/', back.getback),  # 将留言存入数据库
    path('now/', include('now.urls')),  # 登录页
    path('study/', include('study.urls')),  # 学习
    path('respon/', include('respon.urls')),  # 公告
    path('video/', include('vedio.urls')),  # 练习,视频
    path('game/', include('game.urls')),  # 游戏
    path('load/', include('load.urls')),  # 军火库
]
