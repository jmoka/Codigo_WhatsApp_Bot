# Instalar " pip install mysql-connector-python "
'''importar a biblioteca selenium'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from unidecode import unidecode
from multiprocessing import Process
import requests

# CONEXÃO COM O WHATSAPP
def conexao():
    '''ESPERA ATE COM QUE O ELEMENTO SIDE SEJA ENCONTRADO NA TELA'''
    while (len(driver.find_elements(By.ID, 'side')) < 1):
        time.sleep(1)  # "padrão 1"
    else:
        print('QR-COD ABERTO')
        time.sleep(1)  # "padrão 2"

# CLASSE DA MENSAGEM RECEBIDA
class Mensagem_recebida():
    def __init__(self, mensagem):
        self.mensagem_recebida=mensagem
        #self.thread=threading.Thread(target=self.procesar_mensagem_recebida)
        #self.thread.start()

    def procesar_mensagem_recebida(self):
        '''VERIFICA O TITULO NOME DO CONTATO NA PAGINA'''
        titulo_coletado = driver.find_element(By.CSS_SELECTOR, 'div[class="_21nHd"]')
        titulo_inicial_coletado = titulo_coletado.text
        print("TITULO COLETADO NA PAGINA", titulo_inicial_coletado)
        '''VERIFICA SE EXISTE O FLUXO DO CONTATO NO BANCO E DADOS O RETORNO É 0 OU NUMERO DO FLUXO'''
        fluxo = verificar_cadastro_no_banco_retorna_valor_inteiro_valor_do_fluxo("verificar_fluxo_consulta_pelo_titulo",titulo_inicial_coletado)
        fluxo1 = verificar_cadastro_no_banco_retorna_valor_inteiro_valor_do_fluxo(
            "verificar_fluxo_pelo_titulo_informado_0_1", titulo_inicial_coletado)
        print("FLUXO ENCONTRADO NO BANCO DE DADOS: ", fluxo)
        '''NÃO TEM O CONTATO NO BANCO DE DADOS'''
        if fluxo1 == 0:
            print("if")
            fluxo_para_atualizar = 1
            '''CHAMA A FUNÇÃO PARA CADASTRAR O TITULO E O FLUXO NUMERO 1 '''
            cadastrar_banco_de_dados("cadastrar_cliente_novo", titulo_inicial_coletado, fluxo_para_atualizar)
            '''ENVIA PARA A CLASSE MENSAGEM O FLUXO E O TITULO COLETADO'''

            Mensagem_enviada(fluxo, titulo_inicial_coletado, self.mensagem_recebida)

        else:
            print("else")

            Mensagem_enviada(fluxo, titulo_inicial_coletado, self.mensagem_recebida)


    def verificar_cadastro_no_banco_retorna_valor_inteiro_valor_do_fluxo(self,php, titulo):
        coluna = "titulo"
        consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna: {titulo}})
        consulta1 = int(consulta.text)
        print("resposta da consulta se tem cadastro",consulta1)
        return consulta1

    def cadastrar_banco_de_dados(self, php, titulo, fluxo):
        coluna = "titulo"
        coluna1 = "fluxo"
        consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna: {titulo}, coluna1: {fluxo}})
        consulta1 = consulta.text
        print("resposta da consulta se tem cadastro", consulta1)
        return consulta1

#================================================
#================================================
#===============================================
class Mensagem_enviada:

    def __init__(self, fluxo, titulo, mensagem_recebida):
        self.fluxo=fluxo
        self.titulo=titulo
        self.mensagem_recebida=mensagem_recebida
        '''FLUXO DAS MENSAGENS'''
        print("COMANDO CONFERIR FLUXO == ACESSADO---", self.fluxo)
        self.enviar_mensagem(self.fluxo)
        #self.thread=threading.Thread(target=self.enviar_mensagem(self.fluxo))
        #self.thread.start()


    def enviar_mensagem(self, fluxo):
        if fluxo == 0:
            print("fluxo escolhido é 0")

            '''
            MENSAGEM ENVIADA: E A PRIMEIRA VEZ QUE VEJO VOCÊ AQUI EM NOSSO BOT_MOSQUEIRO!!!
            QUAL O SEU NOME?            
            '''
            self.enviar_mensagem1(self.php_2_paramentro("msg_primeira_novo_contato", self.titulo, "titulo"))
            '''ATUALIZA BANCO DE DADOS COM O FLUXO  1 VINDO DA OU'''
            self.atualizar_campo_banco_de_dados("atualizar_campo_fluxo_pelo_titulo", self.titulo, self.fluxo)
            self.esc()
            # ATUALIZA FLUXO
            proximo_fluxo = 1
            self.php_2_elementos("atualizar_campo_fluxo_pelo_titulo", self.titulo, proximo_fluxo)
            main()

        elif fluxo == 1:
            print("fluxo escolhido é 1")
            '''VERIFICAR NOME CADASTRADO'''
            nome_cadastrado = self.php_2_paramentro("verificar_nome_informado_pelo_titulo", self.titulo, "titulo")
            print("NOME COLETADO NO BANCO---", nome_cadastrado)
            '''ENVIA A MENSAGEM PARA CONFIRMAR O NOME E O MENU SIM E NÃO'''
            self.enviar_mensagem1(self.php_2_paramentro("msg_confirmacao_nome",self.mensagem_recebida, "nome_informado"))
            self.enviar_mensagem1( self.msg_sem_parametros("menu_sim_nao"))
            '''ATUALIZA O CAMPO NOME NO BANCO DE DADOS'''
            self.atualizar_nome("atualizar_campo_nome_pelo_titulo", self.titulo, self.mensagem_recebida)
            '''ATUALIZA O CAMPO FLUXO NO BANCO DE DADOS'''
            proximo_fluxo = 2
            self.php_2_elementos("atualizar_campo_fluxo_pelo_titulo", self.titulo, proximo_fluxo)
            self.esc()
            print("enviou para bolinha")
            main()

        elif fluxo == 2:
            print("fluxo escolhido é 2")
            '''VERIFICAR NOME CADASTRADO'''
            nome_cadastrado = self.php_2_paramentro("verificar_nome_informado_pelo_titulo", self.titulo, "titulo")
            print("NOME COLETADO NO BANCO---", nome_cadastrado)
            msg = unidecode(self.mensagem_recebida.lower())
            time.sleep(2)
            print("MENSAGEM ENVIADA PARA FLUXO", msg)
            print( "mensagem enviada para o fluxo 2",)
            sim = ["1", "s","sin", "sim", "ok", "ta", "certo", "ta certo", "certissimo", "com certeza", "perfeito", "claro",
                   "positivo", "afirmativo"]
            nao = ["2", "nao","n","no", "ta errado", "errado", "corrigir"]
            sair = ["sair", "3"]
            if msg in sim:
                '''ENVIA A MENSAGEM DE TRANSIÇÃO -  OK ENTENDI , QUAL SEU NOME NOVAMENTE'''
                self.enviar_mensagem1(self.php_2_paramentro("msg_transicao1", nome_cadastrado, "nome"))
                time.sleep(1)
                self.enviar_mensagem1(self.msg_sem_parametros("menu_principal"))
                '''ATUALIZA O CAMPO FLUXO NO BANCO DE DADOS'''
                proximo_fluxo = 3
                self.php_2_elementos("atualizar_campo_fluxo_pelo_titulo", self.titulo, proximo_fluxo)
                self.esc()
                print("enviou para bolinha")
                main()

            elif msg in nao:
                '''ENVIA A MENSAGEM  OPÇÃO NÃO'''
                self.enviar_mensagem1(self.php_2_paramentro("msg_confirma_nome_novamente", nome_cadastrado, "nome"))
                proximo_fluxo = 1
                self.php_2_elementos("atualizar_campo_fluxo_pelo_titulo", self.titulo, proximo_fluxo)
                self.esc()
                print("enviou para bolinha")
                main()

            elif msg in sair:
                '''ENVIA A MENSAGEM OPÇÃO SAIR '''
                self.enviar_mensagem1( self.php_2_paramentro("msg_sair", nome_cadastrado, "nome"))
                proximo_fluxo = 1
                self.php_2_elementos("atualizar_campo_fluxo_pelo_titulo", self.titulo, proximo_fluxo)
                self.esc()
                print("enviou para bolinha")
                main()

            else:
                '''ENVIA A MENSAGEM DE TRANSIÇÃO -  OK ENTENDI , QUAL SEU NOME NOVAMENTE'''
                self.enviar_mensagem1( self.php_2_paramentro("msg_opcao_errada", nome_cadastrado, "nome"))
                proximo_fluxo = 2
                '''ENVIA A MENSAGEM PARA CONFIRMAR O NOME E O MENU SIM E NÃO'''
                self.enviar_mensagem1(self.php_2_paramentro("msg_confirmacao_nome", nome_cadastrado, "nome_informado"))
                self.enviar_mensagem1(self.msg_sem_parametros("menu_sim_nao"))
                self.php_2_elementos("atualizar_campo_fluxo_pelo_titulo", self.titulo, proximo_fluxo)
                self.esc()
                print("enviou para bolinha")
                main()


#=============================================================================
    '''PARAMETROS DA MENSAGEM'''
#=============================================================================
    def msg_sem_parametros(self, php):
        consulta = requests.get("http://localhost/bot/" + php + ".php/")
        msg_php = consulta.text
        return msg_php

    def php_2_paramentro(self,php, titulo, coluna):

        consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna: {titulo}})
        msg_php = consulta.text
        return msg_php

    def atualizar_nome(self, php, titulo, nome_informado):
        coluna = "titulo"
        coluna1 = "nome_informado"
        consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna: {titulo}, coluna1: {nome_informado}})
        consulta1 = consulta.text
        print("resposta da consulta se tem cadastro", consulta1)
        return consulta1

    def enviar_mensagem1(self,mensagens_php):
        msg_php1 = mensagens_php
        time.sleep(1)
        # elemento campo msg
        campo_texto = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        campo_texto.click()
        time.sleep(1)
        # enviar msg
        campo_texto.send_keys(msg_php1, Keys.ENTER)

    def verificar_cadastro_no_banco_retorna_valor_inteiro_valor_do_fluxo(self,php, titulo):
        coluna = "titulo"
        consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna: {titulo}})
        consulta1 = int(consulta.text)
        print("resposta da consulta se tem cadastro",consulta1)
        return consulta1

    def php_2_elementos(self,php, titulo, fluxo):
        coluna = "titulo"
        coluna1="fluxo"
        consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna: {titulo},coluna1:{fluxo}})
        consulta1 = consulta.text
        print("resposta da consulta se tem cadastro",consulta1)
        return consulta1

    def atualizar_campo_banco_de_dados(self,php, titulo, fluxo):
        campo = requests.get("http://localhost/bot/" + php + ".php/", params={"fluxo": {fluxo}, "titulo": {titulo}})
        campo = campo.text
        print("campo:", campo)
        return campo

    def esc(self):
        element2 = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]')
        element2.send_keys(Keys.ESCAPE)

    def mensagem_recebida(self):
        '''VERIFICA AS MENSAGENS RECEBIDA'''
        todas_as_msg = driver.find_elements(By.CSS_SELECTOR, 'span[class="_11JPr selectable-text copyable-text"]')
        todas_as_msg_texto = [e.text for e in todas_as_msg]
        mensagem_recebida = todas_as_msg_texto[-1]  # MENSAGEM RECEBIDA
        return mensagem_recebida


def main():
    while (1):
        # PEGA AS NOVAS MENSAGENS
        '''BUSCA NOVAS MENSAGENS  '''
        bolinha_notificacao = driver.find_elements(By.CLASS_NAME, '_1pJ9J')
        '''CONFERE A QUANTIDADE DE MENSAGEM'''
        quantidade_bolinha_notificacao = len(bolinha_notificacao)
        if quantidade_bolinha_notificacao > 0:
            time.sleep(2)
            for bolinhas_encontrada in bolinha_notificacao:
                time.sleep(1)
                # MENSAGEM ENCONTRADA CLICAR
                bolinhas_encontrada.click()
            else:
                # DEPOIS DE CLICAR NA MENSAGEM NOVA
                time.sleep(1)  # padrão e 2
                print("procurando elemento grupo")
                # VERIFICA SE É UM GRUPO
                elemento_grupo = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="group-info-drawer-subject-input"]')
                quantidade_elemento_grupo = len(elemento_grupo)
                print("qunatidade de elemento grupo", quantidade_elemento_grupo)
                # SE FOR GRUPO
                if quantidade_elemento_grupo >= 1:
                    # FOR UM GRUPO
                    '''CONFERINDO SE É GRUPO'''
                    grupo = "sim"
                    for i in elemento_grupo:
                        nome_do_grupo = i.text
                        print("NOME DO GRUPO===", nome_do_grupo)
                else:
                    # NÃO É GRUPO
                    grupo = "não"
                    '''VERIFICA AS MENSAGENS RECEBIDA'''
                    todas_as_msg = driver.find_elements(By.CSS_SELECTOR,  'span[class="_11JPr selectable-text copyable-text"]')
                    todas_as_msg_texto = [e.text for e in todas_as_msg]
                    mensagem_recebida = todas_as_msg_texto[-1]  # MENSAGEM RECEBIDA
                    print("MSG", mensagem_recebida)
                    '''VERIFICA O TITULO NOME DO CONTATO NA PAGINA'''
                    titulo_coletado = driver.find_element(By.CSS_SELECTOR, 'div[class="_21nHd"]')
                    titulo_inicial_coletado = titulo_coletado.text
                    print("TITULO COLETADO NA PAGINA", titulo_inicial_coletado)
                    '''VERIFICA SE EXISTE O FLUXO DO CONTATO NO BANCO E DADOS O RETORNO É 0 OU NUMERO DO FLUXO'''
                    fluxo = verificar_cadastro_no_banco_retorna_valor_inteiro_valor_do_fluxo("verificar_fluxo_consulta_pelo_titulo", titulo_inicial_coletado)
                    fluxo1 = verificar_cadastro_no_banco_retorna_valor_inteiro_valor_do_fluxo("verificar_fluxo_pelo_titulo_informado_0_1", titulo_inicial_coletado)
                    print("FLUXO ENCONTRADO NO BANCO DE DADOS: ", fluxo)
                    '''NÃO TEM O CONTATO NO BANCO DE DADOS'''
                    if fluxo1 == 0:
                        print("if")
                        fluxo_para_atualizar = 1
                        '''CHAMA A FUNÇÃO PARA CADASTRAR O TITULO E O FLUXO NUMERO 1 '''
                        cadastrar_banco_de_dados("cadastrar_cliente_novo", titulo_inicial_coletado,fluxo_para_atualizar)
                        '''ENVIA PARA A CLASSE MENSAGEM O FLUXO E O TITULO COLETADO'''

                       # Mensagem_enviada(fluxo, titulo_inicial_coletado, mensagem_recebida)
                        Mensagem_enviada(fluxo, titulo_inicial_coletado, mensagem_recebida)
                    else:
                        print("else")
                        #Mensagem_recebida(mensagem_recebida)
                        Mensagem_enviada(fluxo, titulo_inicial_coletado, mensagem_recebida)





def verificar_cadastro_no_banco_retorna_valor_inteiro_valor_do_fluxo(php, titulo):
    coluna = "titulo"
    consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna: {titulo}})
    consulta1 = int(consulta.text)
    print("resposta da consulta se tem cadastro", consulta1)
    return consulta1

def cadastrar_banco_de_dados(php, titulo, fluxo):
    coluna = "titulo"
    coluna1 = "fluxo"
    consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna: {titulo}, coluna1: {fluxo}})
    consulta1 = consulta.text
    print("resposta da consulta se tem cadastro", consulta1)
    return consulta1
                # aqui a thread


#================================================================================

if __name__ == "__main__":
    site = "https://web.whatsapp.com"
    tempo = 1
    driver = webdriver.Chrome()
    driver.get(site)
    conexao()
    main()
    for i in range(10):
        t= Process(target=main)
        t.start()




