# Instalar " pip install mysql-connector-python "
import mysql.connector

'''importar a biblioteca selenium'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import mysql.connector
from unidecode import unidecode
import requests

# ==========================================================================
class Inicio:
    ''''MÉTODO CONSTRUTOR'''

    def __init__(self, site, tempo, driver):  # ATRIBUTOS
        self.site = site
        self.tempo = tempo
        self.driver = driver
        self.driver.get(self.site)

        while (len(driver.find_elements(By.ID, 'side')) < 1):
            time.sleep(0)
        else:
            print('QR-COD ABERTO')
            time.sleep(2)
            self.comando_iniciar()

    def buscando_bolinha_notificacao(self):
        while (1):
            bolinha_notificacao = driver.find_elements(By.CLASS_NAME, '_1pJ9J')
            quantidade_bolinha_notificacao = len(bolinha_notificacao)
            time.sleep(self.tempo)
            if quantidade_bolinha_notificacao > 0:
                print('NOVA MENSAGEM')
                for bolinhas_encontrada in bolinha_notificacao:
                    time.sleep(self.tempo)
                    bolinhas_encontrada.click()
                    self.verificar_se_e_grupo()

    # ============================================================================================
    def conferir_msg(self, opcao):
        if opcao == "1":
            self.sistema_liberado("*SISTEMA LIBERADO -  SOMENTE CONTATOS*")
            self.buscando_bolinha_notificacao()
        elif opcao == "2":
            self.sistema_liberado("*SISTEMA LIBERADO -  SOMENTE GUPOS*")
            self.buscando_bolinha_notificacao()
        elif opcao == "3":
            self.sistema_liberado("*SISTEMA LIBERADO -  CONTATOS E GUPOS*")
            self.buscando_bolinha_notificacao()
        else:
            msg = self.buscando_msg()
            self.conferir_msg(msg)

    # ============================================================================================
    def conferir_fluxo(self, fluxo):
        if fluxo == 0:
            self.verificar_numero_e_estatus("verificar_telefone_inicial")
            primeira_msg = self.verificar_numero_e_estatus("msg_primeira_novo_contato")
            self.esc_completo(primeira_msg)
            self.buscando_bolinha_notificacao()
        elif fluxo == 1:
            msg_confirmacao_nome = self.php_1("msg_confirmacao_nome")
            self.atualizar_fluxo(2)
            self.php_0("menu_sim_nao")
            sim_nao1 = self.php_0("menu_sim_nao")
            self.php_2("atualizar_campo_nome")
            self.x_enviar_msg_ja_na_pagina(msg_confirmacao_nome)
            time.sleep(1)
            self.enviar_msg_ja_na_pagina_esc(sim_nao1)
            self.buscando_bolinha_notificacao()
        elif fluxo == 2:
            msg = unidecode(self.buscando_msg().lower())
            sim = ["1", "sim", "ok", "ta", "certo", "ta certo", "certissimo", "com certeza", "perfeito", "claro",
                   "positivo", "afirmativo"]
            nao = ["2", "não", "ta errado", "errado", "corrigir"]
            sair = ["sair", "3"]
            if msg in sim:
                self.nome_cadastrado = self.verificar_nome()
                msg_transicao1 = self.msg_transicao()
                self.x_enviar_msg_ja_na_pagina(msg_transicao1)
                time.sleep(1)
                menu_principal1 = self.menu_principal()
                self.enviar_msg_ja_na_pagina_esc(menu_principal1)
                self.atualizar_fluxo(3)
                self.buscando_bolinha_notificacao()

            elif msg in nao:
                self.nome_cadastrado = self.verificar_nome()
                msg_confirma_nome_novamente = self.msg_confirma_nome_novamente()
                self.x_enviar_msg_ja_na_pagina(msg_confirma_nome_novamente)
                self.atualizar_fluxo(1)
                self.esc_simples()

            elif msg in sair:
                self.nome_cadastrado = self.verificar_nome()
                msg_sair = self.msg_sair()
                self.x_enviar_msg_ja_na_pagina(msg_sair)
                self.atualizar_fluxo(0)
                self.esc_simples()


            else:
                self.nome_cadastrado = self.verificar_nome()
                msg_opcao_errada = self.msg_opcao_errada()
                self.x_enviar_msg_ja_na_pagina(msg_opcao_errada)
                self.atualizar_fluxo(0)
                self.esc_simples()

    # =================================================================================================

    ###########################################################################################=======
    def comando_iniciar(self):
        time.sleep(1)
        campo_pesquisa = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
      #  time.sleep(1)
        campo_pesquisa.click()
        time.sleep(1)
        campo_pesquisa.send_keys(f'Bot Jota Novo', Keys.ENTER)
        time.sleep(1)
        self.campo_msg = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
       # time.sleep(1)
        self.campo_msg.click()
        time.sleep(1)
        menu = "menu2"
        self.campo_msg.send_keys(self.php(menu), Keys.ENTER)
        time.sleep(1)
        self.msg = self.buscando_msg()
        print("mensagem enviada - comando", self.msg)
        self.conferir_msg(self.msg)

    def buscando_msg(self):
        while (1):
            todas_as_msg = driver.find_elements(By.CSS_SELECTOR, 'div[class="_21Ahp"]')
            todas_as_msg_texto = [e.text for e in todas_as_msg]
            msg_ultima = todas_as_msg_texto[-1]
            self.opcao = msg_ultima
            time.sleep(1)
            return msg_ultima

    def verificar_se_e_grupo(self):
        elemento_grupo = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="group-info-drawer-subject-input"]')
        self.quantidade_elemento_grupo = len(elemento_grupo)
        print('quantidade elemento grupo', self.quantidade_elemento_grupo)
        if self.quantidade_elemento_grupo >= 1:
            self.grupo = "sim"
            for i in elemento_grupo:
                self.nome_do_grupo = i.text
                print('isso é um grupo')
                print('nome do grupo', self.nome_do_grupo)
                self.pegar_numero_titulo()
        else:
            self.grupo = "não"
            self.pegar_numero_titulo()

    def pegar_numero_titulo(self):
        c = driver.find_element(By.CSS_SELECTOR, 'div[class="_21nHd"]')
        c.click()
        time.sleep(1)
        t = driver.find_element(By.CSS_SELECTOR, 'span[class="_10kwi _1BX24 dd2Ow"]')
        self.telefone = t.text
        s = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[5]/span/div/span/div/div/section/div[1]/div[2]/h2/span')
        self.titulo = s.text.title()
        print('TITULO:', self.titulo)
        print('GRUPO', self.grupo)
        print('TELEFONE DO CONTATO:', self.telefone)
        self.verificar_fluxo()

    def verificar_msg_nome_informadoz(self):
        todas_as_msg = driver.find_elements(By.CSS_SELECTOR, 'div[class="_21Ahp"]')
        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg_ultima = todas_as_msg_texto[-1]
        self.Msg_ultima = msg_ultima
        print('MENSAGEM ENVIADA:', self.Msg_ultima)
        self.buscando_bolinha_notificacao()

    def sistema_liberado(self, ms):
        msg1 = ms
        self.campo_msg = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        self.campo_msg.click()
        time.sleep(1)
        msg = self.campo_msg.send_keys(msg1, Keys.ENTER)
        return msg

    def php(self, Php):
        p = (f"http://localhost/bot/{Php}.php/")
        ph = requests.get(p)
        php = ph.text
        return php

    def verificar_numero_e_estatus(self, php):
        ph = requests.get("http://localhost/bot/" + php + ".php/", params={"telefone": {self.telefone}, "titulo": {self.titulo}, "grupo": {self.grupo}})
        Php = ph.text
        return Php

    def verificar_fluxo(self):
        php = "fluxo_consulta_titulo"
        self.fluxo = int(self.verificar_numero_e_estatus(php))
        self.conferir_fluxo(self.fluxo)

    def menu_principal(self):
        php = "menu_principal"
        menu_principal = requests.get("http://localhost/bot/" + php + ".php/")
        menu_principal1 = menu_principal.text
        return menu_principal1

    def msg_transicao(self):
        php1 = "msg_transicao1"
        msg_transicao1 = requests.get("http://localhost/bot/" + php1 + ".php/", params={"nome": {self.nome_cadastrado}})
        msg_transicao1 = msg_transicao1.text
        return msg_transicao1

    def msg_opcao_errada(self):
        php1 = "msg_opcao_errada"
        msg_opcao_errada = requests.get("http://localhost/bot/" + php1 + ".php/", params={"nome": {self.nome_cadastrado}})
        msg_opcao_errada1 = msg_opcao_errada.text
        return msg_opcao_errada1

    def msg_sair(self):
        php1 = "msg_sair"
        msg_sair = requests.get("http://localhost/bot/" + php1 + ".php/", params={"nome": {self.nome_cadastrado}})
        msg_sair1 = msg_sair.text
        return msg_sair1

    def msg_confirma_nome_novamente(self):
        php1 = "msg_confirma_nome_novamente"
        msg_confirma_nome_novamente = requests.get("http://localhost/bot/" + php1 + ".php/", params={"nome": {self.nome_cadastrado}})
        msg_confirma_nome_novamente1 = msg_confirma_nome_novamente.text
        return msg_confirma_nome_novamente1

    def verificar_nome(self):
        php = "verificar_nome_informado"
        ph = requests.get("http://localhost/bot/" + php + ".php/", params={"telefone": {self.telefone}})
        self.nome_cadastrado = ph.text
        return self.nome_cadastrado

    def php_0(self, php):
        php1 = php
        ph = requests.get("http://localhost/bot/" + php1 + ".php/")
        ph1 = ph.text
        return ph1

    def php_1(self, php):
        msg = self.buscando_msg()
        php1 = php
        ph = requests.get("http://localhost/bot/" + php1 + ".php/", params={"nome_informado": {msg}})
        ph1 = ph.text
        return ph1

    def php_2(self, php):
        msg = self.buscando_msg()
        php2 = php
        ph = requests.get("http://localhost/bot/" + php2 + ".php/", params={"nome": msg, "telefone": {self.telefone}})
        ph1 = ph.text
        return ph1

    def x_enviar_msg_ja_na_pagina(self, msg_php):
        msg_php1 = msg_php
        # elemento x
        time.sleep(1)
        element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[5]/span/div/span/div/header/div/div[1]/div/span')
        element.click()
        time.sleep(1)
        # elemento campo msg
        campo_texto = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        campo_texto.click()
        time.sleep(1)
        # enviar msg
        campo_texto.send_keys(msg_php1, Keys.ENTER)

    def enviar_msg_ja_na_pagina_esc(self, msg_php):
        msg_php1 = msg_php
        time.sleep(1)
        # elemento campo msg
        campo_texto = driver.find_element(By.XPATH,  '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        campo_texto.click()
        time.sleep(1)
        # enviar msg
        campo_texto.send_keys(msg_php1, Keys.ENTER)
        # esc na pagina
        time.sleep(1)
        element1 = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]')
        time.sleep(1)
        element1.send_keys(Keys.ESCAPE)

    def atualizar_fluxo(self, fluxo):
        php0 = "atualizar_campo_fluxo"
        fluxo = requests.get("http://localhost/bot/" + php0 + ".php/",  params={"fluxo": {fluxo}, "telefone": {self.telefone}})
        fluxo1 = fluxo.text
        print("fluxo:", fluxo1)
        return fluxo1

    def esc_simples(self):
        element1 = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]')
        time.sleep(1)
        element1.send_keys(Keys.ESCAPE)

        self.buscando_bolinha_notificacao()

    def esc_completo(self, php):
        element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[5]/span/div/span/div/header/div/div[1]/div/span')
        time.sleep(1)
        element.click()

        time.sleep(1)
        campo_texto = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        time.sleep(1)
        campo_texto.click()
        time.sleep(1)
        campo_texto.send_keys(php, Keys.ENTER)
        time.sleep(1)

        element1 = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]')
        time.sleep(1)
        element1.send_keys(Keys.ESCAPE)

        self.buscando_bolinha_notificacao()


if __name__ == "__main__":
    site = "https://web.whatsapp.com"
    tempo = 1
    driver = webdriver.Chrome()
    inicio = Inicio(site, tempo, driver)

