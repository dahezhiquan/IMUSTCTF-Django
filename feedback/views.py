from django.shortcuts import render, redirect
from datetime import datetime
from .models import *


def isLogin(request):
    # 检查用户是否登录
    if not request.user.is_authenticated:
        print("登录认证失败！")
        return False
    else:
        print("登录认证成功！")
        return True


def feedMain(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")
    print("userflag:" , userflag)
    return render(request, "feedindex.html", {"userflag": userflag})


# 输入表单的数据存入数据库
def getback(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    # 查询当前用户的用户名
    username = FindUsernameByID(request)

    # 获取表单数据
    if request.method == "POST":
        name = request.POST.get("name", None)
        age = request.POST.get("age", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        data = request.POST.get("data", None)
        time = datetime.now()

        # 提交检查信息
        message = "提交成功！"

        # 反馈信息后端检查
        if len(name) > 30 or len(age) > 20 or len(email) > 30 or len(phone) > 30 or len(data) > 5000:
            message = "提交的信息这么长，是不是想搞破坏！"
        else:
            if len(name) == 0 or len(age) == 0 or len(email) == 0 or len(phone) == 0 or len(data) == 0:
                message = "提交的信息中存在空的情况！"
            else:
                # 表单信息存入数据库
                ageNumber = int(age)
                insertIntoUserBack(username, name, ageNumber, email, phone, data, time)

    return render(request, "feedindex.html", {"message": message, "userflag": userflag})
