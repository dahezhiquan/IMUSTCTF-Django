from django.shortcuts import render, redirect, HttpResponse
import requests
import json
from .models import *

def isLogin(request):
    # 检查用户是否登录
    if not request.user.is_authenticated:
        print("登录认证失败！")
        return False
    else:
        print("登录认证成功！")
        return True


# Git学习
def git(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    return render(request,'git.html',{"userflag":userflag})



# 模拟面试主页
def interview(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    # 查找所有面试大类列表内容
    securityList = FindAllInterviewList()

    return render(request, 'interview.html', {"securityList": securityList})


# 模拟面试通话
def call(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    project = request.GET.get("project")
    id = request.GET.get("id")

    # 查找具体类型的面试列表
    projectList = FindTypeInterviewList(project)

    # 根据ID查找面试官
    interviewerList = FindInterviewChapterByID(id)

    # 查找面试题目
    questionList = FindQuestion(project,id)

    return render(request, 'calls.html', {"projectList": projectList, "pro": project, "id": id, \
                                          "interviewerList": interviewerList,"questionList":questionList})


# IMUSTCTF小宠物,将文字信息转化为语音
def callapi(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")
    introduce = request.GET.get('introduce')
    lan = request.GET.get('lan')
    key = settings.DATABASES['default']['apiKey']  # API-Key
    name = lan # 模型

    url = 'https://qqlykm.cn/api/tTS/get?key=' + key + '&content=' + introduce + '&speed=-100' + '&name=' + name

    wb_data = requests.get(url)

    # api返回信息
    calldata = wb_data.text  # 类型:字符串

    dict_callData = json.loads(calldata)  # 转化字符串为字典

    dict_now = dict_callData["data"] # 取data

    ausrc = dict_now["mp3_url"] # 取音频链接


    return HttpResponse(ausrc)
