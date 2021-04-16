from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

link = "http://suninjuly.github.io/wait2.html"

try:

    browser = webdriver.Chrome(executable_path=r'/home/sinegubov/environments/chromedriver')
    
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "price"), "$100")
    )
    button.click()
    #message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
    
except Exception as error:
	print(f'Произошла ошибка, вот почему: {error}')
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    #driver.close()
    #driver.quit()
    
# не забываем оставить пустую строку в конце файла
