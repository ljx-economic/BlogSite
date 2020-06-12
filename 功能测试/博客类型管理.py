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
    
    def test_2(self):# 增加博客类型
        driver.get('http://49.235.199.52/blog/blog_type/add/')
        element = driver.find_element_by_id('id_blog_type')
        element.send_keys('自动化测试')
        element = driver.find_element_by_class_name('btn-primary')
        element.click()
        time.sleep(1)
    
    def test_3(self):# 修改博客类型
        driver.get('http://49.235.199.52/blog/blog_type/change/14')
        element = driver.find_element_by_id('id_blog_type')
        element.send_keys('修改自动化测试')
        element = driver.find_element_by_class_name('btn-primary')
        element.click()
        time.sleep(1)

    def test_4(self):# 删除博客类型
        driver.get('http://49.235.199.52/blog/blog_type/change/14')
        element = driver.find_element_by_class_name('btn-danger')
        element.click()
        time.sleep(1)   
        driver.quit()
        
if __name__=="__main__":
    unittest.main()
