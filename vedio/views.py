from django.shortcuts import render, redirect
import requests
from .models import *
import json

def isLogin(request):
    # 检查用户是否登录
    if not request.user.is_authenticated:
        print("登录认证失败！")
        return False
    else:
        print("登录认证成功！")
        return True

# Create your views here.
# 视频中心主页展示
def showved(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")


    res = FindVideoListByType('classv')

    # 学习视频
    classList = list(map(list, res))
    for data in classList:  # 播放量转化为整数
        data[2] = format(data[2], '.0f')

    res = FindVideoListByType('play')
    # 娱乐视频
    playList = list(map(list, res))
    for data in playList:  # 播放量转化为整数
        data[2] = format(data[2], '.0f')

    res = FindVideoListByType('movie')
    # 影视视频
    movieList = list(map(list, res))
    for data in movieList:  # 播放量转化为整数
        data[2] = format(data[2], '.0f')


    return render(request, "home.html", {"classList": classList, "playList": playList, \
                                         "userflag": userflag, "movieList": movieList})


# 最近观看
def watchlater(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    # 查询用户名
    username = FindUsernameByID(request)

    # 查询用户简介
    perdes = FindPerdesByID(request)



    return render(request, "your-watch-later.html", {"username": username, "perdes": perdes, \
                                                     "userflag": userflag})


# 喜欢的视频
def like(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    username = FindUsernameByID(request)

    perdes = FindPerdesByID(request)


    return render(request, "your-laked-videos.html", {"username": username, "perdes": perdes, \
                                                      "userflag": userflag})


def showtime(request):
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")


    # 获取播放视频的ID信息
    vedioid = request.GET.get("vedioid")


    vediocnt = 0
    vedioCollection = ''
    visrc = ''

    # 根据id查询视频信息
    res = FindVideoDataByID(vedioid)

    for row in res:
        vediocnt = row[3]
        vediocnt = format(vediocnt, '.0f')
        vedioCollection = row[10]
        visrc = row[8]

    # 元组转列表
    vedioresult = list(map(list, res))

    # bilibili视频接口操作
    videoData = ''  # 接口返回的字符串
    bilibiliVisrc = ''  # 视频真实地址
    # 视频地址不是服务器上的视频，而是调用bilibili的接口
    # 接口需要的是bilibili使用的BV号
    if not visrc.startswith("http"):
        key = settings.DATABASES['default']['apiKey']  # API-Key
        id = visrc  # 视频BV号
        url = 'https://qqlykm.cn/api/bilibili/get?key=' + key + '&id=' + id  # Bilibili视频API

        wb_data = requests.get(url)
        videoData = wb_data.text  # 类型:字符串

        dict_videoData = json.loads(videoData,strict=False) # 类型：字典
        print("dict_videoData" , dict_videoData)

        bilibiliVisrc = dict_videoData['data']['videourl']

        vedioresult[0][8] = bilibiliVisrc # 进行视频地址转化

    # 更新视频观看次数
    UpdateVideoCnt(vedioid)

    # 查找相似视频
    vediores = FindVideoCollection(vedioCollection)

    vedioList = list(map(list, vediores))


    return render(request, "single-video.html", {"vedioresult": vedioresult, "userflag": userflag, \
                                                 "vediocnt": vediocnt, "vedioList": vedioList})


def music(request):  # 音乐盒子
    userflag = isLogin(request)
    if userflag == False:
        return redirect("/now/login/")

    url = 'http://api.wpbom.com/api/neran.php'  # api链接,网易云数据接口
    wb_data = requests.get(url)  # 引入requests库来请求数据

    # 获取音乐数据
    musicData = wb_data.text  # 类型:字符串

    # 接受到的数据不是严格的json格式，因此进行转换
    reMusicData = musicData[5:]

    dict_musicData = json.loads(reMusicData)  # 转化字符串为字典
    print("字典类型的音乐返回数据：" , dict_musicData)

    musicUrl = dict_musicData['meta']['music']['musicUrl']
    musicImg = dict_musicData['meta']['music']['preview']
    musicName = dict_musicData['meta']['music']['title']



    return render(request, "music.html", {"userflag": userflag, "musicUrl": musicUrl, \
                                          "musicImg": musicImg, "musicName": musicName, \
                                          })
