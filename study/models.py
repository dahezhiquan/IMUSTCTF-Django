from django.db import models
import pymysql
from django.conf import settings

# Create your models here.

# 面试信息表
class interview(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    uptime = models.CharField(max_length=50)
    sourse = models.CharField(max_length=50) # 题目来源
    type = models.CharField(max_length=50)


# 面试专场表
class interview_chapter(models.Model):
    name = models.CharField(max_length=50)
    uptime = models.CharField(max_length=100)
    interviewerName = models.CharField(max_length=50) # 面试官名称
    interviewerImg = models.CharField(max_length=1000) # 面试官图片地址
    introduce = models.CharField(max_length=255) # 面试官自我介绍
    type = models.CharField(max_length=100)
    lan = models.CharField(max_length=100) # 面试官声音类型

# 面试题目表
class interview_question(models.Model):
    name = models.CharField(max_length=50)
    perfect_time = models.IntegerField() # 建议作答时间
    content = models.CharField(max_length=500) # 题目信息
    project = models.CharField(max_length=50)
    qid = models.IntegerField()


# 查找所有面试大类
def FindAllInterviewList():
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询所有security类型面试题目
    sqlToGetInterviewList = "SELECT id,name,level,detail,uptime,source FROM interview where type = 'security'"
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetInterviewList)
        # 获取所有记录列表,以元组来存储
        securityList = cursor.fetchall()
    except:
        print("查找面试大类信息失败！")

    cursor.close()
    db.close()

    return securityList

# 查找所有面试小类的信息
def FindTypeInterviewList(project):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询所有小合集面试
    sql = "SELECT id,name,uptime FROM interview_chapter where type = '%s' order by uptime desc" % (
        project)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表,以元组来存储
        projectList = cursor.fetchall()
    except:
        print("查找面试小类信息失败！")

    cursor.close()
    db.close()

    return projectList

# 根据ID查找面试官
def FindInterviewChapterByID(id):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询模拟面试官信息
    sqlToGetInterviewChapter = "SELECT interviewerName,interviewerImg,introduce,lan FROM interview_chapter where id = %s" % (id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetInterviewChapter)
        # 获取所有记录列表,以元组来存储
        interviewerList = cursor.fetchall()
    except:
        print("根据ID查找面试官失败！")

    cursor.close()
    db.close()

    return interviewerList

# 查找面试题目内容
def FindQuestion(project,id):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询模拟面试题目信息
    sqlToGetQuestionList = "SELECT id,name,perfect_time,content FROM interview_question where project = '%s' and qid = %s" % (
    project, id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetQuestionList)
        # 获取所有记录列表,以元组来存储
        questionList = cursor.fetchall()
    except:
        print("查询面试题目失败！")

    cursor.close()
    db.close()

    return questionList