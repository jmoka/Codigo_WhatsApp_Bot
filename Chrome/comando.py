'''importar a biblioteca selenium'''
import ssl

import mouseinfo
from selenium import webdriver
import time
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Navegador:
    ''''MÉTODO CONSTRUTOR'''

    def __init__(self, site, tempo, driver, bolinha_notificacao): # ATRIBUTOS
        self.site=site
        self.tempo=tempo
        self.driver=driver
        self.bolinha_notificacao=bolinha_notificacao




        self.driver.get(self.site)

        while(len(driver.find_elements(By.ID, 'side')) < 1) :
                time.sleep(self.tempo)
                print('BUSCANDO NOVAS MENSAGENS')
        else:
            print('O ELEMENTO EXISTE, VAMOS PROCURAR QUANTOS TEM!')
            time.sleep(self.tempo)
            self.buscando_bolinha_notificacao()

    def buscando_bolinha_notificacao(self):
        while(1):
            quantidade_bolinha_notificacao=len(self.bolinha_notificacao)
            time.sleep(self.tempo)
            print('QUANTIDADE ENCONTRADA DE BOLINHAS_NOTIFICAÇÃO: ', quantidade_bolinha_notificacao)
            if quantidade_bolinha_notificacao>0:
                print('VOU ABRIR A MENSAGEM')
                for bolinhas_encontrada in self.bolinha_notificacao:
                    time.sleep(self.tempo)
                    bolinhas_encontrada.click()
                    time.sleep(self.tempo)

                else:
                    self.pegando_titulo()

    def buscando_bolinha_notificacao1(self):
        print('PROCURANDO POR NOVAS MENSAGENS')
        time.sleep(self.tempo)
        self.buscando_bolinha_notificacao()

    def pegando_titulo(self):
        t = driver.find_element(By.CLASS_NAME, '_21nHd')
        time.sleep(2)
        self.titulo=t.text.title()
        print('PEGUEI O TÍTULO:', self.titulo)
        t.click()
        time.sleep(2)
        self.pegando_numero()


    def pegar_nome_conta(self):
        n=driver.find_element(By.CSS_SELECTOR,'span[class="l7jjieqr cw3vfol9 i0jNr selectable-text copyable-text"]')
        time.sleep(self.tempo)
        self.nome_conta=n.text
        print('PEGUEI O NOME: ', self.nome_conta)
        self.imprimir()
    def pegar_nome_conta_comercial(self):
        n=driver.find_element(By.XPATH,'//span[@class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 cw3vfol9 i0jNr selectable-text copyable-text"]')
        time.sleep(self.tempo)
        self.nome_conta_comercial=n.text
        print('PEGUEI O NOME COMERCIAL', self.nome_conta_comercial)
        self.imprimir_comercial()


    def pegando_numero(self):
        telefone1 = driver.find_elements(By.CSS_SELECTOR, 'span[class="AjtLy _1FXE6 _1lF7t"]')
        telefone2 = driver.find_elements(By.CSS_SELECTOR, 'span[class="_3NUK1 VWPRY _1lF7t"]')

        if telefone1 == []:
            self.n2 = telefone2[4].text
            print('NÚMERO COMERCIAL: ', self.n2)
            print('NÚMERO 2 COPIADO')
            time.sleep(2)
            self.pegar_nome_conta_comercial()
        else:
            self.n1 = telefone1[0].text
            print('NÚMERO: ', self.n1)
            print('NÚMERO 1 COPIADO')
            time.sleep(2)
            self.pegar_nome_conta()


    def primeira_msg(self):
        voltar=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[5]/span/div/span/div/header/div/div[1]/div/span')
        voltar.click()
        time.sleep(2)
        print('IREMOS RESPONDER AQUI')
        self.buscando_bolinha_notificacao1()



    def imprimir(self):
        print(f" =====================================\n Nome: {self.nome_conta} \n Número: {self.n1} \n =============================================")
        self.primeira_msg()
    def imprimir_comercial(self):
        print(f" ===================================== \n Título: {self.titulo} \n Nome Comercial: {self.nome_conta_comercial} \n Número: {self.n2} \n =============================================")
        self.primeira_msg()



if __name__=="__main__":
    site="https://web.whatsapp.com"
    tempo=1
    driver=webdriver.Chrome()
    bolinha_notificacao = driver.find_elements(By.CLASS_NAME, '_1pJ9J')
    navegador=Navegador(site,tempo,driver, bolinha_notificacao)





