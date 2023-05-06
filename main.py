import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

edge_driver = '/home/khem/environments/edgedriver_linux64/'
options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Edge(options=options, service=Service(executable_path=edge_driver))
driver.get('https://tinder.com/')
# driver.maximize_window()

base_win = driver.window_handles[0]

time.sleep(2)
accept = driver.find_element(By.XPATH, '//*[@id="s-407411262"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
accept.click()

log_in = driver.find_element(By.XPATH,
                             '//*[@id="s-407411262"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in.click()

time.sleep(5)

more_option = driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div[1]/div/div/div[3]/span/button')
more_option.click()

time.sleep(5)
fb_option = driver.find_element(By.XPATH,
                                '//*[@id="s-2135792338"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_option.click()

time.sleep(5)
fb_win = driver.window_handles[1]
driver.switch_to.window(fb_win)
time.sleep(3)
email = driver.find_element(By.NAME, 'email')
email.send_keys(YOUR USERNAME/NUMBER)

password = driver.find_element(By.NAME, 'pass')
password.send_keys(YOUR PASSWORD, Keys.ENTER)

driver.switch_to.window(base_win)

time.sleep(10)
location_per = driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
location_per.click()

time.sleep(2)
notification = driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div/div[3]/button[2]')
notification.click()

time.sleep(20)

for i in range(100):
    like = driver.find_element(By.XPATH,
                               '//*[@id="s-407411262"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
    like.click()
    time.sleep(3)
driver.quit()
