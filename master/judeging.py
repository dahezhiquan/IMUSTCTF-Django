from .addtype import *
from .models import *

# 此函数在用户提交题目时更新用户本身的一些信息
# 比如用户答题数，通过数，答题列表等
def addjudge(request, title, type):

    # 获取用户名
    username = FindUsernameByID(request)

    # 更新一二三血
    UpdateQuestionBlood(username,title)

    # 判断用户题目数据表中是否有当前UID的记录
    flag = CheckQuesUserHaveUID(request)

    # 用户没有创建过数据，则在表中插入一组UID数据
    if flag == "":
        # 用户题目数据表中插入一条当前UID的数据
        AddQuesUserLine(request)
        addtype(request,type,title)

    # 用户已经创建过数据表，则进行更新操作
    else:
        addtype(request, type, title)

