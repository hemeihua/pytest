import pytest
from util.httpUtil import HttpUtil
from common.commonData import CommonData

http = HttpUtil()

@pytest.fixture(scope='session',autouse=True)
# @pytest.fixture(scope='function',autouse=True)
# @pytest.fixture(scope='class',autouse=False)
def session_fixture():
    data = {"userName":CommonData.mobile,"password":CommonData.password}
    resp_login = http.post("/sys/login",data)
    print(resp_login)
    CommonData.token = resp_login['object']['token']
    assert resp_login['code'] == 200
    print("登录成功")
    yield
    data = {}
    resp_tuichu = http.post("//sys/getUserInfo",data)
    assert resp_tuichu['code'] == 200
    print("退出成功")








# http = requests.session()
#
# # 全局初始化
#
# @pytest.fixture(scope='session',autouse=True)
# # @pytest.fixture(scope='class',autouse=False)
# # @pytest.fixture(scope='module',autouse=True)
# # @pytest.fixture(scope='function',autouse=True)
# def session_fixture(user,pwd):
#
#     proxies = {'http': 'http://localhost:8888'}
#     headers = {'Content-Type':'application/json;charset=UTF-8'}
#
#     resp_login = http.post(url='http://192.168.1.203:8083/sys/login',
#                      proxies=proxies,
#                      data='{"userName":"'+user+'","password":"'+pwd+'"}',
#                      headers=headers)
#
#     print("登录成功",resp_login.status_code==200)
#     print(resp_login.text)
#     resp_dict = json.loads(resp_login.text)
#     token = resp_dict['object']['token']
#     yield
#     headers['token'] = token
#
#     resp1 = http.post(url='http://192.168.1.203:8083/sys/getUserInfo',
#                           proxies=proxies,
#                           data=None,
#                           headers=headers)
#     print("退出登录",resp1.status_code==200)
#     print(resp1.text)