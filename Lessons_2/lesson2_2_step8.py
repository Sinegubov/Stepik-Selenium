from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 
import math
import os 

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')     

try:
    
    browser = webdriver.Chrome(executable_path=r'/home/sinegubov/environments/chromedriver')
    browser.get(link)

    input1 = browser.find_element_by_xpath("//input[@class='form-control']")
    input1.send_keys("Pavel")

    input2 = browser.find_element_by_xpath("(//input[@class='form-control'])[2]")
    input2.send_keys("Sinegubov")

    input3 = browser.find_element_by_xpath("(//input[@class='form-control'])[3]")
    input3.send_keys("sineguboff@gmail.com")

    element = browser.find_element_by_css_selector ("input#file")
    element.send_keys(file_path)

    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
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






#current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
#file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
#element.send_keys(file_path)

#print(os.path.abspath(__file__))

#print(os.path.abspath(os.path.dirname(__file__)))