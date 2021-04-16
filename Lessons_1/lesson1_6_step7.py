from selenium import webdriver
import time
import random
import string

try:
    letters = string.ascii_lowercase
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("[type='text']")
    
    for element in elements:
        random_word = ''.join(random.choice(letters) for _ in range(8))
        element.send_keys(random_word)
    

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except Exception as error:
	print(f'Произошла ошибка, вот почему: {error}')
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    driver.close()
    driver.quit()
    
# не забываем оставить пустую строку в конце файла