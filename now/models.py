from django.db import models
import pymysql
from django.conf import settings

# Create your models here.

# 用户基准信息表
class now_user(models.Model):
    name = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    perdes = models.CharField(max_length=200)
    school = models.CharField(max_length=40)
    major = models.CharField(max_length=40)
    grade = models.CharField(max_length=20)
    header = models.CharField(max_length=100)
    likething = models.CharField(max_length=30)
    UID = models.IntegerField()

# 查询用户的用户名和邮箱
def FindUserInfo(request):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')

    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询语句
    sqlToGetUserInfo = "SELECT username,email FROM auth_user \
                   WHERE id = %s" % (U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetUserInfo)
        # 获取所有记录列表,以元组来存储
        results = cursor.fetchall()

    except:
        print("查找用户用户名及邮箱信息错误！")

    cursor.close()
    db.close()

    return results

# 查询用户基准信息
def FindUserData(request):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')

    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sqlToGetUserData = "SELECT * FROM now_user \
               WHERE UID = %s" % (U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetUserData)
        # 获取所有记录列表,以元组来存储
        nowuser = cursor.fetchall()

    except:
        print("查询用户基准信息错误！")

    cursor.close()
    db.close()

    return nowuser


# 查询用户IMC
def FindImcByID(request):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')

    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 查询用户imc
    imc = 0
    sqlToGetImc = "SELECT imc FROM auth_user WHERE id = %s" % (U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetImc)
        # 获取所有记录列表,以元组来存储
        result = cursor.fetchall()
        for row in result:
            imc = row[0]
    except:
        print("查询用户imc值失败！")

    cursor.close()
    db.close()

    return imc

# 查询用户题目数量数据
def FindUserQuesCnt(request):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')

    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sqlToGetUserQuesCnt = "SELECT acCnt,submitCnt,misccnt,cryptocnt,webcnt,pwncnt,recnt FROM question_user WHERE UID = %s" % (U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetUserQuesCnt)
        # 获取所有记录列表,以元组来存储
        questionData = cursor.fetchall()
    except:
        print("查询用户题目数量失败！")

    cursor.close()
    db.close()

    return questionData

# 更新用户信息
def UpdateUserData(request,name,birthday,phone,address,perdes,school,major,grade,likething):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')

    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 用户是否创建过表单数据,为空则表示用户没有创建过数据信息
    flag = ""

    sqlToGetUserInfo = "SELECT * FROM now_user \
                   WHERE UID = %s" % (U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetUserInfo)
        # 获取所有记录列表,以元组来存储
        results = cursor.fetchall()
        flag = results[0]
    except:
        print("查询userinfo失败！")

    # 用户没有创建过数据，则在表中插入一组UID数据
    if flag == "":
        # SQL 插入语句
        sqlToAddUserData = "INSERT INTO now_user \
                        (name,birthday, phone , address, perdes,school,major,grade,likething,UID) \
                           VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s',%s)" % \
               (name, birthday, phone, address, perdes, school, major, grade, likething, U_id)
        try:
            # 执行sql语句
            cursor.execute(sqlToAddUserData)
            # 提交到数据库执行
            db.commit()
        except:
            print("添加userdata失败！")

    # 用户已经创建过数据表，则进行更新操作
    else:
        # SQL 更新语句
        sqlToUpdateUserData = "UPDATE now_user SET \
                name='%s', birthday='%s', phone='%s', address='%s', perdes='%s', school='%s', major='%s', grade='%s', likething='%s'\
                 WHERE UID = %s" % \
               (name, birthday, phone, address, perdes, school, major, grade, likething, U_id)
        try:
            # 执行SQL语句
            cursor.execute(sqlToUpdateUserData)
            # 提交到数据库执行
            db.commit()
        except:
            print("更新userdata失败！")

    cursor.close()
    db.close()