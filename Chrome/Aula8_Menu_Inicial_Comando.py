# Instalar " pip install mysql-connector-python "
import mysql.connector
'''importar a biblioteca selenium'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import mysql.connector
from unidecode import unidecode
#==========================================================================
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
            self.comando_iniciar()

    def comando_iniciar(self):
            campo_pesquisa = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
            campo_pesquisa.click()
            time.sleep(3)
            campo_pesquisa.send_keys(f'Bot Jota Novo', Keys.ENTER)

            self.campo_msg = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            self.campo_msg.click()

            time.sleep(3)
            self.campo_msg.send_keys('''))) MENU (((
                                             ESCOLHA UMA DAS OPÇÃO ABAIXO                            
                                             (1) - CONTATO
                                             (2) - GRUPOS
                                             (3) - TODOS''''', Keys.ENTER)
            self.buscando_msg()
    def buscando_msg(self):
        while (1):
            todas_as_msg = driver.find_elements(By.CSS_SELECTOR, 'div[class="_21Ahp"]')
            todas_as_msg_texto = [e.text for e in todas_as_msg]
            msg_ultima = todas_as_msg_texto[-1]
            self.opcao=msg_ultima
            time.sleep(2)
            self.conferir_msg(msg_ultima)

    def conferir_msg(self, opcao):
        if  opcao == "1":
            self.campo_msg = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            self.campo_msg.click()
            time.sleep(3)
            self.campo_msg.send_keys('''SISTEMA LIBERADO -  SOMENTE CONTATOS''''', Keys.ENTER)
            time.sleep(5)
            self.buscando_bolinha_notificacao()
        elif opcao == "2":
            self.campo_msg = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            self.campo_msg.click()
            time.sleep(3)
            self.campo_msg.send_keys('''SISTEMA LIBERADO -  SOMENTE GRUPO''''', Keys.ENTER)
            self.buscando_bolinha_notificacao()
        elif opcao == "3":
             self.campo_msg = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
             self.campo_msg.click()
             time.sleep(3)
             self.campo_msg.send_keys('''SISTEMA LIBERADO-SOMENTE CONATOS E GRUPOS''''', Keys.ENTER)
             self.buscando_bolinha_notificacao()
        else:
            self.buscando_msg()

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
                self.pegando_numero()
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
            return self.n2
        else:
            self.n1 = telefone1[0].text
            time.sleep(self.tempo)
            self.pegar_nome_conta()
            return self.n1

    def primeira_msg(self):
        voltar=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[5]/span/div/span/div/header/div/div[1]/div/span')
        voltar.click()
        time.sleep(self.tempo)
        if self.opcao=='1' and self.quantidade_elemento_grupo==0:
            print('PEGAR MENSAGEM ENVIADA')
            self.ler_msg()
        elif self.opcao=='2' and self.quantidade_elemento_grupo>=1:
            print('responder grupo')
            self.buscando_bolinha_notificacao1()
        elif self.opcao=='3':
            self.buscando_bolinha_notificacao1()
        else:
           self.esc()

    def esc(self):
        element = driver.find_element(By.CSS_SELECTOR,'div[class="n5hs2j7m oq31bsqd gx1rr48f qh5tioqs"]')
        print('voltando')
        element.send_keys(Keys.ESCAPE)
        time.sleep(self.tempo)
        self.buscando_bolinha_notificacao1()

    def ler_msg(self):
        todas_msg=driver.find_elements(By.CLASS_NAME,'_1Gy50')
        todas_msg_texto=[e.text for e in todas_msg]
        self.msg=unidecode(todas_msg_texto[-1].lower()).split() # transforma a instrig
        print('MENSAGEM EVIADA DIVIDIDA', self.msg)

        sql1 = f'''select boas_vindas from palavras_chaves; '''

        sql2 = f'''select saudacao from palavras_chaves; '''

        self.verificar_palavras_boas_vindas(sql1, sql2)

    def verificar_palavras_boas_vindas(self, sql1, sql2):
        '''BASE DE DADOS BOAS VINDAS'''
        base_palavras_msg_boasvindas = Metodos.metodo_coleta(sql1).Comite_resultado
        print('base_palavras_msg_boasvindas',base_palavras_msg_boasvindas)
        base_palavras_msg_boasvindas1=list(base_palavras_msg_boasvindas)
        base_palavras_msg_boasvindas2 = str(base_palavras_msg_boasvindas1)
        self.base_palavras_msg_boasvindas3=unidecode(base_palavras_msg_boasvindas2.lower())
        print('base_palavras_msg_boasvindas3 CONVERTIDA', self.base_palavras_msg_boasvindas3)

        for x in self.msg:
            if x in self.base_palavras_msg_boasvindas3:
                print('ACHEI A MSG BOAS VINDAS:', x)
                self.responder_msg()
        else:
            print('NÃO ACHEI MSG BOAS VINDAS')
            self.verificar_palavras_saudacao(sql2)

    def verificar_palavras_saudacao(self,sql2):
        '''BASE DE DADOS BOAS VINDAS'''
        base_verificar_palavras_saudacao = Metodos.metodo_coleta(sql2).Comite_resultado
        print('base_verificar_palavras_saudacao', base_verificar_palavras_saudacao)
        base_verificar_palavras_saudacao1 = list(base_verificar_palavras_saudacao)
        base_verificar_palavras_saudacao2 = str(base_verificar_palavras_saudacao1)
        self.base_verificar_palavras_saudacao3 = unidecode(base_verificar_palavras_saudacao2.lower())
        print('base_verificar_palavras_saudacao3 CONVERTIDA', self.base_verificar_palavras_saudacao3)

        for x in self.msg:
            if x in self.base_verificar_palavras_saudacao3:
                print('ACHEI A MSG SAUDAÇÃO:', x)
                self.responder_msg1()
        else:
            print('NÃO ACHEI MSG SAUDAÇÃO')
            self.responder_msg2()

    def responder_msg(self):
        campo_texto=driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        campo_texto.click()
        time.sleep(3)
        campo_texto.send_keys(f'"olá" {self.nome_conta}',Keys.ENTER)
        print('MENSAGEM ENVIADA OLÁ')
        self.esc()
        self.primeira_msg()

    def responder_msg1(self):
        campo_texto = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        campo_texto.click()
        time.sleep(3)
        campo_texto.send_keys(f'"TUDO BEM COM VC? {self.nome_conta}"', Keys.ENTER)
        print('MENSAGEM ENVIADA TUDO BEM COM VC?')
        self.esc()
        self.primeira_msg()

    def responder_msg2(self):
        campo_texto = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        campo_texto.click()
        time.sleep(3)
        campo_texto.send_keys(f'"COMO VC ESTÁ {self.nome_conta}"', Keys.ENTER)
        print('MENSAGEM ENVIADA TUDO BEM COM VC?')
        self.esc()
        self.primeira_msg()

    def imprimir(self):
        grupo="false"
        titulo='não tem'
        print(f"ESSA CONTA NÃO É COMERCIAL===============\nNome: {self.nome_conta}\nNúmero: {self.n1}\n=============================================")
        Contato_Inicial(self.nome_conta, titulo, self.n1, grupo)
        self.primeira_msg()
    def imprimir_comercial(self):
        grupo="true"
        print(f"ESSA CONTA É COMERCIAL==================\nTítulo: {self.titulo}\nNome Comercial: {self.nome_conta_comercial}\nNúmero: {self.n2}\n=============================================")
        self.primeira_msg()

'''
CLASSE CONEXAO
'''
class Conexao:
    def __init__(self, host, database, user, password, port, tabela):
        self.host=host
        self.database=database
        self.user=user
        self.password=password
        self.port=port
        self.tabela=tabela

    def conexao(self):
        con = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port)
        print('CONECTADO')
        return con
'''
CLASSE MÉTODOS
'''
class Metodos:
  def __init__(self,sql,conexao,cursor, execucao, comite_resultado, fechar):
    self.sql=sql
    self.Conexao=conexao
    self.Cursor=cursor
    self.execucao=execucao
    self.Comite_resultado=comite_resultado
    self.Fechar=fechar

  def metodo_conexao(sql):
      conexao = conectar.conexao()
      cursor = conexao.cursor()
      execucao = cursor.execute(sql)
      comite_resultado = conexao.commit()
      fechar = conexao.close()
      metodos = Metodos(sql, conexao, cursor, execucao, comite_resultado, fechar)
      return metodos

  def metodo_coleta(sql):
      conexao = conectar.conexao()
      cursor = conexao.cursor()
      execucao = cursor.execute(sql)
      comite_resultado = cursor.fetchall()
      fechar = conexao.close()
      metodos = Metodos(sql, conexao, cursor, execucao, comite_resultado, fechar)
      return metodos

'''
CLASSE DADOS INICIAIS
'''

class Contato_Inicial:
    def __init__(self, nome, titulo, telefone, grupo):
        self.nome=nome
        self.titulo=titulo
        self.telefone=telefone
        self.grupo=grupo
        self.sql_verificar_numero()

    def comandoDDL(self,sql):
        Metodos.metodo_conexao(sql)
        print('Ação Bem Sucedida!!')

    def inserirDadosTabela(self):
    # Inserir Dados nas Tabelas, "INSERT INTO NOME DA TABELA (COLUNA1,COLUNA2) VALUES (X,Y,G)
        sql = f''' insert into cadastro
               (nome,titulo,telefone,grupo) 
               VALUES 
               ("{self.nome}","{self.titulo}","{self.telefone}", "{self.grupo}");'''
        self.comandoDDL(sql)

    def sql_verificar_numero(self):
        print('telefone para consulta', self.telefone)
        sql = f'''select * from cadastro
        where telefone='{self.telefone}'; '''
        self.verificar_numero(sql)
    def verificar_numero(self, sql):
        i=[]
        for i in Metodos.metodo_coleta(sql).Comite_resultado:
            print(i)
        if self.telefone in i:
            print('telefone enconetrado')
            print('enviar uma msg')
            print('IR PARA A MENSAGEM CONTATO ENCONTRATO')
        elif i==[]:
           print('primeiro contato')
           self.inserirDadosTabela()
           print('IR PARA A MENSAGEM CONTATO ENCONTRATO')

if __name__=="__main__":
    host = 'localhost'
    database = 'BD_WhatsApp'
    user = 'root'
    password = "123456"
    port = '3306'
    tabela="cadastro"
    conectar = Conexao(host, database, user, password, port,tabela)

    site = "https://web.whatsapp.com"
    tempo = 1
    driver = webdriver.Chrome()
    navegador = Navegador(site, tempo, driver)

    nome = ""
    titulo = ""
    telefone = ""
    grupo = ""
    contato_inicial=Contato_Inicial(nome,titulo, telefone, grupo)









