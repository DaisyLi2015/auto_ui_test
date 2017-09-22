import os, sys, time, unittest
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
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
from public.common.send_email import send_mail
from public.pakeage.HTMLTestRunner3 import HTMLTestRunner
from public.common.get_config import r_config
from public.common.get_files import get_new_file

img_path = r_config(conf_path, 'image', 'img_path')
log_path = r_config(conf_path, 'log', 'log_path')
report_path = r_config(conf_path, 'report', 'report_path')
test_case_path = r_config(conf_path, 'test_case', 'test_case_path')


if __name__ == '__main__':
    now_time = time.strftime("%Y-%m-%d-%H-%M-%S")
    fp = open(report_path + now_time + "_result.html", 'wb')
    runner = HTMLTestRunner(fp, title="网易邮箱测试报告", description="运行环境：macOS Sierra, chrome")
    discover = unittest.defaultTestLoader.discover(test_case_path, pattern='login_*.py')
    runner.run(discover)
    fp.close()
    file_path = get_new_file(report_path)
    send_mail(file_path)
