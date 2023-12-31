from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Ваш код, который заполняет обязательные поля
    span1 = browser.find_element(By.ID, 'input_value')
    span1 = span1.text

    x = calc(int(span1))
    
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(x)

    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    # Отправляем заполненную форму


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()