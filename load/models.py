from django.db import models
import pymysql
from django.conf import settings


class arms(models.Model):
    armsName = models.CharField(max_length=100)
    armsDetail = models.CharField(max_length=255)
    backcolor = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    need_password = models.IntegerField()
    password = models.CharField(max_length=100)
    filesrc = models.CharField(max_length=1000)


# 查找某个类型的军火列表
def FindArmsByType(typePage):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 根据选出所有的工具
    sqlToGetArms = "SELECT armsName,armsDetail,backcolor,icon,need_password,id FROM arms \
                               WHERE type = '%s'" % (typePage)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetArms)
        # 获取所有记录列表,以元组来存储
        res = cursor.fetchall()
        resList = list(map(list, res))

    except:
        print("查询", typePage, "军火内容失败！")

    # 关闭数据库连接
    cursor.close()
    db.close()

    return resList


# 查询某个工具的密码信息
def FindArmsPassword(toolName):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sqlToGetArmsPassword = "SELECT password,type FROM arms where armsName = '%s'" % (toolName)

    # 执行SQL语句
    cursor.execute(sqlToGetArmsPassword)

    # 获取所有记录列表,以元组来存储
    results = cursor.fetchall()

    cursor.close()
    db.close()

    return results


# 查询军火的下载链接
def FindArmsFilesrc(toolName):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    print("model层接收到的待下载的工具名称：" ,toolName)
    sqlToGetFilesrc = "SELECT filesrc FROM arms where armsName = '%s'" % (toolName)

    # 执行SQL语句
    cursor.execute(sqlToGetFilesrc)

    # 获取所有记录列表,以元组来存储
    results = cursor.fetchall()

    print("load-model层文件地址查询数据库返回结果：" , results)

    filesrc = ''

    for row in results:
        filesrc = row[0]

    print("model层文件下载地址:", filesrc)

    cursor.close()
    db.close()

    return filesrc
