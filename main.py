# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import sys


#selenium初期設定
driver_path = '/app/.chromedriver/bin/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options = options, executable_path = driver_path)
driver.get('https://w5.linguaporta.jp/user/seibido/index.php')


def login():
    try:
        usrname = '#content-login > form > table > tbody > tr:nth-child(1) > td > input[type=text]'
        element = driver.find_element_by_css_selector(usrname)
        usr = input('Enter your name: ')
        element.send_keys(usr)
        password = '#content-login > form > table > tbody > tr:nth-child(2) > td > input[type=password]'
        element = driver.find_element_by_css_selector(password)
        pass_word = input('Enter your password: ')
        element.send_keys(pass_word)
        login_bt = '#btn-login'
        element = driver.find_element_by_css_selector(login_bt)
        sleep(1)
        element.click()
        sleep(2)
        study = '#menu2 > dl > dt:nth-child(3) > form > a'
        element = driver.find_element_by_css_selector(study)
        element.click()
        sleep(2)
    except:
        pass
    else:
        raise ValueError('Invalid password or username')

def select_unit():
    a


if __name__ == '__main__':
    for i in range(0, 3):
        try:
            login()
        except:
            if i == 2:
                print ('ミスしすぎです、プログラムが停止しました。')
                driver.quit()
                sys.exit()
            else:
                print('ログインに失敗しました、再度ログインし直してください。')
        else:
            break