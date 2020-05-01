from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#input_xpath = raw_input
#findElement = 'driver.find_element_by_xpath('inputXpath')'

class ChromeConfig():
    def chromeDriver():
        EXE_PATH = r'C:\automation_ui\flask_app\flaskbot\automation\drivers\chromedriver.exe'
        chrome = webdriver.Chrome(executable_path=EXE_PATH)
        chrome.get('https://google.com')
        teststring = "CAN YOU SEE THIS AUZ"

class Automate(ChromeConfig):
    def runCSS(id, value, act, chrome): #find navigate click sendkeys
        if act == 'Navigate':
            action_var = "driver.get(input_string)"
        else:# action == 'Click':
            #print(stringt)
            element = chrome.find_element_by_css_selector(id).send_keys(value)


    def run(action, element_type, element_id, input_string, chrome):#first if will be navigate
        if element_type == "css":
            Automate.runCSS(element_id, input_string, action, chrome)
        else:# element_type == "xpath":
            runXPATH(element_id, input_string)

    """    driver_string = "driver." + selector_var + element_id + '")' + action_var
        print("READING THIS HERE!!!!!!! " + driver_string + input_string)


        #time.sleep(5)
        #element = driver.find_element_by_xpath(element_id)#"//*[@id=\"tsf\"]/div[2]/div[1]/div[1]/div/div[2]/input"
        #element_id = "//*[@id=\"tsf\"]/div[2]/div[1]/div[1]/div/div[2]/input"
        #element_id = "#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input"
        time.sleep(3)
        element = driver.find_element_by_css_selector(element_id).send_keys(input_string)#"//*[@id=\"tsf\"]/div[2]/div[1]/div[1]/div/div[2]/input"
        #element = driver.execute_script(driver_string)
        #element = driver.execute_script(driver.find_element_by_css_selector(element_id).send_keys(input_string))
        #element = driver_string
        time.sleep(5)
        #element.send_keys(input_string)"""
