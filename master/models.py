from django.db import models
import pymysql
from django.conf import settings


# 在这里创建模型

# 练习题目信息表
class question(models.Model):
    title = models.CharField(max_length=50)
    simplemsg = models.CharField(max_length=100)  # 缩略信息
    msg = models.CharField(max_length=255)  # 题目信息
    uploadsrc = models.CharField(max_length=500)
    oneblood = models.CharField(max_length=100)
    twoblood = models.CharField(max_length=100)
    threeblood = models.CharField(max_length=100)
    trycnt = models.IntegerField()
    accnt = models.IntegerField()
    score = models.IntegerField()
    flag = models.CharField(max_length=255)
    type = models.CharField(max_length=100)


# 用户练习数据存储表
class question_user(models.Model):
    UID = models.IntegerField()
    acCnt = models.IntegerField()
    submitCnt = models.IntegerField()
    acList = models.CharField(max_length=5000)
    misccnt = models.IntegerField()
    cryptocnt = models.IntegerField()
    webcnt = models.IntegerField()
    pwncnt = models.IntegerField()
    recnt = models.IntegerField()


# 查询题目列表
def FindQuestionList(type):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询所有misc题目
    sqlToGetQuesionList = "SELECT id,title,simplemsg FROM question where type = 'misc'"
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetQuesionList)
        # 获取所有记录列表,以元组来存储
        questionList = cursor.fetchall()
    except:
        print("查找题目数据错误！")

    cursor.close()
    db.close()

    return questionList


# 查询用户的通过题目列表
def FindUserAcList(request):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 获取当前登陆用户的ID
    acList = ''
    U_id = request.session.get('_auth_user_id')
    sqlToGetUserAcList = "SELECT acList FROM question_user where UID = %s" % (U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetUserAcList)
        # 获取所有记录列表,以元组来存储
        res = cursor.fetchall()
        for row in res:
            acList = row[0]
    except:
        print("查询用户已作答题目列表出错！")

    cursor.close()
    db.close()

    return acList

# 更新用户通过题目列表
def UpdateUserAcList(request,acStr):
    U_id = request.session.get('_auth_user_id')
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 更新语句
    sqlToUpdate = "UPDATE question_user SET acList = '%s' WHERE UID = %s" % (acStr, U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToUpdate)
        # 提交到数据库执行
        db.commit()
    except:
        print("更新用户通过题目列表失败！")

    cursor.close()
    db.close()


# 查询用户的用户名,imc
def FindUserInfo():
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 按用户的imc排序查询信息
    sqlToGetUserList = "SELECT id,username,imc FROM auth_user order by imc desc"
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetUserList)
        # 获取所有记录列表,以元组来存储
        info = cursor.fetchall()
    except:
        print("查询用户注册数据出错！")

    cursor.close()
    db.close()

    return info


# 查询用户的基准信息，UID，姓名，喜欢的题目类型
def FindUserData():
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询用户基准画像信息
    sqlToGetUserData = "SELECT UID,name,likething FROM now_user order by UID"
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetUserData)
        # 获取所有记录列表,以元组来存储
        userData = cursor.fetchall()
    except:
        print("查询用户基准数据出错！")

    cursor.close()
    db.close()

    return userData


# 查询题目的flag信息
def FindQuestionFlag(title):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询题目的flag值
    sqlToGetFlag = "SELECT flag FROM question where title = '%s'" % (title)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetFlag)
        # 获取所有记录列表,以元组来存储
        rightFlagList = cursor.fetchall()
        for row in rightFlagList:
            rightFlag = row[0]

    except:
        print("查询题目的flag出错！")
    cursor.close()
    db.close()

    return rightFlag


# 当用户正确做作答一题时，更新题目的ac次数
def UpdateQuestionAcCnt(title):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sqlToAddAcCnt = "UPDATE question SET accnt = accnt + 1 WHERE title = '%s'" % (title)
    try:
        # 执行SQL语句
        cursor.execute(sqlToAddAcCnt)
        # 提交到数据库执行
        db.commit()
    except:
        print("更新题目ac次数失败！")
    cursor.close()
    db.close()


