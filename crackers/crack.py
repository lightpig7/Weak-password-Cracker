import csv  # 导入CSV模块，用于读写CSV文件
import time  # 导入time模块，用于计时

from selenium import webdriver  # 导入selenium的webdriver模块，用于驱动浏览器
from selenium.webdriver.common.by import By  # 导入By类，用于指定元素定位方式
from selenium.webdriver.support import expected_conditions as EC  # 导入expected_conditions模块，用于设置条件等待
from selenium.webdriver.support.wait import WebDriverWait  #

start_time = time.time()  # 记录开始时间名列表建CSV写入对象
browser = webdriver.Chrome()  # 创建Chrome浏览器驱动对象
url = 'https://csab.zju.edu.cn/login'  # 豆瓣电影Top250的URL
browser.get(url)  # 打开指定URL
button = browser.find_elements(By.CSS_SELECTOR, '.ivu-btn-primary')  # 查找页码元素
unput = browser.find_elements(By.CSS_SELECTOR, '.ivu-input-default')
if __name__ == '__main__':
    with open('Password-Top1000（1010）.txt') as f:
        username= unput[0].send_keys('123')
        password=unput[1].send_keys('234')
        button[0].click()
        # imformation = browser.page_source
        alert = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ivu-message-error span')))
        alert_text = alert[0]
        print("Alert Text:", alert_text)
        time.sleep(5)
        # 处理警告框（点击确认按钮）
        alert.accept()  # 点击确认按钮


        if '错误' not in alert_text:
            pass
