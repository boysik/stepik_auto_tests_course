from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим WebDriver ждать цены в 100$
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element(By.ID, "book").click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    # Находим элемент x и присваиваем его переменной
    x_element = browser.find_element(By.ID, "input_value")
    #x_element_value = x_element.get_attribute("valuex")
    x = x_element.text
    y = calc(x)
    
    # Находим текстовое поле и помещаем в него значение Х
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    