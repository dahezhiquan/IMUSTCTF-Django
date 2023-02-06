import requests
import json
from django.conf import settings


# icp备案查询接口
def resicp(url):
    key = settings.DATABASES['default']['apiKey']  # API-Key
    url = 'https://qqlykm.cn/api/icp/get?key=' + key + '&domain=' + url  # ICP备案查询接口

    wb_data = requests.get(url)

    icpData = wb_data.text  # 类型:字符串

    dict_icpData = json.loads(icpData)  # 转化字符串为字典

    # 取出字典里的元素
    icp = dict_icpData['icp']
    unitName = dict_icpData['unitName']
    natureName = dict_icpData['natureName']

    resData = "icp号：" + str(icp) + '；' + '备案实名姓名：' + str(unitName) + '；' + "备案类型：" + str(natureName)

    return resData
