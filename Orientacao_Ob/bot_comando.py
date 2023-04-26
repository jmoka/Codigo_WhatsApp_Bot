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

class Comando_inicial:

    def __init__(self, site, tempo, driver):  # ATRIBUTOS
        self.site = site
        self.tempo = tempo
        self.driver = driver
        self.driver.get(self.site)
    def iniciar(self):
        while (len(driver.find_elements(By.ID, 'side')) < 1):
            time.sleep(2) #"padrão 1"
        else:
            print('QR-COD ABERTO')
            time.sleep(2) #"padrão 2"
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
                    print("CLICOU NA BOLINHA")
                    print("PROXIMO COMANDO: verificar_se_ja_tem_cadastro")
                    time.sleep(1) #"padrão 1"
                    self.verificar_se_e_grupo()

    def comando_iniciar(self):
            time.sleep(1)  # "padrão 1"
            campo_pesquisa = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
            campo_pesquisa.click()
            print("esperando aparecer o elemento---")
            time.sleep(2) #"padrão 1"
            campo_pesquisa.send_keys(f'Bot Jota Novo', Keys.ENTER)
            print("esperando chama teste---")
            self.campo_msg1()

    def campo_msg1(self):
            time.sleep(1) #"padrão 1"
            self.campo_msg = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            self.campo_msg.click()
            time.sleep(2) #"padrão 1"
            menu = "menu2"
            self.campo_msg.send_keys(self.php(menu), Keys.ENTER)
            self.msg = self.buscando_msg()
            time.sleep(1) #"padrão 1"
            print("mensagem enviada - comando", self.msg)
            self.conferir_msg(self.msg)

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

    def verificar_se_e_grupo(self):
            time.sleep(2) # padrão e 2
            self.elemento_grupo = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="group-info-drawer-subject-input"]')
            self.quantidade_elemento_grupo = len(self.elemento_grupo)
            print('quantidade elemento grupo', self.quantidade_elemento_grupo)
            if self.quantidade_elemento_grupo >= 1:
                self.grupo = "sim"
                for i in self.elemento_grupo:
                    self.nome_do_grupo = i.text
                    print('isso é um grupo')
                    print('nome do grupo', self.nome_do_grupo)
                    self.pegar_numero_titulo()
            else:
                self.grupo = "não"
                self.pegar_numero_titulo()

    def verificar_se_ja_tem_cadastro(self):
        print("PROXIMO COMANDO: verificar_se_ja_tem_cadastro == ACESSADO")
        telefone = int(self.telefone_coletado_Bd())
        print("TELEFONE PARA CONSULTA_ ( 1 ) ou ( 0 ):", telefone)
        if telefone == 0:
            print("NÃO ENCONTROU TELEFONE NO BANCO, CLIENTE NOVO ")
            self.pegar_numero_titulo()
        else:
            print("CHAMAR CLASSE FLUXO - FUNÇÃO : verificar_se_ja_tem_cadastro")
            Mensagem()

    def telefone_coletado_Bd(self):
        php = "verificar_telefone_pelo_titulo"
        coluna = "titulo"
        titulo_coletado_pagina=self.pegar_titulo_inicial()
        print("telefone inical coletado", titulo_coletado_pagina)
        verifica_telefone = self.consultar_um_elemento_bd(php, coluna, titulo_coletado_pagina)
        return verifica_telefone

    def pegar_titulo_inicial(self):
        print("PEGAR TITULO NA PAGINA")
        titulo_coletado = driver.find_element(By.CSS_SELECTOR,'div[class="_21nHd"]')
        titulo_inicial_coletado = titulo_coletado.text
        print("TITULO COLETADO NA PAGINA", titulo_inicial_coletado)
        return titulo_inicial_coletado

    def consultar_um_elemento_bd(self, php, coluna1, conteudo_coluna):
        print("php verificado", php)
        print("coluna", coluna1)
        print("conteudo da coluna", conteudo_coluna)
        consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna1: {conteudo_coluna}})
        consulta1 = consulta.text
        print(consulta1)
        return consulta1

    def pegar_numero_titulo(self):
        # clica na foto na pagina
        print("PROXIMO COMANDO: verificar_se_ja_tem_cadastro == CONFERINDO TITULO")
        telefone = int(self.telefone_coletado_Bd())
        print("TELEFONE PARA CONSULTA_ ( 1 ) ou ( 0 ):", telefone)

        if telefone == 0:
            print("NÃO ENCONTROU TELEFONE NO BANCO, CLIENTE NOVO ")
            c = driver.find_element(By.CSS_SELECTOR, 'div[class="_21nHd"]')
            c.click()
            time.sleep(1) #padrão 1
            # pega o telefone na pagina
            t = driver.find_element(By.CSS_SELECTOR, 'span[class="_10kwi _1BX24 dd2Ow"]')
            self.telefone = t.text
            # pega o titulo na gagina
            s = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[5]/span/div/span/div/div/section/div[1]/div[2]/h2/span')
            self.titulo = s.text.title()
            print('TITULO:', self.titulo)
            print('GRUPO', self.grupo)
            print('TELEFONE DO CONTATO:', self.telefone)

            self.verificar_numero_e_estatus("verificar_telefone_inicial")
            primeira_msg = self.verificar_numero_e_estatus("msg_primeira_novo_contato")
            self.esc_completo(primeira_msg)
        else:
            print("CHAMAR CLASSE FLUXO FUNÇÃO - pegar_numero_titulo")
            Mensagem()


    def verificar_numero_e_estatus(self, php):
        telefone = self.telefone
        titulo = self.titulo
        grupo = self.grupo
        ph = requests.get("http://localhost/bot/" + php + ".php/", params={"telefone": {telefone}, "titulo": {titulo}, "grupo": {grupo}})
        Php = ph.text
        return Php

    def esc_completo(self, php):
        print('iniciar esc completo 1')
        # clica no x
        time.sleep(2) # padrão e 2
        self.element1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[5]/span/div/span/div/header/div/div[1]/div/span')
        self.element1.click()

        print('iniciar esc completo 2')
        # clica no campo superior
        time.sleep(2)
        self.campo_texto = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        self.campo_texto.click()
        # da um esc depois de ter selecionado o campo
        self.campo_texto.send_keys(php, Keys.ENTER)

        print('iniciar esc completo 3')
        time.sleep(1)# padrão e 2
        self.element2 = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]')
        self.element2.send_keys(Keys.ESCAPE)

        print('iniciar esc completo 4')
        self.buscando_bolinha_notificacao()

    def buscando_msg(self):
        while (1):
            todas_as_msg = driver.find_elements(By.CSS_SELECTOR, 'div[class="_21Ahp"]')
            todas_as_msg_texto = [e.text for e in todas_as_msg]
            msg_ultima = todas_as_msg_texto[-1]
            self.opcao = msg_ultima
            return msg_ultima

    def php(self, Php):
        p = (f"http://localhost/bot/{Php}.php/")
        ph = requests.get(p)
        php = ph.text
        return php

    def sistema_liberado(self, ms):
        msg1 = ms
        self.campo_msg = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        self.campo_msg.click()
        time.sleep(1)
        msg = self.campo_msg.send_keys(msg1, Keys.ENTER)
        return msg

