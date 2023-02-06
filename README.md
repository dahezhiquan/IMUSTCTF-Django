# 网站概述📕
一款综合性的网络安全实战平台

**本网站采用Python-Django + Mysql + Redis开发，MTV开发模式**

分为模型（Model）、视图（View）和控制（Controller）三个部分：

- 模型（Model）部分包含了应用程序的业务逻辑和业务数据；
- 视图（View）部分封装了应用程序的输出形式，也就是通常所说的页面或者是界面；
- 控制器（Controller）部分负责协调模型和视图，根据用户请求来选择要调用哪个模型来处理业务，以及最终由哪个视图为用户做出应答。

##### 关于静态文件的部署：

[`django.contrib.staticfiles`](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.") 提供了一个便利的管理命令，用于将静态文件收集至独立目录，方便你为它们提供服务。

1.将 [`STATIC_ROOT`](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-STATIC_ROOT) 配置成你喜欢的目录，在这个目录提供服务，例如:

```
STATIC_ROOT = "/var/www/example.com/static/"
```

2.运行 [`collectstatic`](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/staticfiles/#django-admin-collectstatic) 管理命令:

```
$ python manage.py collectstatic
```

这将会把静态目录下的所有文件拷贝至 [`STATIC_ROOT`](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-STATIC_ROOT) 目录。

3.选一个 Web 服务器为这些文件提供服务。 文档 [部署静态文件](https://docs.djangoproject.com/zh-hans/3.2/howto/static-files/deployment/) 介绍了静态文件的常见部署策略。


##### 关于debug模式与发布模式：

**请在项目本地测试时开启测试模式：**

```python
DEBUG = True
```

**请在项目发布上线时开启发布模式：**

```python
DEBUG = False
```

##### 关于数据库的连接

请在使用pymysql进行数据库连接时进行如下配置

```python
# 打开数据库连接
db = pymysql.connect(host="localhost",
user=settings.DATABASES['default']['USER'],
password=settings.DATABASES['default']['PASSWORD'],
database=settings.DATABASES['default']['NAME'])
```

并且在调用数据库资源后务必关闭资源使用，您可以添加如下两行代码关闭数据库连接

```python
cursor.close()
db.close()
```

# 网站定位🙌

**网络安全一体化在线教学平台，支持视频教程，日常娱乐，CTF练习，CTF竞赛，文档阅读等的网络安全学习场景，可支持的漏洞环境复现与测试，每个漏洞环境复现均有贴心的文档教程**

## 代码目录结构🎈

##### 1.app - master

**目前业务：主页，排行榜，练习，帮助**

**模板文件：**

nav.html - 全局头部导航栏、底部备案信息

index.html - 首页

misc.html - misc练习

faq.html - 帮助

flag.html - 提交flag页面

ranking.html - 排行榜

**静态文件：**

assets - 导航栏及主页静态资源

assetsflag - 练习及提交flag静态资源

ranking - 排行榜静态资源

**视图文件：**

addtype.py - 更新用户具体题目数量，更新用户题目列表

judeging.py - 此函数在用户提交题目时更新用户本身的一些信息,比如用户答题数，通过数，答题列表等

##### 2.app - feedback

**目前业务：反馈表单**

**模板文件：**

feedindex.html - 反馈表单

##### 3.app - game

**目前业务：游戏盒子**

**模板文件：**

bear.html - 小熊闯关游戏

##### 4.app - load

**目前业务：军火库，IMUSTCTF自研工具盒子**

**模板文件：**

ctftools.html - 军火库下载页面

imusttools.html - icp备案查询页面，自研工具库主页

toolsnav.html - 自研工具库导航模板

**视图文件：**

icpmethod.py - icp备案查询接口

##### 5.app - now

**目前业务：登录系统，个人主页**

**模板文件：**

setdata.html - 个人信息修改页面

login.html - 登录页面

personindex.html - 用户主页

##### 6.app - respon

**目前业务：IMUSTCTF大事件日历，IMUSTCTF版本日历**

**模板文件：**

imust.html - 大事件日历

version.html - IMUSTCTF版本日历

**静态资源：**

assetstwo - 大事件日历静态资源

##### 7.app - study

**目前业务：IMUSTCTF模拟面试，Git练习小游戏**

**模板文件：**

interview.html - 面试页面

call.html - 模拟面试官页面

git.html - Git练习小游戏

##### 8.app - vedio

**目前业务：每日音乐，IMUSTCTF-Video**

**模板文件：**

music.html - 每日音乐

home.html - 视频中心主页

your-watch-later - 最近观看

your-laked-videos.html - 喜欢的视频

single-video.html - 视频播放页面

## 安装说明❤

**见INSTALL.md**

## Author👵

dahezhiquan 3390205563@qq.com

xiaozhu 241900086@qq.com

后来的Github小伙伴记得加入自己的名字和邮箱哦~~~
