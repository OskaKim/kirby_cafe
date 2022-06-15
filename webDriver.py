import time
from selenium import webdriver

def getReservationPageSource():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.implicitly_wait(3)    
    driver.get('https://kirbycafe-reserve.com/guest/tokyo/reserve/')

    time.sleep(3)

    start_button = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[2]/button/span')
    start_button.click()

    time.sleep(3)

    start_button = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]')
    start_button.click()

    time.sleep(3)

    start_button = driver.find_element_by_xpath('//*[@id="list-35"]/div[2]')
    start_button.click()
    
    time.sleep(3)

    return driver.page_source