from selenium.common.exceptions import TimeoutException

from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\webdriver\chromedriver.exe')
driver.get('https://bongobd.com')

FreeContentClick = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div/div[5]/div/div[2]/div/div/div[2]/div/div[1]/div/a/div/div/div')
FreeContentClick.click()
