import os
import unittest
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
conf_path = BASE_DIR + '/config/config.ini'
conf_path = conf_path.replace('/', '\\')
from public.common.get_config import r_config
from public.common.get_log import Log
from public.common.get_images import browser, insert_img

img_path = r_config(conf_path, 'image', 'img_path')

class MyTest(unittest.TestCase):

    global case_count
    case_count = 0

    global image_count
    image_count = 0

    # 计算测试用例的个数，用于显示在测试报告中
    def case_id(self):
        global case_count
        case_count += 1
        if case_count <= 9:
            count = "00" + str(case_count)
        elif case_count <= 99:
            count = "0" + str(case_count)
        else:
            count = str(case_count)
        return count

    # 测试完成，生成截图文件的名称
    def image_id(self):
        global image_count
        image_count += 1
        if image_count <= 9:
            count = "00" + str(image_count)
        elif image_count <= 99:
            count = "0" + str(image_count)
        else:
            count = str(image_count)
        return count

    def setUp(self):
        self.logger = Log(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'conf/conf.ini'))
        self.logger.info('############################### START ###############################')
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print("case " + str(self.case_id()))

    def tearDown(self):
        img_id = self.image_id()
        file_name =img_path + img_id + ".jpg"
        print(file_name)
        insert_img(self.driver, file_name)
        self.driver.quit()
        self.logger.info('###############################  End  ###############################')





