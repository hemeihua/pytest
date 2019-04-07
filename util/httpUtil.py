import requests
import json
from common.commonData import CommonData

class HttpUtil:

    def __init__(self):
        self.http = requests.session()
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}

    def post(self, path, data):
        proxies = CommonData.proxies #获取全局变量proxies
        host = CommonData.host   #获取全局变量host
        data_json = json.dumps(data)  #将data参数转为json格式
        if CommonData.token is not None:
            self.headers['token'] = CommonData.token

        resp_login = self.http.post(url=host+path, #发起post请求
                         proxies=proxies,
                         data=data_json,
                         headers=self.headers)
        assert resp_login.status_code == 200 #校验返回码是否为200
        resp_json = resp_login.text          #获取response响应的body值
        resp_dict = json.loads(resp_json)    #将body值转换为dict
        return resp_dict                     #返回




















# # resp = requests.get('http://www.baidu.com')
# proxies = {'http':'http://localhost:8888'}
# headers = {'Content-Type':'application/json;charset=UTF-8'}
# http = requests.session()
# resp = http.post(url='http://192.168.1.203:8083/sys/login',
#                      proxies=proxies,
#                      data = '{"userName":"18210034706","password":"123456"}',
#                      headers = headers)
# print("******",resp.text)
# print(resp.status_code)
#
# resp_dict = json.loads(resp.text)
# token = resp_dict['object']['token']
# headers['token'] = token
# data = {'token':token}
# data_json = json.dumps(data)
#
# resp1 = http.post(url='http://192.168.1.203:8083/sys/getUserInfo',
#                      proxies=proxies,
#                      data = data_json,
#                      headers = headers)
#
# # assert resp.status_code == 200
# print("5555555555",resp1.text)
# print("--------",resp1.headers)
# print("1111111111111",resp1.status_code)
# # print("++++++++++--",resp1.cookies)
#
# # print("!!!!!!!!!!!!!!!!!1",resp)
# # class HttpUtil:
# #     print("fghdsj")