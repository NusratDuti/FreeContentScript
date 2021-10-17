from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\webdriver\chromedriver.exe')
driver.get('https://bongobd.com')

#content with ad
#Clicking on movies from menu
FindMovies = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/header/div/div/div[2]/div[1]/a[1]/div/span')
FindMovies.click()

#Content is getting played automatically after the ad
ContentClick = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div/div[4]/div/div[2]/div/div/div[2]/div/div[1]/div/a/div/div/div')
ContentClick.click()
