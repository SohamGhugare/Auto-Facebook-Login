from selenium import webdriver

username = USERNAME
password = PASSWORD

driver = webdriver.Chrome('Your chrome driver path !')
driver.get('https://facebook.com')

userTextbox = driver.find_element_by_id('email')
userTextbox.send_keys(username)

passTextbox = driver.find_element_by_id('pass')
passTextbox.send_keys(password)

submit = driver.find_element_by_id('u_0_b')
submit.click()