# Software para Criptografia de Mensagens
# @author: Augusto dos Santos
# Aluno de Análise e Desenvolvimento de Sistemas - FATEC

# Funções para o App

class Funções:
    def __init__(self, mensagemIn, mensagemOut):
        self.texto1 = mensagemIn
        self.texto2 = mensagemOut
        self.vazio = self.texto1.get(1.0, 10.0)

    def cript(self):
        #Função para obter valor inteiro ASCII de um caractere ord()
        # Valor inteiro para o caractere ASCII correspondente chr()
        if self.texto1.get(1.0, 10.0) == self.vazio:
            self.texto2.delete(1.0, 10.0)
            self.texto2.insert(1.0, "SEM TEXTO PARA CRIPTOGRAFAR")
        else:
            newcript = ""
            for letra in self.texto1.get(1.0, 10.0):
                newcript += chr(ord(letra) + 1)
            self.texto2.delete(1.0, 10.0)
            self.texto2.insert(1.0, newcript)

    def descript(self):
        if self.texto1.get(1.0, 10.0) == self.vazio:
            self.texto2.delete(1.0, 10.0)
            self.texto2.insert(1.0, "SEM TEXTO PARA DESCRIPTOGRAFAR")
        else:
            newcript = ""
            for letra in self.texto1.get(1.0, 10.0):
                newcript += chr(ord(letra) - 1)
            self.texto2.delete(1.0, 10.0)
            self.texto2.insert(1.0, newcript)

    def areaTransf(self):
        print("Copiado para a área de transferência")

    def salvaTexto(self):
        arquivo = open('cripto.txt', 'w')
        for palavra in self.texto2.get(1.0, 10.0):
            arquivo.write("%s" %palavra)
        arquivo.close()
