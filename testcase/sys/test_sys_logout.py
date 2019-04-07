# from conftest import http
# import pytest
# import allure
#
# @allure.feature('注销模块')
# @pytest.mark.logout
# class Test_logout():
#     @allure.story('注销')
#     def test_logout(self):
#         data = {
#             'userName': '15935158135',
#             'password': '123456'
#         }
#
#         resp = http.post('/sys/login', data)
#         assert resp['code'] == 200
#         assert resp['msg'] == "操作成功"
#         data  = {}
#         resp = http.post('/sys/logout',data)
#         assert resp['code'] == 200
#         assert resp['msg'] == '操作成功'
#         print('注销成功************************')
# @pytest.fixture(autouse=True)
# def first_fixture():
#     print("注销--------------------")