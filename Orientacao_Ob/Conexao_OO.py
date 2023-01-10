'''
CLASSE CONEXAO
'''
import mysql.connector
class Conexao:
    def __init__(self, host, database, user, password, port, tabela):
        self.host=host
        self.database=database
        self.user=user
        self.password=password
        self.port=port
        self.tabela=tabela
        self.conexao()

    def conexao(self):
        con = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port)
        print('CONECTADO')
        return con

host = 'localhost'
database = 'BD_WhatsApp'
user = 'root'
password = "123456"
port = '3306'
tabela="cadastro"
conectar = Conexao(host, database, user, password, port,tabela)
