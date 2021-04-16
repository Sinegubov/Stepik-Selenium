from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 

link = "http://suninjuly.github.io/math.html"
    

try:

    browser = webdriver.Chrome(executable_path=r'/home/sinegubov/environments/chromedriver')
    browser.get(link)

#except ONE:

    people_radio = browser.find_element_by_id("peopleRule")
    
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    #assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"

#except TWO:

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

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
