from unidecode import unidecode
'''

class Verificar:
    def __init__(self, base, msg_enviada):
        self.base=base
        self.msg_enviada=msg_enviada

        self.verificar_msg_enviada()

    def verificar_msg_enviada(self):
        print('mensagem',self.msg_enviada)
        i=unidecode(self.msg_enviada.lower()).split()
        print(i)
        for palavras_base in self.base:
            print(palavras_base)
            if palavras_base in i:
                print(palavras_base)



if __name__=="__main__":
    msg_enviada = ('jose ola oI belém')
    lista_base=["oi", "ola", 'belem']
    verificar=Verificar(lista_base, msg_enviada)
'''


numeros = input().split()
numeros = [int(x) for x in numeros]
maior_numero = max(numeros)

for i in range(len(numeros)):
    numeros[i] = maior_numero - numeros[i]

print(numeros)