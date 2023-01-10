import Conexao_BD

class Metodos:
  def __init__(self,sql,conexao,cursor, execucao, comite_resultado, fechar):
    self.setSql(sql)
    self.setConexao(conexao)
    self.setCursor(cursor)
    self.setExecucao(execucao)
    self.setComite_resultado(comite_resultado)
    self.setFechar(fechar)