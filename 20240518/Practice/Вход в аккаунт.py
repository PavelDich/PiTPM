from selenium import webdriver
from selenium.webdriver.chrome.options import Options

username = "isp-22a-9"
password = "https://www.youtube.com/watch?v=oHg5SJYRHA0&ab_channel=cotter548"

o = Options()
o.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=o)
driver.implicitly_wait(10)

driver.get('https://m.vksit.ru/login/index.php')
driver.set_window_size(1920, 1080)
while True:
    try:
        element_username = driver.find_element("id", "username")
        element_username.clear()
        element_username.send_keys(username)
        element_password = driver.find_element("id", "password")
        element_password.clear()
        element_password.send_keys(password)
        element_loginbtn = driver.find_element("id", "loginbtn")
        element_loginbtn.click()
        break
    except:
        driver.implicitly_wait(10)
        print("Wait")
