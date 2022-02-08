#Задание: ждем нужный текст на странице
#Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#Нажать на кнопку "Book"
#Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), str("$100"))
        )
    browser.find_element_by_css_selector("#book").click()
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector("#solve").click()  
    
finally :
    time.sleep(10)
    browser.quit()    