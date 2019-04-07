from util.httpUtil import HttpUtil
from conftest import http
import pytest
import allure
@allure.feature('注册模块')
# http =HttpUtil()
# @pytest.mark.zhuce
class Test_Login:
    @allure.story('注销')
    def test_zhuce(self):
        data = {
            "nickName":"wwwuuu",
            "userName":"15922922114",
            "telNo":"",
            "email":"",
            "address":"",
            "roleIds":"",
            "regionId":1,
            "regionLevel":1
        }
        resp = http.post('/user/saveOrUpdateUser', data)
        # assert resp['code'] == 401
        # assert resp['msg'] == "无权限访问"
        print(resp)
        user=data['userName']
        id=self.login1(user)
        self.huoqu(user,id)
        print("注册成功-----------------------------------------------------")
    def login1(self,user):
        data = {
            'userName': user,
            'password': '123456'
        }

        resp = http.post('/sys/login', data)
        id=resp['object']['userId']
        assert resp['code'] == 200
        assert resp['msg'] == "操作成功"
        print("正确登录-----------------------------------------------------")
        return id
    def huoqu(self,zhuce,id):
        data = {"pageCurrent":1,"pageSize":10,"nickName":"","userName":"","regionId":1}

        resp = http.post('/user/loadUserList', data)

        assert resp['code'] == 200
        assert resp['msg'] == "操作成功"
        assert resp['object']['list'][0]['id'] == id
        assert resp['object']['list'][0]['userName'] == zhuce

        print("获取第一个用户名-----------------------------------------------------")


