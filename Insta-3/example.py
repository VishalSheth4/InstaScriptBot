from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
driver.get('https://www.instagram.com/accounts/login/')
# driver.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
driver.email = 'life_explorer_4'
driver.password = 'tigerF1sh00'
driver.username = 'natgeotravellerindia'
time.sleep(10)
try:
    emailInput=driver.find_element_by_xpath("//input[@name = 'username']")
    passwordInput=driver.find_element_by_xpath("//input[@name = 'password']")
except (NoSuchElementException, ElementNotVisibleException) as exceptions:
    pass
emailInput.send_keys(driver.email)
passwordInput.send_keys(driver.password)
passwordInput.send_keys(Keys.ENTER)
time.sleep(10)

# ---pop up handle---
NotNow=driver.find_element_by_xpath("//button[text() = 'Not Now']").click()
time.sleep(10)
driver.get('https://www.instagram.com/' + driver.username + '/')
time.sleep(5)
driver.get('https://www.instagram.com/' + driver.username + '/followers/')
Followers=driver.find_element_by_xpath("//a[@class='-nal3 ']").click()
time.sleep(5)
# ------------------------
# ------------------------
#find all li elements in list
fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
scroll = 0
for j in (1,100):
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(10)
for k in (1,10):
    driver.execute_script('arguments[0].scrollDown = arguments[0].scrollDown + arguments[0].offsetHeight;', fBody)
    time.sleep(10)


while scroll < 500: # scroll 500 times
    for i in (0,4):
        try:
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            Follow=driver.find_element_by_xpath("//button[text() = 'Follow']").click()
            time.sleep(10)
        except (NoSuchElementException, ElementNotVisibleException) as exceptions:
        	pass
    time.sleep(8)
    # driver.executeScript("window.scrollBy(0,100)")
    scroll += 1
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(2)


# fList  = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
# print("fList len is {}".format(len(fList)))
# print("ended")    