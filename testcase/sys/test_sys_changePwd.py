from conftest import http
import pytest
import allure

@allure.feature('修改密码模块')
# @pytest.mark.changePwd
class Test_changePwd():
    # @pytest.mark.usefixtures('changePwd1')
    @allure.story('修改密码1*******************')
    def test_changePwd(self):
        data = {
            'userId':148,
            'userName':'15935158135',
            'oldPwd':'123456',
            'password':'456789'
        }
        resp = http.post('/sys/changePwd',data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        print("修改密码成功-----------------------------------------------------")
        self.changePwd1(data)

    @allure.story('修改密码2*******************')
    def test_changePwd1(self):
        data = {
            'userId':1,
            'userName':'15935158135',
            'oldPwd':'123456',
            'password':'159159'
        }
        resp = http.post('/sys/changePwd',data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        print("修改密码成功-----------------------------------------------------")
        self.changePwd1(data)

    def changePwd1(self, data):
        c = data['oldPwd']
        data['oldPwd'] = data['password']
        data['password'] = c
        resp = http.post('/sys/changePwd', data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        print("还原密码成功-----------------------------------------------------")
@pytest.fixture(autouse=True)
def first_fixture():
    print("change密码-----------------")
