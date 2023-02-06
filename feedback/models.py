from django.db import models
import pymysql
from django.conf import settings


# Create your models here.

class userback(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    age = models.IntegerField
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    data = models.CharField(max_length=500)
    time = models.DateTimeField


# 查找当前用户的用户名
def FindUsernameByID(request):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')
    username = ""

    # 获取ID对应的用户名
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

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
        print("获取用户用户名失败！")

    # 关闭数据库连接
    cursor.close()
    db.close()

    return username


# 表单添加数据到userback表
def insertIntoUserBack(username, name, age, email, phone, data, time):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 插入语句
    sqlToAddFeed = "INSERT INTO userback(username, \
                           name, age, email, phone , data , time) \
                           VALUES ('%s', '%s',  %s,  '%s', '%s','%s','%s')" % \
                   (username, name, age, email, phone, data, time)
    try:
        cursor.execute(sqlToAddFeed)
        # 执行sql语句
        db.commit()
    except:
        print("反馈数据库表单添加数据失败！")

    # 关闭数据库连接
    cursor.close()
    db.close()
