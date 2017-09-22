# coding=utf-8

import time,os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import  TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
conf_path = BASE_DIR + '/config/config.ini'
conf_path = conf_path.replace('/', '\\')

from public.common.get_log import Log
from public.common.get_config import r_config
from selenium.webdriver.common.keys import Keys

img_path = r_config(conf_path, 'image', 'img_path')
log_path = r_config(conf_path, 'log', 'log_path')
success = "SUCCESS   "
fail = "FAIL   "
logger = Log(log_path)

class base_frame(object):


    def __init__(self, driver, base_url="http://www.baidu.com"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def my_print(self, msg):
        logger.info(msg)

    def open(self, url):

        t1 = time.time()
        try:
            self.driver.get(url)
            self.my_print("{0} Navigated to {1}, Spend {2} seconds".format(success, url, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to load {1}, Spend {2} seconds".format(fail, url, time.time() - t1))
            raise

    def max_window(self):

        t1 = time.time()
        self.driver.maximize_window()
        self.my_print("{0} Set browser window maximized, Spend {1} seconds".format(success, time.time() - t1))

    def set_window(self, wide, high):

        t1 = time.time()
        self.driver.set_window_size(wide, high)
        self.my_print("{0} Set browser window wide: {1},high: {2}, Spend {3} seconds".format(success,
                                                                                             wide, high,
                                                                                             time.time() - t1))

    def wait(self, secs):

        t1 = time.time()
        self.driver.implicitly_wait(secs)
        self.my_print("{0} Set wait all element display in {1} seconds, Spend {2} seconds".format(success,
                                                                                                  secs,
                                                                                                  time.time() - t1))

    def find_element(self, element):

        if "=" not in element:
            raise NameError("Positioning syntax errors, lack of '='")

        by = element[:element.index("=")]
        value = element[element.index("=")+1:]

        if by == "id":
            return self.driver.find_element_by_id(value)
        elif by == "name":
            return self.driver.find_element_by_name(value)
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        elif by == "text":
            return self.driver.find_element_by_link_text(value)
        elif by == "text_part":
            return self.driver.find_element_by_partial_link_text(value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")

    def wait_element(self, element, seconds=5):


        if "=" not in element:
            raise NameError("Positioning syntax errors, lack of '='")

        by = element[:element.index("=")]
        value = element[element.index("=")+1:]
        messages = 'Element: {0} not found in {1} seconds.'.format(element, seconds)

        if by == "id":
            WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((By.ID, value)), messages)
        elif by == "name":
            WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((By.NAME, value)), messages)
        elif by == "class":
            WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)),
                                                         messages)
        elif by == "text":
            WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)),
                                                         messages)
        elif by == "xpath":
            WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((By.XPATH, value)), messages)
        elif by == "css":
            WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)),
                                                         messages)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")

    def send_keys(self, element, text):

        t1 = time.time()
        try:
            self.wait_element(element)
            self.find_element(element).clear()
            self.find_element(element).send_keys(text)
            self.my_print("{0} Typed element: <{1}> content: {2}, Spend {3} seconds".format(success,
                                                                                            element, text,
                                                                                            time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to type element: <{1}> content: {2}, Spend {3} seconds".format(fail,
                                                                                                     element, text,
                                                                                                     time.time() - t1))
            raise

    def send_keys_and_enter(self, element, text, secs=0.5):

        t1 = time.time()
        try:
            self.wait_element(element)
            self.find_element(element).clear()
            self.find_element(element).send_keys(text)
            time.sleep(secs)
            self.find_element(element).send_keys(Keys.ENTER)
            self.my_print(
                "{0} Element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".format(
                    success, element, text, secs, time.time() - t1))
        except Exception:
            self.my_print(
                "{0} Unable element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".
                    format(fail, element, text, secs, time.time() - t1))
            raise

    def click(self, element):

        t1 = time.time()
        try:
            self.wait_element(element)
            self.find_element(element).click()
            self.my_print("{0} Clicked element: <{1}>, Spend {2} seconds".format(success, element, time.time() - t1))
        except Exception:
            self.my_print(
                "{0} Unable to click element: <{1}>, Spend {2} seconds".format(fail, element, time.time() - t1))
            raise

    def right_click(self, element):

        t1 = time.time()
        try:
            self.wait_element(element)
            ActionChains(self.driver).context_click(self.find_element(element)).perform()
            self.my_print(
                "{0} Right click element: <{1}>, Spend {2} seconds".format(success, element, time.time() - t1))
        except Exception:
            self.my_print(
                "{0} Unable to right click element: <{1}>, Spend {2} seconds".format(fail, element, time.time() - t1))
            raise

    def move_to_element(self, element):

        t1 = time.time()
        try:
            self.wait_element(element)
            ActionChains(self.driver).move_to_element(self.find_element(element)).perform()
            self.my_print("{0} Move to element: <{1}>, Spend {2} seconds".format(success, element, time.time() - t1))
        except Exception:
            self.my_print(
                "{0} unable move to element: <{1}>, Spend {2} seconds".format(fail, element, time.time() - t1))
        raise

    def double_click(self, element):

        t1 = time.time()
        try:
            self.wait_element(element)
            ActionChains(self.driver).double_click(self.find_element(element)).perform()
            self.my_print(
                "{0} Double click element: <{1}>, Spend {2} seconds".format(success, element, time.time() - t1))
        except Exception:
            self.my_print(
                "{0} Unable to double click element: <{1}>, Spend {2} seconds".format(fail, element, time.time() - t1))
        raise

    def drag_and_drop(self, source_element, target_element):

        t1 = time.time()
        try:
            self.wait_element(source_element)
            self.wait_element(target_element)
            ActionChains(self.driver).drag_and_drop(self.find_element(source_element),
                                                    self.find_element(target_element)).perform()
            self.my_print("{0} Drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(success,
                                                                                                         source_element,
                                                                                                         target_element,
                                                                                                         time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(fail,
                                                                                                                   source_element,
                                                                                                                   target_element,
                                                                                                                   time.time() - t1))
        raise

    def back(self):

        t1 = time.time()
        self.driver.back()
        self.my_print("{0} Back to old window, Spend {1} seconds".format(success, time.time() - t1))

    def forward(self):

        t1 = time.time()
        self.driver.forward()
        self.my_print("{0} Forward to old window, Spend {1} seconds".format(success, time.time() - t1))

    def get_attribute_on(self, element, attribute):

        t1 = time.time()
        try:
            self.wait_element(element)
            attr = self.find_element(element).get_attribute(attribute)
            self.my_print("{0} Get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(success,
                                                                                                      element,
                                                                                                      attribute,
                                                                                                      time.time() - t1))
            return attr
        except Exception:
            self.my_print("{0} Unable to get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(fail,
                                                                                                                element,
                                                                                                                attribute,
                                                                                                                time.time() - t1))
            raise

    def get_text(self, element):

        t1 = time.time()

        try:
            self.wait_element(element)
            text = self.find_element(element).text
            self.my_print(
                "{0} Get element text element: <{1}>, Spend {2} seconds".format(success, element, time.time() - t1))
            return text
        except Exception:
            self.my_print(
                "{0} Unable to get element text element: <{1}>, Spend {2} seconds".format(fail, element,
                                                                                          time.time() - t1))
            raise

    def get_display(self, element):

        t1 = time.time()
        try:
            self.wait_element(element)
            self.find_element(element).is_displayed()
            self.my_print("{0} the element is display, Spend {1} seconds".format(success, time.time() - t1))
            return True
        except Exception:
            self.my_print("{0} the element is not display, Spend {1} seconds".format(fail, time.time() - t1))
            return False

    def get_title(self):

        t1 = time.time()
        title = self.driver.title
        self.my_print("{0} Get current window title, Spend {1} seconds".format(success, time.time() - t1))
        return title

    def get_url(self):

        t1 = time.time()
        url = self.driver.current_url
        self.my_print("{0} Get current window url, Spend {1} seconds".format(success, time.time() - t1))
        return url

    def get_screenshot(self, file_name):

        t1 = time.time()
        try:
            file_path = img_path + file_name
            self.driver.get_screenshot_as_file(file_path)
            self.my_print("{0} Get the current window screenshot,path: {1}, Spend {2} seconds".format(success,
                                                                                                      file_path,
                                                                                                      time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to get the current window screenshot,path: {1}, Spend {2} seconds".format(fail,
                                                                                                                file_path,
                                                                                                                time.time() - t1))
            raise

    def submit(self, element):

        t1 = time.time()
        try:
            self.wait_element(element)
            self.find_element(element).submit()
            self.my_print(
                "{0} Submit form args element: <{1}>, Spend {2} seconds".format(success, element, time.time() - t1))
        except Exception:
            self.my_print(
                "{0} Unable to submit form args element: <{1}>, Spend {2} seconds".format(fail, element,
                                                                                          time.time() - t1))
        raise

    def switch_to_frame(self, element):

        t1 = time.time()
        try:
            self.wait_element(element)
            self.driver.switch_to.frame(self.find_element(element))

            self.my_print(
                "{0} Switch to frame element: <{1}>, Spend {2} seconds".format(success, element, time.time() - t1))
        except Exception:
            self.my_print(
                "{0} Unable switch to frame element: <{1}>, Spend {2} seconds".format(fail, element, time.time() - t1))
            raise

    def switch_to_frame_out(self):

        t1 = time.time()
        self.driver.switch_to.default_content()
        self.my_print("{0} Switch to frame out, Spend {1} seconds".format(success, time.time() - t1))

    def switch_new_window(self, element):

        t1 = time.time()
        try:
            current_windows = self.driver.current_window_handle
            self.find_element(element).click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != current_windows:
                    self.driver.switch_to.window(handle)
            self.my_print("{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(success,
                                                                                                                element,
                                                                                                                time.time() - t1))
        except Exception:
            self.my_print("{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(fail,
                                                                                                                element,
                                                                                                                time.time() - t1))
            raise

    def into_new_window(self):

        t1 = time.time()
        try:
            all_handle = self.driver.window_handles
            flag = 0
            while len(all_handle) < 2:
                time.sleep(1)
                all_handle = self.driver.window_handles
                flag += 1
                if flag == 5:
                    break
            self.driver.switch_to.window(all_handle[-1])
            self.my_print("{0} Switch to the new window,new window's url: {1}, Spend {2} seconds".format(success,
                                                                                                         self.driver.current_url,
                                                                                                         time.time() - t1))
        except Exception:
            self.my_print("{0} Unable switch to the new window, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    def F5(self):

        t1 = time
        self.driver.refresh()
        self.my_print("{0} Refresh the current page, Spend {1} seconds".format(success, time.time() - t1))

    def js(self, script):

        t1 = time.time()

        try:
            self.driver.execute_script(script)
            self.my_print(
                "{0} Execute javascript scripts: {1}, Spend {2} seconds".format(success, script, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to execute javascript scripts: {1}, Spend {2} seconds".format(fail,
                                                                                                    script,
                                                                                                    time.time() - t1))
            raise

    def accept_alert(self):

        t1 = time.time()

        self.driver.switch_to.alert.accept()
        self.my_print("{0} Accept warning box, Spend {1} seconds".format(success, time.time() - t1))

    def dismiss_alert(self):

        t1 = time.time()
        self.driver.switch_to.alert.dismiss()
        self.my_print("{0} Dismisses the alert available, Spend {1} seconds".format(success, time.time() - t1))

    def close(self):

        t1 = time.time()
        self.driver.close()
        self.my_print("{0} Closed current window, Spend {1} seconds".format(success, time.time() - t1))

    def quit(self):

        t1 = time.time()
        self.driver.quit()
        self.my_print("{0} Closed all window and quit the driver, Spend {1} seconds".format(success, time.time() - t1))

    def element_exist(self, element):

        t1 = time.time()
        try:
            self.wait_element(element)
            self.my_print("{0} Element: <{1}> is exist, Spend {2} seconds".format(success, element, time.time() - t1))
            return True
        except TimeoutException:
            self.my_print("{0} Element: <{1}> is not exist, Spend {2} seconds".format(fail, element, time.time() - t1))
            return False

    @property
    def origin_driver(self):

        return self.driver

    def js_click(self, element):

        t1 = time.time()
        js_str = "$('{0}').click()".format(element)
        try:
            self.driver.execute_script(js_str)
            self.my_print(
                "{0} Use javascript click element: {1}, Spend {2} seconds".format(success, js_str, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to use javascript click element: {1}, Spend {2} seconds".format(fail,
                                                                                                      js_str,
                                                                                                      time.time() - t1))
            raise






if __name__ == '__main__':
    dr = base_frame()
    dr.open('http://www.baidu.com')
    dr.max_window()
    dr.find_element('id=kw')
    dr.get_screenshot('1.jpg')
    dr.close()





