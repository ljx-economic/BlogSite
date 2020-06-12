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
    def test_1(self):# 登录
        driver.get('http://49.235.199.52/')
        element = driver.find_element_by_id('id_username')
        element.send_keys('Joker')
        element = driver.find_element_by_id('id_password')
        element.send_keys('Joker123456')
        element = driver.find_element_by_id('btn-login')
        element.click()
        time.sleep(1)
    
    def test_2(self):# 新建收藏夹
        driver.get('http://49.235.199.52/star/add/')
        element = driver.find_element_by_id('id_star')
        element.send_keys('Django')
        element = driver.find_element_by_id('id_brief')
        element.send_keys('Web框架,python语言开发')
        element = driver.find_element_by_class_name('btn-primary')
        element.click()
        time.sleep(1)

    def test_3(self):# 修改收藏夹
        driver.get('http://49.235.199.52/star/change/8')
        element = driver.find_element_by_class_name('btn-primary')
        element.click()
        time.sleep(1)

    def test_4(self):# 删除收藏夹
        driver.get('http://49.235.199.52/star/manage/')
        driver.get('http://49.235.199.52/star/delete/8')
        time.sleep(1)   
        driver.quit()
        
if __name__=="__main__":
    unittest.main()
