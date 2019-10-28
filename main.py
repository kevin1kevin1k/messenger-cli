import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

browser_name = 'Chrome'
driver_path = '/Users/KevinLee/Downloads/chromedriver'

# Log in
browser = getattr(webdriver, browser_name)
options = Options()
options.headless = True
driver = browser(executable_path=driver_path, chrome_options=options)
driver.get('https://messenger.com')
email = input('Email: ')
password = getpass.getpass()
print('Logging in (this may take a while)')
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()

# Get list of recent chats
divs = driver.find_elements_by_xpath("//div[@data-tooltip-alignh='center']")
for i, div in enumerate(divs):
    print(i, '\t', div.get_attribute('data-tooltip-content'))
who = int(input('Select who to send message: '))
divs[who].click()

# Send message
msg = input('Message: ').strip()
div = driver.find_element_by_xpath("//div[@aria-label='New message']")
div.find_element_by_xpath(".//br[@data-text='true']").send_keys(msg[0])
div.find_element_by_xpath(".//span[@data-text='true']").send_keys(msg[1:])
div.find_element_by_xpath(".//span[@data-text='true']").send_keys(Keys.RETURN)
