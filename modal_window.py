from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Находим кнопку и нажимаеем на нее.
    magical_button = browser.find_element(By.CSS_SELECTOR, ".btn").click()
    
    #Переключаемся на модальное окно и жмем окей
    confurm = browser.switch_to.alert.accept()
    
    # Высчитываем значение Х
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
    