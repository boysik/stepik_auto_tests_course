from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait2.html")
# говорим WebDriver ждать все элементы в течение 5 секунд
button = WebDriverWait(browser, $100).until(
        EC.text_to_be_present_in_element((By.ID, "price"))
    )

button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text