# Instalar " pip install mysql-connector-python "
import threading

import mysql.connector

'''importar a biblioteca selenium'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# CONEXÃO COM O WHATSAPP
def conexao():
    '''ESPERA ATE COM QUE O ELEMENTO SIDE SEJA ENCONTRADO NA TELA'''
    while (len(driver.find_elements(By.ID, 'side')) < 1):
        time.sleep(1)  # "padrão 1"
    else:
        print('QR-COD ABERTO')
        time.sleep(1)  # "padrão 2"


def main():
    while (1):
        # PEGA AS NOVAS MENSAGENS
        '''BUSCA NOVAS MENSAGENS  '''
        bolinha_notificacao = driver.find_elements(By.CLASS_NAME, '_1pJ9J')
        '''CONFERE A QUANTIDADE DE MENSAGEM'''
        quantidade_bolinha_notificacao = len(bolinha_notificacao)
        if quantidade_bolinha_notificacao > 0:
            time.sleep(1)
            for bolinhas_encontrada in bolinha_notificacao:
                time.sleep(1)
                # MENSAGEM ENCONTRADA CLICAR
                bolinhas_encontrada.click()
                element2 = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]')
                element2.send_keys(Keys.ESCAPE)
                time.sleep(2)
#================================================================================

if __name__ == "__main__":
    site = "https://web.whatsapp.com"
    driver = webdriver.Chrome()
    driver.get(site)
    conexao()
    main()






