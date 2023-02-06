from django.shortcuts import render, redirect
from django.contrib import auth  # 用户认证模块
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import *


def isLogin(request):
    # 检查用户是否登录
    if not request.user.is_authenticated:
        print("登录认证失败！")
        return False
    else:
        print("登录认证成功！")
        return True

# 登录页展示
def login_way(request):
    return render(request, "login.html")


# 设置个人信息
def setdata(request):  # 设置个人信息表单

    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')

    # 查询用户的用户名和邮箱
    results = FindUserInfo(request)

    username = ''
    email = ''
    for row in results:
        username = row[0]
        email = row[1]

    # 查询用户基准信息
    nowuser = FindUserData(request)

    for row in nowuser:
        name = row[1]
        birthday = row[2]
        phone = row[3]
        address = row[4]
        perdes = row[5]
        school = row[6]
        major = row[7]
        grade = row[8]
        likething = row[10]



    return render(request, "setdata.html", {"username": username, "email": email, \
                                            "name": name, "birthday": birthday, \
                                            "major": major, "school": school, \
                                            "likething": likething, "perdes": perdes, \
                                            "grade": grade, "phone": phone, "address": address,"U_id":U_id})


# 注册页
def register(request):
    try:
        message = "注册成功！IMUSTCTF送您100imc币~"
        if request.method == "POST":
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            email = request.POST.get("email", None)
            agpassword = request.POST.get("agpassword", None)


            # 反馈信息长度后端检查
            lenflag = 1
            if len(username) > 15 or len(password) > 20 or len(email) > 30 or len(agpassword) > 20:
                lenflag = 0

            print("len username：" , len(username))

            # 检查密码安全性
            passwordflag = 1
            if (len(password) < 8):
                passwordflag = 0

            if (agpassword == password and passwordflag == 1 and lenflag == 1):
                User.objects.create_user(username=username, password=password, email=email)
            elif (agpassword == password and passwordflag == 0):
                message = "密码长度小于8位，请重新输入！"
            elif (agpassword == password and lenflag == 0):
                message = "输入信息过长！请不要破坏登录系统哦~"
            else:
                message = "两次输入的密码不一致，请重新检查输入！"
    except:
        message = "您输入的用户名已被注册，请重新输入！"

    return render(request, "login.html", {"message": message})


# 登录
def loginin(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        lenflag = 1
        # 反馈信息后端检查
        if len(username) > 15 or len(password) > 20:
            lenflag = 0

        if lenflag == 1:
            user_obj = auth.authenticate(username=username, password=password)
            if user_obj == None:
                message = "用户名或密码错误！"
            else:
                message = "登录成功！"
                login(request, user_obj)
        else:
            message = "输入信息过长！请不要破坏登录系统哦~"
    return render(request, "login.html", {"message": message})


# 登出
def logoutout(request):
    auth.logout(request)
    return redirect("/")


def person(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    name = "暂未填写"
    birthday = "暂未填写"
    phone = "暂未填写"
    likething = "没有任何爱好的"
    school = "暂未填写"
    major = "暂未填写"
    perdes = "暂未填写"
    address = "暂未填写"
    grade = "暂未填写"


    # 获取当前登陆用户的ID
    U_id = request.session.get('_auth_user_id')

    # 查询用户的用户名和邮箱
    results = FindUserInfo(request)

    username = ''
    email = ''

    for row in results:
        username = row[0]
        email = row[1]

    # 查询用户基准信息
    nowuser = FindUserData(request)

    for row in nowuser:
        name = row[1]
        birthday = row[2]
        phone = row[3]
        address = row[4]
        perdes = row[5]
        school = row[6]
        major = row[7]
        grade = row[8]
        likething = row[10]

        # 排除用户提交过表单不显示暂未填写的情况
        if name == "":
            name = "暂未填写"
        if birthday == "":
            birthday = "暂未填写"
        if phone == "":
            phone = "暂未填写"
        if address == "":
            address = "暂未填写"
        if perdes == "":
            perdes = "暂未填写"
        if school == "":
            school = "暂未填写"
        if major == "":
            major = "暂未填写"
        if grade == "":
            grade = "暂未填写"

    rightRate = 0.00

    questionData = FindUserQuesCnt(request)
    for row in questionData:
        acCnt = row[0]
        submitCnt = row[1]
        rightRate = acCnt/submitCnt


    # 查询imc
    imc = FindImcByID(request)

    return render(request, "personindex.html", {"username": username, "email": email, \
                                                "name": name, "birthday": birthday, \
                                                "major": major, "school": school, \
                                                "likething": likething, "perdes": perdes, \
                                                "grade": grade, "phone": phone, "address": address, \
                                                "U_id": U_id, "userflag": userflag,"questionData":questionData,\
                                                "imc":imc,"rightRate":rightRate})


# 表单收集
def setdatabase(request):
    # 获取表单数据
    if request.method == "POST":
        name = request.POST.get("name", None)
        birthday = request.POST.get("birthday", None)
        phone = request.POST.get("phone", None)
        address = request.POST.get("address", None)
        perdes = request.POST.get("perdes", None)
        school = request.POST.get("school", None)
        major = request.POST.get("major", None)
        grade = request.POST.get("grade", None)
        likething = request.POST.get("like", None)

        # 获取当前登陆用户的ID
        UID = request.session.get('_auth_user_id')

        try:
            # 获取上传文件的处理对象
            header = request.FILES['header']
            # 创建一个文件,用用户名做名字的头像
            if header == None:
                pass
            else:
                save_path = 'userInfo/header/%s.jpg' % (UID)
                with open(save_path, 'wb') as f:
                    # 获取上传文件的内容并写到创建的文件中
                    for content in header.chunks():
                        f.write(content)
        except:
            print("上传的图片流存入服务器失败！")

        # 更新用户基准信息
        UpdateUserData(request, name, birthday, phone, address, perdes, school, major, grade, likething)

    return redirect("/now/person/")
