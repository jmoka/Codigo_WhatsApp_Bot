import requests

def nenhum(php):
    consulta = requests.get("http://localhost/bot/" + php + ".php/")
    consulta1 = consulta.text
    print(consulta1)

def um(php, coluna1, conteudo_coluna):
    consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna1: {conteudo_coluna}})
    consulta1 = consulta.text
    print( consulta1)

def dois(php,coluna1,coluna2,conteudo_coluna1, conteudo_coluna2):
    consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna1: {conteudo_coluna1}, coluna2: {conteudo_coluna2}})
    consulta1 = consulta.text
    print(consulta1)

def tres(php,coluna1,coluna2,coluna3,conteudo_coluna1, conteudo_coluna2, conteudo_coluna3):
    consulta = requests.get("http://localhost/bot/" + php + ".php/", params={coluna1: {conteudo_coluna1}, coluna2: {conteudo_coluna2}, coluna3: {conteudo_coluna3}})
    consulta1 = consulta.text
    print(consulta1)

def x():
    ss="+55 91 9629-3532"
    return ss
#menu_principal="verificar_fluxo_consulta"
#nenhum(menu_principal)


coluna1="titulo"
conteudo_coluna1="Jota Empresas"
coluna2=""
conteudo_coluna2=""
coluna3=""
conteudo_coluna3=""



msg_transicao1="msg_transicao1"
msg_opcao_errada="msg_opcao_errada"
msg_sair="msg_sair" # coluna=nome / coteudo="qualquer nome"
msg_confirma_nome_novamente="msg_confirma_nome_novamente" #coluna=nome informado
verificar_nome_informado="verificar_nome_informado"
verificar_grupo_sim_nao_pelo_telefone="verificar_grupo_sim_nao_pelo_telefone"
verificar_codigo="verificar_codigo"
atualizar_fluxo="atualizar_campo_fluxo"
cadastra_contato_inicial="verificar_telefone_inicial"
atualizar_campo_nome="atualizar_campo_nome"
fluxo_consulta_titulo="fluxo_consulta_titulo"


php="verificar_titulo_informado_0_1"
#dois(php,coluna1,coluna2, conteudo_coluna1, conteudo_coluna2)
um(php, coluna1, conteudo_coluna1)
#tres(php,coluna1,coluna2,coluna3,conteudo_coluna1,conteudo_coluna2,conteudo_coluna3)

