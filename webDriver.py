import time
from selenium import webdriver

def getReservationPageSources():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.implicitly_wait(3)    
    driver.get('https://kirbycafe-reserve.com/guest/tokyo/reserve/')

    time.sleep(3)

    button = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[2]/button/span')
    button.click()

    time.sleep(3)

    button = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]')
    button.click()

    time.sleep(3)

    button = driver.find_element_by_xpath('//*[@id="list-35"]/div[2]')
    button.click()
    
    time.sleep(3)
    
    page_sources = []
    this_month_page_source = driver.page_source
    page_sources.append(this_month_page_source)

    button = driver.find_element_by_xpath('//*[@id="step2"]/div[2]/div[1]/button[2]')
    button.click()
    
    time.sleep(3)

    next_month_page_source = driver.page_source
    page_sources.append(next_month_page_source)

    return page_sources