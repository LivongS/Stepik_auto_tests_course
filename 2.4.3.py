from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


import time

try:    
  browser = webdriver.Chrome(ChromeDriverManager().install())
  browser.implicitly_wait(5)
  browser.get("http://suninjuly.github.io/wait1.html")
  browser.find_element_by_css_selector ("#verify").click()
  message = browser.find_element_by_css_selector("#verify_message")
  assert "successful" in message.text
finally:

  time.sleep(5)
  browser.quit()