#===========================================================================================================
    '''INICIAR CLASSE MENSAGEM'''
#===========================================================================================================
class Mensagem():  # HERANÇA
    def __init__(self):
        # VERIFICAR FLUXO NO BANCO
        self.fluxo1=int(self.verificar_fluxo_Bd_M())
        print("FLUXO COLETADO BANCO DE DADOS CLASSE MSG", self.fluxo1)
        self.conferir_fluxo(self.fluxo1)

    def buscando_bolinha_notificacao1(self):
        while (1):
            bolinha_notificacao = driver.find_elements(By.CLASS_NAME, '_1pJ9J')
            quantidade_bolinha_notificacao = len(bolinha_notificacao)
            time.sleep(2)
            if quantidade_bolinha_notificacao > 0:
                print('NOVA MENSAGEM')
                for bolinhas_encontrada in bolinha_notificacao:
                    time.sleep(2)
                    bolinhas_encontrada.click()
                    print("CLICOU NA BOLINHA")
                    print("PROXIMO COMANDO: verificar_se_ja_tem_cadastro")
                    time.sleep(1) #"padrão 1"
                    Mensagem()

    def pegar_telefone_inicial_M(self):
        titulo_coletado = driver.find_element(By.CSS_SELECTOR,'span[class="_7T_0D"]')
        titulo_inicial_coletado = titulo_coletado.text
        return titulo_inicial_coletado

    def telefone_coletado_Bd_M(self):
        php = "verificar_telefone_pelo_titulo_resposts_telefone"
        coluna = "titulo"
        telefone_coletado_bd = self.pegar_titulo_inicial1()
        verifica_telefone = str(self.consultar_um_elemento_bd_M(php, coluna, telefone_coletado_bd))
        print("telefone coletado ----", verifica_telefone )
        return verifica_telefone

    def consultar_um_elemento_bd_M(self, php, coluna1, conteudo_coluna):
        print("php verificado", php)
        print("coluna", coluna1)
        print("conteudo da coluna", conteudo_coluna)
        consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna1: {conteudo_coluna}})
        consulta1 = consulta.text
        print(consulta1)
        return consulta1

    def verificar_fluxo_Bd_M(self):
        php="fluxo_consulta_titulo"
        conteudo_coluna=self.pegar_titulo_inicial_M()
        consulta = requests.get("http://localhost/bot/" + php + ".php/", params={"titulo": {conteudo_coluna}})
        fluxo_cadastrado_bd = consulta.text
        print("FLUXO COLETADO",fluxo_cadastrado_bd)
        time.sleep(2)
        return fluxo_cadastrado_bd

    def pegar_titulo_inicial_M(self):
        print("PEGAR TITULO NA PAGINA")
        titulo_coletado = driver.find_element(By.CSS_SELECTOR, 'div[class="_21nHd"]')
        titulo_inicial_coletado = titulo_coletado.text
        print("TITULO COLETADO NA PAGINA", titulo_inicial_coletado)
        return titulo_inicial_coletado
