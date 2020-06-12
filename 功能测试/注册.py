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
    def test_1(self):# 用户名输入不规范
        driver.get('http://49.235.199.52/user/register/')
        element = driver.find_element_by_id('id_username')
        element.send_keys('Jo')
        element = driver.find_element_by_id('id_email')
        element.send_keys('13579@qq.com')
        element = driver.find_element_by_id('id_password')
        element.send_keys('123456')
        element = driver.find_element_by_id('id_password_again')
        element.send_keys('123456')
        element = driver.find_element_by_class_name('btn-danger')
        element.click()
        time.sleep(1)

    def test_2(self):# 邮箱格式不规范
        driver.get('http://49.235.199.52/user/register/')
        element = driver.find_element_by_id('id_username')
        element.send_keys('user_test')
        element = driver.find_element_by_id('id_email')
        element.send_keys('13579qq.com')
        element = driver.find_element_by_id('id_password')
        element.send_keys('123456')
        element = driver.find_element_by_id('id_password_again')
        element.send_keys('123456')
        element = driver.find_element_by_class_name('btn-danger')
        element.click()
        time.sleep(1)
        
    def test_3(self):# 密码少于6位
        driver.get('http://49.235.199.52/user/register/')
        element = driver.find_element_by_id('id_username')
        element.send_keys('user_test')
        element = driver.find_element_by_id('id_email')
        element.send_keys('13579@qq.com')
        element = driver.find_element_by_id('id_password')
        element.send_keys('12345')
        element = driver.find_element_by_id('id_password_again')
        element.send_keys('12345')
        element = driver.find_element_by_class_name('btn-danger')
        element.click()
        time.sleep(1)
        
    def test_4(self):# 两次密码输入不一致
        driver.get('http://49.235.199.52/user/register/')
        element = driver.find_element_by_id('id_username')
        element.send_keys('user_test')
        element = driver.find_element_by_id('id_email')
        element.send_keys('13579@qq.com')
        element = driver.find_element_by_id('id_password')
        element.send_keys('123456')
        element = driver.find_element_by_id('id_password_again')
        element.send_keys('1234567')
        element = driver.find_element_by_class_name('btn-danger')
        element.click()
        time.sleep(1)
        
    def test_5(self):# 用户名已存在
        driver.get('http://49.235.199.52/user/register/')
        element = driver.find_element_by_id('id_username')
        element.send_keys('Joker')
        element = driver.find_element_by_id('id_email')
        element.send_keys('13579@qq.com')
        element = driver.find_element_by_id('id_password')
        element.send_keys('123456')
        element = driver.find_element_by_id('id_password_again')
        element.send_keys('123456')
        element = driver.find_element_by_class_name('btn-danger')
        element.click()
        time.sleep(1)

    def test_6(self):# 邮箱已存在
        driver.get('http://49.235.199.52/user/register/')
        element = driver.find_element_by_id('id_username')
        element.send_keys('user_test')
        element = driver.find_element_by_id('id_email')
        element.send_keys('15826774141@163.com')
        element = driver.find_element_by_id('id_password')
        element.send_keys('123456')
        element = driver.find_element_by_id('id_password_again')
        element.send_keys('123456')
        element = driver.find_element_by_class_name('btn-danger')
        element.click()
        time.sleep(1)

    def test_7(self):# 注册成功
        driver.get('http://49.235.199.52/user/register/')
        element = driver.find_element_by_id('id_username')
        element.send_keys('user_test')
        element = driver.find_element_by_id('id_email')
        element.send_keys('13579@qq.com')
        element = driver.find_element_by_id('id_password')
        element.send_keys('123456')
        element = driver.find_element_by_id('id_password_again')
        element.send_keys('123456')
        element = driver.find_element_by_class_name('btn-danger')
        element.click()
        time.sleep(1)
        driver.quit()
        
if __name__=="__main__":
    unittest.main()
