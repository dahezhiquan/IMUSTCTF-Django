from django.shortcuts import render,redirect


# Create your views here.

def isLogin(request):
    # 检查用户是否登录
    if not request.user.is_authenticated:
        print("登录认证失败！")
        return False
    else:
        print("登录认证成功！")
        return True


def bear(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")
    return render(request, "bear.html")
