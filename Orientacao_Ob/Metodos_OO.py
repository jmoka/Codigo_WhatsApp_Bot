'''
CLASSE MÉTODOS
'''
from Conexao_OO import conectar
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

