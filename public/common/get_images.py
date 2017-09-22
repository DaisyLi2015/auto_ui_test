import os
from public.common.get_config import r_config
from selenium.webdriver import Remote
from selenium import webdriver


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
conf_path = BASE_DIR + '/config/config.ini'
conf_path = conf_path.replace('/', '\\')
img_path = r_config(conf_path, "image", "img_path")
print(img_path)



def insert_img(driver, file_name):
    driver.get_screenshot_as_file(file_name)



# 启动浏览器驱动
def browser():
    driver = webdriver.Chrome()
    '''
    host = '127.0.0.1:4444' # 运行主机：端口号 （本机默认：127.0.0.1:4444）
    dc = {'browserName': 'chrome'} # 指定浏览器（'chrome','firefox',）
    driver = Remote(command_executor='http://' + host + '/wd/hub',
                    desired_capabilities=dc)
    '''
    return driver






if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    insert_img('123')
    driver.quit()




