from django.db import models
import pymysql
from django.conf import settings


# Create your models here.

# 视频表
class vedios(models.Model):
    vedioname = models.CharField(max_length=50)
    vediotime = models.CharField(max_length=20)
    vedioteacher = models.CharField(max_length=20)
    vediouptime = models.CharField(max_length=30)
    vediocnt = models.FloatField()
    vedioperdes = models.CharField(max_length=300)
    vediolike = models.IntegerField()
    vediohate = models.IntegerField()
    vedioid = models.IntegerField()
    classdousrc = models.CharField(max_length=1000)  # 课程配套工具
    visrc = models.CharField(max_length=500)  # 视频播放地址或者BV号
    ismain = models.IntegerField()
    collection = models.CharField(max_length=100)  # 视频类型，小类
    type = models.CharField(max_length=100)  # 视频类型，大类
    imgsrc = models.CharField(max_length=300)  # 视频封面地址
    teacherimg = models.CharField(max_length=300)  # 老师的图片


# 查询三大类的视频列表
def FindVideoListByType(type):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 选出主页展示的视频，有的视频有合集，合集的首视频的ismain值为1
    sqlToGetVideoList = "SELECT vedioname,vediotime,vediocnt,vediouptime,vedioid,imgsrc,teacherimg FROM vedios \
                           WHERE type = '%s' and  ismain = 1 order by vediocnt desc" % (type)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetVideoList)
        # 获取所有记录列表,以元组来存储
        res = cursor.fetchall()

    except:
        print("查询视频列表失败！")

    # 关闭数据库连接
    cursor.close()
    db.close()

    return res


# 通过id查找用户名
def FindUsernameByID(request):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    username = ''

    # SQL 查询语句
    sqlToGetUsername = "SELECT username FROM auth_user \
                       WHERE id = %s" % (U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetUsername)
        # 获取所有记录列表,以元组来存储
        results = cursor.fetchall()
        for row in results:
            username = row[0]
    except:
        print("查询用户用户名失败！")

    # 关闭数据库连接
    cursor.close()
    db.close()

    return username


# 通过ID查询用户个人简介
def FindPerdesByID(request):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    perdes = ''

    sqlToGetPerdes = "SELECT perdes FROM now_user \
                   WHERE UID = %s" % (U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetPerdes)
        # 获取所有记录列表,以元组来存储
        nowuser = cursor.fetchall()
        for row in nowuser:
            perdes = row[0]

    except:
        print("错误：没有查找到数据")

    # 关闭数据库连接
    cursor.close()
    db.close()

    return perdes


# 根据id查询视频信息
def FindVideoDataByID(vid):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sqlToGetVideoData = "SELECT vedioname,vedioteacher,vediouptime,\
         vediocnt,vedioperdes,vediolike,vediohate,classdousrc,visrc,teacherimg,collection,imgsrc\
         FROM vedios \
                   WHERE vedioid = %s" % (vid)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetVideoData)
        # 获取所有记录列表,以元组来存储
        res = cursor.fetchall()
    except:
        print("查询视频信息失败！")

    # 关闭数据库连接
    cursor.close()
    db.close()

    return res


# 更新观看次数
def UpdateVideoCnt(vid):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 更新观看次数
    sqlAddVideoCnt = "UPDATE vedios SET vediocnt = vediocnt + 0.5 WHERE vedioid = %s" % (vid)
    try:
        # 执行SQL语句
        cursor.execute(sqlAddVideoCnt)
        # 提交到数据库执行
        db.commit()
    except:
        print("观看次数更新失败！")

    # 关闭数据库连接
    cursor.close()
    db.close()


# 获取视频的相近视频列表
def FindVideoCollection(vedioCollection):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sqlToGetCollection = "SELECT vedioname,vedioteacher,vediouptime,\
             imgsrc,vediotime,vedioid FROM vedios WHERE collection = '%s'" % (vedioCollection)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetCollection)
        # 获取所有记录列表,以元组来存储
        vediores = cursor.fetchall()
    except:
        print("查找该视频相近视频列表失败！")

    # 关闭数据库连接
    cursor.close()
    db.close()

    return vediores
