# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import sys


#selenium初期設定
driver_path = '/usr/bin/chromedriver'
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
        cocet = '#content-study > form > div > div:nth-child(2) > div.table-resp-col.study-col-button > input'
        element = driver.find_element_by_css_selector(cocet)
        element.click()
        sleep(2)
    except:
        pass
    else:
        raise ValueError('Invalid password or username')

def select_unit(unitnumber):
    unitnumber = (unitnumber - 1) / 25 + 1
    unit = "select_unit('drill', '" + str(1813 + (unitnumber - 1) * 4) + "', '');"
    try:
        driver.execute_script(unit)
        sleep(2)
        driver.save_screenshot('jikken.png')
    except:
        driver.quit()
        sys.exit()


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
    while True:
        unitnumber = input('ユニットの最初の数字を入力してください: ')
        if unitnumber % 25 == 1:
            break
        else:
            print('数字が違うぞもう一回入力してください。')
    select_unit(unitnumber)