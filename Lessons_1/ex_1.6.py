from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//div[1]/div[1]/input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//div[1]/div[2]/input')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//div[1]/div[3]/input')
    input3.send_keys("aaa@323432.com")

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    time.sleep(1)

    welcome_text_etl = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_etl.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()