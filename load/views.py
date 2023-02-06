from django.shortcuts import render, redirect
import os
from django.http import HttpResponse, FileResponse
from .icpmethod import *
from .models import *


def isLogin(request):
    # 检查用户是否登录
    if not request.user.is_authenticated:
        print("登录认证失败！")
        return False
    else:
        print("登录认证成功！")
        return True


# ICP备案查询
def imusttools(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    return render(request, "imusttools.html")


# ICP备案接口查询
def res_imusttools(request):
    url = request.GET.get("url")
    realUrl = url[4:]  # 处理ajax的冗余数据，只截取url部分
    icpData = resicp(realUrl)  # icp查询接口文件
    return HttpResponse(icpData)


# 军火库工具页面
def ctftools(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    # 获得军火库类型,这决定要展示什么样的页面内容
    typePage = request.GET.get('type')

    resList = FindArmsByType(typePage)

    return render(request, "ctftools.html", {"resList": resList, "typePage": typePage})


# 密码核对模块
def toolcheck(request):
    # 用户输入的工具密码
    toolPassword = request.GET.get('toolpassword', default=None)

    # 使用隐藏域获取到工具名
    toolName = request.GET.get('toolnameid', default=None)

    results = FindArmsPassword(toolName)

    realPassword = ''
    checktype = ''

    # 判断密码是否与数据库密码一致
    for row in results:
        realPassword = row[0]
        checktype = row[1]

    if (realPassword == toolPassword):
        return redirect('/load/upload/?toolname=' + toolName)

    else:
        message = "密码错误"

    return render(request, "ctftools.html", {"message": message, "checktype": checktype})


# 下载模块
def upload(request):  # 文件下载支持

    toolName = request.GET.get("toolname")
    print("待下载的工具名称：" , toolName)

    filesrc = FindArmsFilesrc(toolName)
    print("文件下载地址：" , filesrc)

    # 远程下载地址
    if filesrc.startswith('http'):
        return redirect(filesrc)
    # 服务器下载
    else:
        cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        response = FileResponse(open(cwd + filesrc, "rb"))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename=' + toolName + '.rar'
        return response
