import pytest

from utils.read_config import getdata

# @pytest.mark.parametrize配合读取yaml参数传递

@pytest.mark.parametrize('dataname',getdata())
def test_usedata(dataname):
    print(dataname)


