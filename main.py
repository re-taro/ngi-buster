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


#接続
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

#ユニットを選ぶ
def select_unit(unitnumber):
    unitnumber = (unitnumber - 1) / 25 + 1
    unit = "select_unit('drill', '" + str(1813 + (unitnumber - 1) * 4) + "', '');"
    try:
        driver.execute_script(unit)
        sleep(2)
    except:
        driver.quit()
        sys.exit()

#翻訳して答えを返す
def ans_trans(ans, ques):
    driver.execute_script("window.open()")
    sleep(1)
    driver.switch_to_window(driver.window_handles[1])
    driver.get('https://translate.google.co.jp/?hl=ja&sl=en&tl=ja&op=translate')
    sl_en = '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea'
    element = driver.find_element_by_css_selector(sl_en)
    element.send_keys(ques.text)
    sleep(1)
    tl_jp = '#ow634 > div.J0lOec > span.VIiyi > span > span'
    guess = driver.find_element_by_css_selector(tl_jp).text
    driver.save_screenshot('jikken.png')#test
    driver.switch_to_window(driver.window_handles[0])
    for i, answer in enumerate(ans):
        ans_text = answer.get_attribute('value')
        if ans_text in guess or guess in ans_text:
            return i
    return -1

#記憶機能の作成
def mk_memo(ans, ques, memo):
    for answer in ans:
        memo.setdefault(ques.text, []).append(answer.get_attribute('value'))
    return memo

#記録する処理
def update_memo(ans, ques, memo):
    tmp = []
    for answer in ans:
        ans_text = answer.get_attribute('value')
        if ans_text in memo[ques.text]:
            tmp.append(ans_text)
    memo[ques.text] = tmp
    return memo

#memoから回答する
def ans_memo(ans, ques, memo):
    for i, answer in enumerate(ans):
        ans_text = answer.get_attribute('value')
        if ans_text in memo[ques.text]:
            return i

#回答する
def Answer():
    while True:
        sleep(2)
        try:
            question = '#qu02'
            ques = driver.find_element_by_css_selector(question)
        except:
            print('このユニットは既に完了しています。')
            break
        ans = []
        ans_0 = '#answer_0_0'
        ans.append(driver.find_element_by_css_selector(ans_0))
        ans_1 = '#answer_0_1'
        ans.append(driver.find_element_by_css_selector(ans_1))
        ans_2 = '#answer_0_2'
        ans.append(driver.find_element_by_css_selector(ans_2))
        ans_3 = '#answer_0_3'
        ans.append(driver.find_element_by_css_selector(ans_3))
        ans_4 = '#answer_0_4'
        ans.append(driver.find_element_by_css_selector(ans_4))
        choose = ans_trans(ans, ques)
        if choose == -1:
            ans[0].click()
        else:
            ans[choose].click()
        submit = '#under_area > form > input.btn.btn-problem-next.form_font_size'
        driver.find_element_by_css_selector(submit).submit()
        sleep(2)
        try:
            true_msg = '#true_msg'
            driver.find_element_by_css_selector(true_msg)
            print('正解')
        except:
            print('不正解')
        try:
            next_btn = '#under_area > form > input.btn.btn-problem-next.form_font_size'
            driver.find_element_by_css_selector(next_btn)
        except:
            break



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
                pass
        else:
            break
    while True:
        unitnumber = int(input('ユニットの最初の番号を入力してください: '))
        if unitnumber % 25 == 1:
            break
        else:
            print('番号が違うぞもう一回入力してください。')
    while True:
        end_unitnumber = int (input('終了する番号を入力してください: '))
        if end_unitnumber % 25 == 0:
            break
        else:
            print('番号が違うぞもう一回入力してください。')
    while True:
        print('現在のユニット: ', str(unitnumber) + '-' + str(unitnumber + 24))
        select_unit(unitnumber)
        Answer()
        if unitnumber >= (end_unitnumber - 24):
            break
        unitnumber += 25
    print('回答が終わりました。プログラムを終了します。')
    driver.quit()
    sys.exit()