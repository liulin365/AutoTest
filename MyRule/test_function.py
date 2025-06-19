import pytest


class Testfunction:
    usename_1= ''
    token1 = ''
    # @pytest.fixture(scope="class",autouse=True)
    # def first_do(self):
    #     print('这是一个前置处理程序。')

    def test_login(self):
        username = 'liulin'
        password = '123456'
        token = 'token'
        Testfunction.token1 = token
        Testfunction.usename_1 = username
        assert Testfunction.token1 == token


    def test_userinfo(self):

        headers = {'token' : Testfunction.token1}
        assert headers['token'] == Testfunction.token1

