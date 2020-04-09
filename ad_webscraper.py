from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from settings import (
    AD_USER,
    AD_PWD,
    SELENIUM_DL_SETTINGS
)
from time import sleep
options = Options()
options.add_experimental_option("prefs", SELENIUM_DL_SETTINGS)

counter = 1
url = 'https://member.assessmentday.com/member/member-area/'

chrm = webdriver.Chrome(options=options)

chrm.get(url)
chrm.find_element_by_id("amember-login").send_keys(AD_USER)
chrm.find_element_by_id("amember-pass").send_keys(AD_PWD)
chrm.find_element_by_id("remember_login").click()
chrm.find_element_by_xpath('//*[@id="am-login-form"]/fieldset/div[4]/div/input').click()

sleep(30)

while True:
    download_url = f'https://member.assessmentday.com/member/content/f/id/{counter}/'
    chrm.get(download_url)
    counter+=1
    sleep(1)

    if counter %% 100 == 0:
        print(f'Step: {counter}')

    if counter == 489:
        print(f'End of Scrape.')
        chrm.close()
        break



