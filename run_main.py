import pytest
import requests
import re


if __name__=='__main__':
    # pytest.main(['-s','-m=info','-q'])
    # pytest.main(['-s'])
    # pytest.main(['-s','-m=changePwd','-q','--alluredir','./report/xml'])
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])

