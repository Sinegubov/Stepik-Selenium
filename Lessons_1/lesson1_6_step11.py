from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    input1 = browser.find_element_by_css_selector(".first_block .first")
    input1.send_keys("Жирослав")
    input2 = browser.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Йовович")
    input3 = browser.find_element_by_css_selector(".first_block .third")
    input3.send_keys("elonmusk@gmail.com")
    input4 = browser.find_element_by_css_selector(".second_block .first")
    input4.send_keys("88005553535")
    input4 = browser.find_element_by_css_selector(".second_block .second")
    input4.send_keys("Pushkino, Kolotushkino")
       

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
