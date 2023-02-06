from django.shortcuts import render, redirect, HttpResponse
import requests
import json
from .judeging import *
from .models import *



def isLogin(request):
    # 检查用户是否登录
    if not request.user.is_authenticated:
        print("登录认证失败！")
        return False
    else:
        print("登录认证成功！")
        return True


# 主页
def homeproc(request):
    userflag = isLogin(request)

    key = settings.DATABASES['default']['apiKey']  # API-Key
    type = "itzhijia"  # 平台类型

    url = 'https://qqlykm.cn/api/hotlist/get?key=' + key + '&type=' + type  # IT之家热榜API

    wb_data = requests.get(url)

    hotData = wb_data.text  # 类型:字符串

    dict_hotData = json.loads(hotData)  # 转化字符串为字典

    totalData = dict_hotData['data'] # 获取热搜的具体数据

    data = totalData[0:3] # 只取前三条热搜,形成最终的展示数据data

    return render(request, "index.html", {"userflag": userflag, "data":data })


# 题目列表展示
def misc(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    questionList = FindQuestionList('misc')

    acList = FindUserAcList(request)

    return render(request, "misc.html", {"userflag": userflag, "questionList": questionList,\
                                         "acList":acList})

# 检查flag内容
def textflag(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")


    title = request.GET.get('title')
    type = request.GET.get('type')  # 题目类型
    # 未处理的flag值
    unflag = request.GET.get('flag')
    # 处理后的flag值
    flag = unflag[5:]
    judeg = ''
    rightFlag = FindQuestionFlag(title)

    # 判断答题正确与否
    if rightFlag == flag:
        judeg = "正确"

        # 题目ac数 + 1
        UpdateQuestionAcCnt(title)

        addjudge(request, title, type)  # 答对之后后续的一些操作(对用户数据)，防止代码冗杂

    else:
        judeg = "错误"

    # 题目尝试数 + 1
    UpdateQuestionTryCnt(title)

    # 用户submit数 + 1
    UpdateUserSubmitCnt(request)

    return HttpResponse(judeg)


# 提交flag页面的渲染
def subflag(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    # 获取题目ID信息
    questionId = request.GET.get("id")

    trycnt = 0
    accnt = 0

    questionData = FindQuestionByID(questionId)

    for row in questionData:
        trycnt = row[7]
        accnt = row[8]

    # 计算正确率
    if trycnt != 0:
        rightRate = accnt / trycnt
    else:
        rightRate = 0.00

    return render(request, "flag.html", {"userflag": userflag, "questionData": questionData, \
                                         "rightRate": rightRate})


# 帮助页面
def faq(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    return render(request, "faq.html", {"userflag": userflag})


# 排行榜
def ranking(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")


    info = FindUserInfo()

    userData = FindUserData()

    # 将二维元组转化为二维列表
    infoList = list(map(list, info))
    userDataList = list(map(list, userData))

    cnt = 0
    # 处理列表数据，整合到一个列表infoList里面
    for ina in infoList:
        for inb in userDataList:
            if ina[0] == inb[0]:
                infoList[cnt].append(inb[1])
                infoList[cnt].append(inb[2])
                break
        cnt = cnt + 1


    return render(request, "ranking.html", {"userflag": userflag, "infoList": infoList})
