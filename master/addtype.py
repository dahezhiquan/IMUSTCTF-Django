from .models import *


# 更新用户具体题目数量，更新用户题目列表
def addtype(request, type, title):
    isrepeat = 0  # 是否重复，用户是否提交了已经正确作答的题目

    # 获取用户通过题目列表
    acStr = FindUserAcList(request)

    if title in acStr:  # 用户重复提交了已经正确作答的题目
        isrepeat = 1
    else:
        acStr = acStr + title + ','  # 用户答题列表添加新数据
        # 更新用户的通过题目列表
        UpdateUserAcList(request, acStr)

    if isrepeat == 0:
        # 更新用户的作答类型数量
        UpdateUserTypeQuestion(request, type)

    # 还要更新下用户通过题目数量，并且加上积分
    if isrepeat == 0:
        # 更新用户的acCnt
        UpdateUserAcCnt(request)

        # 获取当前题目的分值信息
        score = FindQuestionScore(title)

        # 更新用户imc币数量
        UpdateImc(request, score)
