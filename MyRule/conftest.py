import pytest

@pytest.fixture(scope='class',autouse=True)
def first_do():
    print('这是前置处理程序。')
    yield
    print('这是后置处理。')