from conftest import http
import pytest
import allure

@allure.feature('获取用户信息模块')
# @pytest.mark.getUserInfo
class Test_getUserInfo():

    @allure.story('正确获取用户信息')
    def test_getUserInfo(self):
        data = {
            'userName': '15935158135',
            'password': '123456'
        }

        resp = http.post('/sys/login', data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        print("用户登录成功------------------------------------------")

        data = {}
        resp = http.post('/sys/getUserInfo',data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        print("获取用户信息-----------------------------------------------------")

@pytest.fixture(autouse=True)
def first_fixture():
    print("获取用户信息++++++++++++++++++++++++++++++++++++++++")