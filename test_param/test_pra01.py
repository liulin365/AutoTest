import pytest

# 单参数
# @pytest.mark.parametrize('name',['李宗恒'])
# def test_param(name):
#     print('我是'+ name)

# @pytest.mark.parametrize('name',['提莫','蛮王','剑豪'])
# def test_param(name):
#     print('我是'+ name)

# 多个参数，多次循环
@pytest.mark.parametrize("name,word",[('安其拉','火焰是我的'),('剑圣','你的剑'),('蛮王','饥渴难耐')])
def test_fuck(name,word):
    print(name,word)