from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#input_xpath = raw_input
#findElement = 'driver.find_element_by_xpath('inputXpath')'

EXE_PATH = r'C:\automation_ui\flask_app\flaskbot\automation\drivers\chromedriver.exe'
driver = webdriver.Chrome(executable_path=EXE_PATH)
driver.get('https://google.com')
element = driver.find_element_by_xpath("//*[@id=\"tsf\"]/div[2]/div[1]/div[1]/div/div[2]/input")
element.send_keys("Hey Mom and dad")

"""def action():
    if input_action == 'Navigate':
        input_url == raw_input #Element Field
    else input_action == 'Click':
        input_element == raw_input #Element Field

def selector():
    if input_selector == "css":
        find_css == raw_input
    else if input_selector == "xpath":
        find_xpath == raw_input
    else:
        find_html = raw_input

 def enable_input():
     if input_action  == "Input":
         #Enable input field"""