# 当用户作答一题时，更新题目的try次数
def UpdateQuestionTryCnt(title):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sqlToAddTryCnt = "UPDATE question SET trycnt = trycnt + 1 WHERE title = '%s'" % (title)
    try:
        # 执行SQL语句
        cursor.execute(sqlToAddTryCnt)
        # 提交到数据库执行
        db.commit()
    except:
        print("更新题目try次数失败！")
    cursor.close()
    db.close()


# 当用户作答一题时，更新用户的submit次数
def UpdateUserSubmitCnt(request):
    # 用户的尝试数目+1
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')
    flag = ""  # 用户题目数据是否存在

    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询用户题目信息
    sqlToGetUID = "SELECT UID FROM question_user \
                       WHERE UID = %s" % (U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetUID)
        # 获取所有记录列表,以元组来存储
        results = cursor.fetchall()
        flag = results[0]
    except:
        # 没有数据
        print("用户题目数据查询UID失败！")

    # 用户没有创建过数据，则在表中插入一组UID数据
    if flag == "":

        sqlToAddQuestionLine = "INSERT INTO question_user \
                            (UID,acCnt, submitCnt , acList, misccnt,cryptocnt,webcnt,pwncnt,recnt,testamount) \
                               VALUES (%s,0,1,'',0,0,0,0,0,0)" % (U_id)
        try:
            # 执行sql语句
            cursor.execute(sqlToAddQuestionLine)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            print("插入用户题目数据失败！")

    # 用户已经创建过数据表，则进行更新操作,用户尝试数+1
    else:

        sqlToAddUserSubCnt = "UPDATE question_user SET submitCnt = submitCnt + 1 WHERE UID = %s" % (U_id)
        try:
            # 执行SQL语句
            cursor.execute(sqlToAddUserSubCnt)
            # 提交到数据库执行
            db.commit()
        except:
            print("更新用户submit数失败！")

    cursor.close()
    db.close()

# 当用户正确作答一题时，更新用户的acCnt
def UpdateUserAcCnt(request):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')

    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 更新语句
    sqlToAddUserAcCnt = "UPDATE question_user SET acCnt = acCnt + 1 WHERE UID = %s" % (U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToAddUserAcCnt)
        # 提交到数据库执行
        db.commit()
    except:
        print("更新用户的acCnt失败！")
    cursor.close()
    db.close()


# 通过UID查询用户的用户名
def FindUsernameByID(request):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')
    username = ''

    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sqlToGetUsername = 'select username from auth_user where id = %s' % (U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetUsername)
        # 获取所有记录列表,以元组来存储
        userList = cursor.fetchall()
        for row in userList:
            username = row[0]
    except:
        print("通过UID查询用户名失败！")

    cursor.close()
    db.close()

    return username


# 设置题目的一二三血
def UpdateQuestionBlood(username, title):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    oneblood = ''
    twoblood = ''
    threeblood = ''

    # SQL 查询题目的一二三血
    sqlToGetBlood = "SELECT oneblood,twoblood,threeblood FROM question where title = '%s'" % (title)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetBlood)
        # 获取所有记录列表,以元组来存储
        bloodList = cursor.fetchall()
        for row in bloodList:
            oneblood = row[0]
            twoblood = row[1]
            threeblood = row[2]
        if oneblood == None:

            sql = "UPDATE question SET oneblood = '%s' WHERE title = '%s'" % (username, title)
            try:
                # 执行SQL语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # 发生错误时回滚
                print("添加一血失败！")
        elif oneblood != None and twoblood == None and oneblood != username:

            sql = "UPDATE question SET twoblood = '%s' WHERE title = '%s'" % (username, title)
            try:
                # 执行SQL语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                print("添加二血失败！")
        elif oneblood != None and twoblood != None and threeblood == None and oneblood != username and twoblood != username:
            # SQL 更新语句
            sql = "UPDATE question SET threeblood = '%s' WHERE title = '%s'" % (username, title)
            try:
                # 执行SQL语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                print("添加三血失败！")
        else:
            print("一二三血都已经有人啦！")

    except:
        print("查询题目一二三血失败！")

    cursor.close()
    db.close()


