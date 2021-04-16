from selenium import webdriver
browser = webdriver.Chrome(executable_path=r'/home/sinegubov/environments/chromedriver')

#browser.execute_script("alert('Robots at work');")

#browser.execute_script("document.title='AAAAaaarrrrgh';alert('Robots at work');")


link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()