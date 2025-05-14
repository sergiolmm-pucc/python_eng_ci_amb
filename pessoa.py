##
#  Exemplo de uso de classes (OO) em python
#
class Pessoa:
    # define o construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.alture = None

    def setNome(self, nome):
        self.nome = nome
        
    def getNome(self):
        return self.nome
    
    def eMaiorDeIdade(self):
        return self.idade >= 18
            


if (__name__ == "__main__"):
    aluno = Pessoa("Isabelly",19)
    print(aluno.getNome())
    aluno.setNome("Melissa")
    print(aluno.getNome())