# 判断question_user表里是否有当前UID的数据
def CheckQuesUserHaveUID(request):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    flag = ""  # 用户题目数据是否存在

    # SQL 查询语句
    sqlToFindUID = "SELECT UID FROM question_user \
                   WHERE UID = %s" % (U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToFindUID)
        # 获取所有记录列表,以元组来存储
        results = cursor.fetchall()
        flag = results[0]
    except:
        print("用户题目表中查询是否存在UID错误！")

    cursor.close()
    db.close()

    return flag


# 用户题目数据表中添加一条记录
def AddQuesUserLine(request):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sqlToAddQuesUserLine = "INSERT INTO question_user \
                        (UID,acCnt, submitCnt , acList, misccnt,cryptocnt,webcnt,pwncnt,recnt) \
                           VALUES (%s,0,0,'',0,0,0,0,0)" % (U_id)
    try:
        # 执行sql语句
        cursor.execute(sqlToAddQuesUserLine)
        # 提交到数据库执行
        db.commit()
    except:
        print("用户题目数据插入一条当前UID数据失败！")

    cursor.close()
    db.close()

# 更新用户作答题目类型数量
def UpdateUserTypeQuestion(request,type):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    if type == 'misc':
        # SQL 更新语句
        sql = "UPDATE question_user SET misccnt = misccnt + 1 WHERE UID = %s" % (U_id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

    if type == 'crypto':
        # SQL 更新语句
        sql = "UPDATE question_user SET cryptocnt = cryptocnt + 1 WHERE UID = %s" % (U_id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

    if type == 're':
        # SQL 更新语句
        sql = "UPDATE question_user SET recnt = recnt + 1 WHERE UID = %s" % (U_id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

    if type == 'web':
        # SQL 更新语句
        sql = "UPDATE question_user SET webcnt = webcnt + 1 WHERE UID = %s" % (U_id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

    if type == 'pwn':
        # SQL 更新语句
        sql = "UPDATE question_user SET pwncnt = pwncnt + 1 WHERE UID = %s" % (U_id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

    cursor.close()
    db.close()

# 通过title获取题目的分数
def FindQuestionScore(title):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 获取该题目对应的分数
    score = 0

    sqlToGetQuesScore = "SELECT score FROM question WHERE title = '%s'" % (title)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetQuesScore)
        # 获取所有记录列表,以元组来存储
        results = cursor.fetchall()
        for row in results:
            score = row[0]
    except:
        print("通过title获取题目分数失败！")
    cursor.close()
    db.close()

    return score

# 更新IMC币的数量
def UpdateImc(request,score):
    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 更新imc币,用于购买一些软件，付费培训课程，以及兑换现金
    # SQL 更新语句
    sqlToUpdateImc = "UPDATE auth_user SET imc = imc + %s WHERE id = %s" % (score, U_id)
    try:
        # 执行SQL语句
        cursor.execute(sqlToUpdateImc)
        # 提交到数据库执行
        db.commit()
    except:
        print("imc币更新失败！")

    cursor.close()
    db.close()


# 通过题目id查找题目对应的信息
def FindQuestionByID(questionId):
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user=settings.DATABASES['default']['USER'],
                         password=settings.DATABASES['default']['PASSWORD'],
                         database=settings.DATABASES['default']['NAME'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询题目具体信息
    sqlToGetQuesData = "SELECT title,msg,type,uploadsrc,oneblood,twoblood,threeblood,trycnt,accnt,score FROM question where id = %s " % (
        questionId)
    try:
        # 执行SQL语句
        cursor.execute(sqlToGetQuesData)
        # 获取所有记录列表,以元组来存储
        questionData = cursor.fetchall()

    except:
        print("根据ID查找题目信息失败！")

    cursor.close()
    db.close()

    return questionData