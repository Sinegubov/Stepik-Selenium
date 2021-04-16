from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    browser = webdriver.Chrome(executable_path=r'/home/sinegubov/environments/chromedriver')
    #browser.implicitly_wait(12)
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"$100")
    )
    button = browser.find_element_by_id("book")
    button.click()
    
    NUM = browser.find_element_by_css_selector("span#input_value")
    x = NUM.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(y)
    
    button = browser.find_element_by_id("solve")
    button.click()
    
    
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
