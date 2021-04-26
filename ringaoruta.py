from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');

driver = webdriver.Chrome(executable_path='D:\Webdriver\chromedriver.exe' ,chrome_options=options)

url ='https://w5.linguaporta.jp/user/seibido/'
driver.get(url)

username = '#content-login > form > table > tbody > tr:nth-child(1) > td > input[type=text]'
element = driver.find_element_by_css_selector(username)

element.send_keys('r02i16')

password = '#content-login > form > table > tbody > tr:nth-child(2) > td > input[type=password]'
element = driver.find_element_by_css_selector(password)

element.send_keys('1UY57vrt')

login = '#btn-login'
element = driver.find_element_by_css_selector(login)
element.click()

study_login = '#menu2 > dl > dt:nth-child(3) > form > a'
element =  driver.find_element_by_css_selector(study_login)
element.click()

unit_login = '#content-study > form > div > div:nth-child(2) > div.table-resp-col.study-col-button > input'
element = driver.find_element_by_css_selector(unit_login)
element.click()

items = driver.find_elements_by_class_name("table-resp-row")
for item in items:
    score = item.find_element_by_class_name("col-points")
    print(score.text)
    if score.text != "25点/25点満点" and score.text !="得点":
        element = item.find_element_by_css_selector('#content-study > div.table-resp.table-unit-list > div:nth-child(9) > div.table-resp-col.col-unitname > div > inputs')
        element.click()
    #if score.text != "25点/25点満点" and score.text !="得点":
        #driver.implicitly_wait(2)
        #element = item.find_element_by_class_name("col-study")
        #loc = element.location
        #x, y = loc['x'], loc['y']
        #actions = ActionChains(driver)
        #actions.move_by_offset(x, y)
        #actions.click()
        #actions.perform()
