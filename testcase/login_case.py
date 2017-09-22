

from time import sleep
import unittest, random, sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf = BASE_DIR + '/config/config.ini'

public = base = BASE_DIR + '/public'
common = BASE_DIR + '/public/common'
base = BASE_DIR + '/public/base'

conf_path = conf.replace('/', '\\')
public_path = public.replace('/', '\\')
common_path = common.replace('/', '\\')
base_path = base.replace('/', '\\')

sys.path.append(conf_path)
sys.path.append(public_path)
sys.path.append(base_path)
sys.path.append(common_path)

from public.common import my_unit
from public.base.login_page import LoginPage




class loginTest(my_unit.MyTest):
    '''社区登录测试'''

    def test_login_user_pawd_null(self):
        '''用户名、密码为空登录'''
        po = LoginPage(self.driver)
        po.open('http://192.168.20.12:8080/nisdn_platform/')
        username = ""
        passwd = ""
        po.pro(username, passwd)
        sleep(2)
        self.assertEqual(po.error_text(), '用户名不能为空！')

    def test_login_pawd_null(self):
        '''密码为空登录'''
        po = LoginPage(self.driver)
        po.open('http://192.168.20.12:8080/nisdn_platform/')
        username = "admin"
        passwd = ""
        po.pro(username, passwd)
        sleep(2)
        self.assertEqual(po.error_text(), '密码不能为空！')

    def test_login_user_pawd_error(self):
        '''用户名、密码为错误'''
        po = LoginPage(self.driver)
        po.open('http://192.168.20.12:8080/nisdn_platform/')
        character = random.choice('zyxwvutsrqponmlkjihgfedcba')
        username = "admin" + character
        passwd = "admin"
        po.pro(username, passwd)
        sleep(2)
        self.assertEqual(po.error_text(), '用户名只能输入字母或者数字！！')

    def test_login_success(self):
        '''用户名、密码正确，登录成功'''
        po = LoginPage(self.driver)
        po.open('http://192.168.20.12:8080/nisdn_platform/')
        user = "admin"
        passwd = "admin"
        po.pro(user, passwd)
        sleep(2)



if __name__ == '__main__':
    #unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(loginTest("test_login_success"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
