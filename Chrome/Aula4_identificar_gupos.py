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

    def __init__(self, site, tempo, driver): # ATRIBUTOS
        self.site=site
        self.tempo=tempo
        self.driver=driver
        self.driver.get(self.site)

        while(len(driver.find_elements(By.ID, 'side')) < 1) :
                time.sleep(8)
                print('AGUARDANDO AUTENTICAR QR-COD')
        else:
            print('QR-COD ABERTO')
            self.opcao = input('1-contatos\n2-grupos\n3-todos\n')
            time.sleep(self.tempo)
            self.buscando_bolinha_notificacao()


    def buscando_bolinha_notificacao(self):
        while(1):
            bolinha_notificacao=driver.find_elements(By.CLASS_NAME, '_1pJ9J')
            quantidade_bolinha_notificacao=len(bolinha_notificacao)
            time.sleep(self.tempo)
            if quantidade_bolinha_notificacao>0:
                print('NOVA MENSAGEM')
                for bolinhas_encontrada in bolinha_notificacao:
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
        t = driver.find_element(By.CLASS_NAME,'_21nHd')
        time.sleep(self.tempo)
        self.titulo=t.text.title()
        t.click()
        time.sleep(self.tempo)
        self.verificar_grupo()

    def verificar_grupo(self):
        elemento_grupo=driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="group-info-drawer-subject-input"]')
        self.quantidade_elemento_grupo=len(elemento_grupo)
        print('quantidade elemento grupo',self.quantidade_elemento_grupo)
        if self.quantidade_elemento_grupo >=1:
            for i in elemento_grupo:
                self.nome_do_grupo=i.text
                print('isso é um grupo')
                print('nome do grupo', self.nome_do_grupo)
                self.primeira_msg(self.opcao)

        else:
            self.pegando_numero()

    def pegar_nome_conta(self):
        n=driver.find_element(By.CSS_SELECTOR,'span[class="l7jjieqr cw3vfol9 i0jNr selectable-text copyable-text"]')
        time.sleep(self.tempo)
        self.nome_conta=n.text
        self.imprimir()
    def pegar_nome_conta_comercial(self):
        n=driver.find_element(By.XPATH,'//span[@class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 cw3vfol9 i0jNr selectable-text copyable-text"]')
        time.sleep(self.tempo)
        self.nome_conta_comercial=n.text
        self.imprimir_comercial()


    def pegando_numero(self):
        telefone1 = driver.find_elements(By.CSS_SELECTOR, 'span[class="AjtLy _1FXE6 _1lF7t"]')
        telefone2 = driver.find_elements(By.CSS_SELECTOR, 'span[class="_3NUK1 VWPRY _1lF7t"]')

        if telefone1 == []:
            self.n2 = telefone2[4].text
            time.sleep(self.tempo)
            self.pegar_nome_conta_comercial()
        else:
            self.n1 = telefone1[0].text
            time.sleep(self.tempo)
            self.pegar_nome_conta()


    def primeira_msg(self, opcao):

        voltar=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[5]/span/div/span/div/header/div/div[1]/div/span')
        voltar.click()
        time.sleep(self.tempo)
        if opcao=='1' and self.quantidade_elemento_grupo==0:
            print('responder contatos')
            self.buscando_bolinha_notificacao1()
        elif opcao=='2' and self.quantidade_elemento_grupo>=1:
            print('responder grupo')
            self.buscando_bolinha_notificacao1()
        elif opcao=='3':
            self.buscando_bolinha_notificacao1()
        else:
           self.esc()

    def esc(self):
        element = driver.find_element(By.CSS_SELECTOR,'div[class="n5hs2j7m oq31bsqd gx1rr48f qh5tioqs"]')
        print('voltando')
        element.send_keys(Keys.ESCAPE)
        time.sleep(self.tempo)
        self.buscando_bolinha_notificacao1()




    def imprimir(self):
        print(f"ESSA CONTA NÃO É COMERCIAL===============\nNome: {self.nome_conta}\nNúmero: {self.n1}\n=============================================")
        self.primeira_msg(self.opcao)
    def imprimir_comercial(self):
        print(f"ESSA CONTA É COMERCIAL==================\nTítulo: {self.titulo}\nNome Comercial: {self.nome_conta_comercial}\nNúmero: {self.n2}\n=============================================")
        self.primeira_msg(self.opcao)



if __name__=="__main__":
    site="https://web.whatsapp.com"
    tempo=1
    driver=webdriver.Chrome()
    navegador=Navegador(site,tempo,driver)





