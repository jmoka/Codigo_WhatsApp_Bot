
class Contato_Inicial:
    def __init__(self, nome, titulo, telefone, grupo):
        self.nome=nome
        self.titulo=titulo
        self.telefone=telefone
        self.grupo=grupo
        self.sql_verificar_numero()

    def comandoDDL(self,sql):
        Conexao_BD.Metodos.metodo_conexao(sql)
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
        for i in Conexao_BD.Metodos.metodo_coleta(sql).Comite_resultado:
            print(i)
        if self.telefone in i:
            print('telefone enconetrado')
            print('enviar uma msg')
            Mensagens.mensagem.primeira_msg()



        elif i==[]:
           print('primeiro contato')
           self.inserirDadosTabela()
           Mensagens.mensagem.segunda_msg()







