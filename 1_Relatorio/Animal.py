# Classe Animal
class Animal:
        
    #  # Construtor da classe por parametro
    # def __init__(self,nome,idade,especie,cor,som): 
    #     self.nome = nome
    #     self.idade = idade
    #     self.especie = especie
    #     self.cor = cor
    #     self.som = som
    
    # Construtor da classe, entrada de dados
    def __init__(self): 
        self.nome = input("Digite o nome: ")
        self.idade = input("Digite a idade: ")
        self.especie = input("Digite a especie: ")
        self.cor = input("Digite a cor: ")
        self.som = input("Digite o som: ")
        
    # Função emitir som
    def emitir_som(self):   
        print("Som do animal:", self.som) 
        
    # Função para alterar a cor do animal
    def mudar_cor(self):
        self.cor = input("Altere a cor: ")
        # print("Nova cor:", self.cor)
        