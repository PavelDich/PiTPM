Задание не может быть строго выполнена по предложенному варианту на сайте т.к версия библеотки предложенная там устарела на 2 года и некоторые решения категорически отличаються. 
Например:

driver.find_element_by_id("password") 
driver.find_element(By.XPATH, "password")
=>
driver.find_element("id","password")

chrome_options = Options()
=>
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)