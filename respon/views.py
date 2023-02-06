from django.shortcuts import render, redirect


def isLogin(request):
    # 检查用户是否登录
    if not request.user.is_authenticated:
        print("登录认证失败！")
        return False
    else:
        print("登录认证成功！")
        return True

def imust(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    return render(request, "imust.html", {"userflag": userflag})


def version(request):
    userflag = isLogin(request)

    return render(request, "version.html",{"userflag": userflag})
