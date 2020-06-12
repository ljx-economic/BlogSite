from selenium import webdriver
import unittest
import time

driver = webdriver.Chrome()
# 设置最大等待时长为 15秒
driver.implicitly_wait(15)
# 通过继承unittest.TestCase来实现用例
class forTest(unittest.TestCase):
    # 初始化测试用例
    def setUp(self):
        print('setUp')
    # 释放
    def tearDown(self):
        print('tearDown')
    # 测试用例，函数名以test_开头
    def test_1(self):# 输入关键字搜索
        driver.get('http://49.235.199.52/')
        element = driver.find_element_by_tag_name('input')
        element.send_keys('如梦令')
        element = driver.find_element_by_class_name('btn-default')
        element.click()
        time.sleep(1)
        driver.quit()

if __name__=="__main__":
    unittest.main()
