from conftest import http
import pytest
import allure
@allure.feature('登录模块')
# @pytest.mark.login
class Test_Login():
    @allure.story('正确登录')
    def test_login(self):
        data = {
            'userName':'15935158135',
            'password':'123456'
        }

        resp = http.post('/sys/login',data)
        assert resp['code'] == 200
        assert resp['msg'] == "操作成功"
        assert resp['object']['userId'] == 148
        print("正确登录-----------------------------------------------------")
    @allure.story('用户名不正确')
    def test_login_fail(self):
        data = {
            'userName':'123456789',
            'password':'123456'
        }
        resp = http.post('/sys/login',data)
        assert resp['code'] == 410
        assert resp['msg'] == "用户不存在"
        print("用户名不正确-------------------------------------------------")

    @allure.story('用户名太长')
    def test_login_fail1(self):
        data = {
            'userName': '1222131564789465451234889546546136548894165',
            'password': '123456'
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 410
        assert resp['msg'] == "用户不存在"
        print("用户名太长------------------------------------------------------")

    @allure.story('密码不正确')
    def test_login_fail2(self):
        data = {
            'userName': '15935158135',
            'password': '456789'
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 410
        assert resp['msg'] == "用户名或密码错误"
        print("密码不正确--------------------------------------------------------")

    @allure.story('用户名为空')
    def test_login_fail3(self):
        data = {
            'userName': '',
            'password': '456789'
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 410
        assert resp['msg'] == "此账户禁止登录"
        print("用户名为空--------------------------------------------------------")

    @allure.story('密码为空')
    def test_login_fail4(self):
        data = {
            'userName': '15935158135',
            'password': ''
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 410
        assert resp['msg'] == "用户名或密码错误"
        print("密码为空--------------------------------------------------------")
@pytest.fixture(autouse=True)
def first_fixture():
    print("登录+++++++++++++++++++++++++++++++++")

