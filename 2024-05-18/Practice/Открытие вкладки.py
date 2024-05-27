from selenium import webdriver
from selenium.webdriver.chrome.options import Options
o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)
driver.get('https://m.vksit.ru/mod/assign/view.php?id=14188&forceview=1')