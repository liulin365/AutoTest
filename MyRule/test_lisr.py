import pytest
import requests

class Test_shop:
    def setup_class(self):
        print('\n开始测试的操作')

    @pytest.mark.skip
    @pytest.mark.skipif('1 == 1') # 加的判断条件，为True则跳过，否则不跳过
    def teardown_class(self):
        print('\n结束测试的操作')
    def test_buy(self):
        print('buy..................')


    def test_order(self):
        print('order................')


    def test_sercher(self):
        print('sercher..............')


    def test_login(self):
        print('login................')


# 使用main函数控制  整个页面的所有用例一起执行
if __name__ == '__main__':
    pytest.main()
