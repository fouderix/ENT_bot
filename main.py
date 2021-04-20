from selenium import webdriver
from time import sleep
import os

driver = webdriver.Firefox(executable_path="geckodriver.exe")

def while_connect_ent():
    while True:
        try:
            sleep(3)
            driver.get("https://michelet.ecollege.haute-garonne.fr/")
            connect_button = driver.find_element_by_css_selector(".fo-connect__link")
            connect_button.click()
            user_eleve = driver.find_element_by_css_selector(".form__label")
            user_eleve.click()
            valider_button = driver.find_element_by_css_selector("#button-submit")
            valider_button.click()
            username = driver.find_element_by_css_selector("#username")
            username.send_keys("identifiant")
            password = driver.find_element_by_css_selector("#password")
            password.send_keys("password")
            valider_button2 = driver.find_element_by_css_selector("#button-submit")
            valider_button2.click()
        except:
            try:
                verify_connected = driver.find_element_by_css_selector("ul.user")
                print("connecté")
                os._exit()
                return
            except:
                try:
                    indispo = driver.find_element_by_css_selector("div.msg--error")
                    while_connect_ent()
                except:
                    print("bug")
                    os._exit()

if __name__ == "__main__":
    while_connect_ent()
