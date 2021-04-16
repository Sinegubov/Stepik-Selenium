from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 
import math

link = "https://suninjuly.github.io/math.html"
    

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    browser = webdriver.Chrome(executable_path=r'/home/sinegubov/environments/chromedriver')
    browser.get(link)
     
    NUM = browser.find_element_by_css_selector("span#input_value")
    x = NUM.text
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(y)
    checkbox = browser.find_element_by_css_selector("input#robotCheckbox")
    checkbox.click()
    button2 = browser.find_element_by_css_selector("input#robotsRule")
    button2.click()
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
