from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import math
import time 

link = "http://suninjuly.github.io/selects1.html"
    

try:

    browser = webdriver.Chrome(executable_path=r'/home/sinegubov/environments/chromedriver')
    browser.get(link)
    
    NUM1 = browser.find_element_by_id("num1")
    x = NUM1.text

    NUM2 = browser.find_element_by_id("num2")
    y = NUM2.text

    z = int(x) + int(y)

    ZZ = str(z)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(ZZ)

    button = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    button.click()



except Exception as error:
	print(f'Произошла ошибка, вот почему: {error}')
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    #driver.close()
    #driver.quit()
    
# не забываем оставить пустую строку в конце файла