#================================================================

    def conferir_fluxo(self, fluxo):
        print("COMANDO CONFERIR FLUXO == ACESSADO")
        if fluxo== 0:
            inicio.iniciar()

        elif fluxo == 1:
            print("fluxo escolhido é 1")
            msg_confirmacao_nome = self.php_1("msg_confirmacao_nome")

            self.atualizar_fluxo(2)

            sim_nao1 = self.php_0("menu_sim_nao")
            self.php_2("atualizar_campo_nome_pelo_titulo")

            self.enviar_msg_ja_na_pagina_esc(msg_confirmacao_nome)
            time.sleep(1)
            self.enviar_msg_ja_na_pagina_esc(sim_nao1)
            self.esc_simples()
            self.buscando_bolinha_notificacao1()
            print("enviou para bolinha")

        elif fluxo == 2:
            print("fluxo escolhido é 2")
            time.sleep(2)
            msg = unidecode(self.buscando_msg().lower()) #
            print("msg -- - - :", msg)
            sim = ["1", "sim", "ok", "ta", "certo", "ta certo", "certissimo", "com certeza", "perfeito", "claro","positivo", "afirmativo"]
            nao = ["2", "não", "ta errado", "errado", "corrigir"]
            sair = ["sair", "3"]
            if msg in sim:
             #   self.nome_cadastrado = self.verificar_nome()
                nome_cadastrado = self.verificar_nome()
                print("nome_cadastrado fluxo 2", nome_cadastrado)
                msg_transicao1 = self.msg_transicao()
                print("msg_transicao1 fluxo 2", msg_transicao1)
                self.enviar_msg_ja_na_pagina_esc(msg_transicao1)
                menu_principal1 = self.menu_principal()
                self.enviar_msg_ja_na_pagina_esc(menu_principal1)
                self.esc_simples()
                self.buscando_bolinha_notificacao1()
            elif msg in nao:
               # self.nome_cadastrado = self.verificar_nome()
                msg_confirma_nome_novamente = self.msg_confirma_nome_novamente()
                self.enviar_msg_ja_na_pagina_esc(msg_confirma_nome_novamente)
                self.atualizar_fluxo(1)
                self.esc_simples()
                self.buscando_bolinha_notificacao1()

            elif msg in sair:
               # self.nome_cadastrado = self.verificar_nome()
                msg_sair = self.msg_sair()
                self.enviar_msg_ja_na_pagina_esc(msg_sair)
                self.atualizar_fluxo(4)
                self.esc_simples()
                self.buscando_bolinha_notificacao1()
            else:
              #  self.nome_cadastrado = self.verificar_nome()
                msg_opcao_errada = self.msg_opcao_errada()
                self.enviar_msg_ja_na_pagina_esc(msg_opcao_errada)
                self.atualizar_fluxo(2)
                self.esc_simples()
                self.buscando_bolinha_notificacao1()

    def atualizar_fluxo(self, fluxo):
        print("fluxo para consulta em atualizar:---", fluxo)
        php0 = "atualizar_campo_fluxo_pelo_titulo"
        titulo=self.pegar_titulo_inicial_M()
        fluxo = requests.get("http://localhost/bot/" + php0 + ".php/", params={"fluxo": {fluxo}, "titulo": {titulo}})
        fluxo1 = fluxo.text
        print("fluxo:", fluxo1)
        return fluxo1

    def php_0(self, php):
        php1 = php
        ph = requests.get("http://localhost/bot/" + php1 + ".php/")
        ph1 = ph.text
        return ph1

    def php_1(self, php):
        msg = inicio.buscando_msg()
        php1 = php
        ph = requests.get("http://localhost/bot/" + php1 + ".php/", params={"nome_informado": {msg}})
        ph1 = ph.text
        return ph1

    def php_2(self, php):
        msg = inicio.buscando_msg()
        php2 = php
        titulo=self.pegar_titulo_inicial_M()
        ph = requests.get("http://localhost/bot/" + php2 + ".php/",  params={"nome": msg, "titulo": {titulo}})
        ph1 = ph.text
        return ph1

    def verificar_numero_e_estatus_M(self, php):
        telefone = self.telefone_coletado_Bd_M()
        titulo = self.pegar_titulo_inicial_M()
        grupo = inicio.grupo
        ph = requests.get("http://localhost/bot/" + php + ".php/", params={"telefone": {telefone}, "titulo": {titulo}, "grupo": {grupo}})
        Php = ph.text
        return Php

    def x_enviar_msg_ja_na_pagina(self, msg_php):
        msg_php1 = msg_php
        # elemento x
        time.sleep(1)
        element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[5]/span/div/span/div/header/div/div[1]/div/span')
        element.click()
        time.sleep(1)
        # elemento campo msg
        campo_texto = driver.find_element(By.XPATH,  '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        campo_texto.click()
        time.sleep(1)
        # enviar msg
        campo_texto.send_keys(msg_php1, Keys.ENTER)

    def enviar_msg_ja_na_pagina_esc(self, msg_php):
        msg_php1 = msg_php
        time.sleep(1)
        # elemento campo msg
        campo_texto = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        campo_texto.click()
        time.sleep(1)
        # enviar msg
        campo_texto.send_keys(msg_php1, Keys.ENTER)


    def msg_transicao(self):
        php1 = "msg_transicao1"
        nome_cadastrado = self.verificar_nome()
        msg_transicao1 = requests.get("http://localhost/bot/" + php1 + ".php/",  params={"nome": {nome_cadastrado}})
        msg_transicao1 = msg_transicao1.text
        return msg_transicao1

    def msg_opcao_errada(self):
        php1 = "msg_opcao_errada"
        nome_cadastrado = self.verificar_nome()
        msg_opcao_errada = requests.get("http://localhost/bot/" + php1 + ".php/", params={"nome": {nome_cadastrado}})
        msg_opcao_errada1 = msg_opcao_errada.text
        return msg_opcao_errada1

    def msg_sair(self):
        php1 = "msg_sair"
        nome_cadastrado = self.verificar_nome()
        msg_sair = requests.get("http://localhost/bot/" + php1 + ".php/", params={"nome": {nome_cadastrado}})
        msg_sair1 = msg_sair.text
        return msg_sair1

    def msg_confirma_nome_novamente(self):
        php1 = "msg_confirma_nome_novamente"
        nome_cadastrado=self.verificar_nome()
        msg_confirma_nome_novamente = requests.get("http://localhost/bot/" + php1 + ".php/", params={"nome": {nome_cadastrado}})
        msg_confirma_nome_novamente1 = msg_confirma_nome_novamente.text
        return msg_confirma_nome_novamente1

    def esc_simples(self):
        time.sleep(1)
        element1 = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]')
        time.sleep(1)
        element1.send_keys(Keys.ESCAPE)

    def verificar_nome(self):
        php = "verificar_nome_informado_pelo_titulo"
        titulo=self.pegar_titulo_inicial1()
        ph = requests.get("http://localhost/bot/" + php + ".php/", params={"titulo": {titulo}})
        nome_cadastrado = ph.text
        print('nome coletado:', nome_cadastrado)
        return nome_cadastrado

    def menu_principal(self):
        php = "menu_principal"
        menu_principal = requests.get("http://localhost/bot/" + php + ".php/")
        menu_principal1 = menu_principal.text
        return menu_principal1

    def verificar_fluxo(self):
        php = "fluxo_consulta_titulo"
        self.fluxo = int(self.verificar_numero_e_estatus1(php))
        self.conferir_fluxo(self.fluxo)

    def verificar_numero_e_estatus1(self, php):
        telefone = self.telefone_coletado_Bd_M
        titulo = self.pegar_titulo_inicial_M()
        grupo = inicio.grupo
        ph = requests.get("http://localhost/bot/" + php + ".php/",  params={"telefone": {telefone}, "titulo": {titulo}, "grupo": {grupo}})
        Php = ph.text
        return Php

    def pegar_titulo_inicial1(self):
        print("PEGAR TITULO NA PAGINA")
        titulo_coletado = driver.find_element(By.CSS_SELECTOR,'div[class="_21nHd"]')
        titulo_inicial_coletado = titulo_coletado.text
        print("TITULO COLETADO NA PAGINA", titulo_inicial_coletado)
        return titulo_inicial_coletado

    def buscando_msg(self):
        while (1):
            todas_as_msg = driver.find_elements(By.CSS_SELECTOR, 'div[class="_21Ahp"]')
            todas_as_msg_texto = [e.text for e in todas_as_msg]
            msg_ultima = todas_as_msg_texto[-1]
            self.opcao = msg_ultima
            return msg_ultima
#================================================================================

if __name__ == "__main__":
    site = "https://web.whatsapp.com"
    tempo = 1
    driver = webdriver.Chrome()
    inicio = Comando_inicial(site, tempo, driver)
    inicio.iniciar()
