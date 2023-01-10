import time
from selenium.webdriver.common.keys import Keys
import main


class Mensagens():
    def __init__(self):
        pass

    def
    def primeirca_msg(self):
        campo_texto = main.navegador.driver.find_elements(By.)
        campo_texto.click()
        time.sleep(3)
        campo_texto.send_keys("primeira msg", Keys.ENTER)
        self.esc(driver)

    def segunda_msg(self, driver):
        campo_texto = driver
        campo_texto.click()
        time.sleep(3)
        campo_texto.send_keys("segunda mensagem", Keys.ENTER)
        self.esc(driver)

    def esc(self, driver):
        element = driver
        print('voltando')
        element.send_keys(Keys.ESCAPE)
        time.sleep(3)

mensagem=Mensagens()




