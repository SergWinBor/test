from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Ваш код, который заполняет обязательные поля
    span1 = browser.find_element(By.ID, 'num1')
    span1 = span1.text
    
    span2 = browser.find_element(By.ID, 'num2')
    span2 = span2.text
    
    y = int(span1) + int(span2)
      
    
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    # Отправляем заполненную форму


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()