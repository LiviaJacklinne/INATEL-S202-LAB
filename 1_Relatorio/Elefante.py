# Importando classe
from Animal import *

#Classe Elefante que herda Animal       
class Elefante(Animal):
      
   # Construtor da classe por parametro
    # def __init__(self, nome, idade, especie, cor, som,tamanho):
    #     super().__init__(nome, idade, especie, cor, som)
    #     self.tamanho = tamanho
    
    # Construtor da classe com entrada de dados
    def __init__(self):
        super().__init__()
        self.tamanho = input("Digite o tamanho: ")
              
    # Função que verifica a especie e emite o som do animal 
    def trombar(Animal):
        if(Animal.especie == 'africano' and int(Animal.idade) < 10):
            Animal.tamanho = "pequeno"
            Animal.som = Animal.som.lower() # função para deixar as letras minusculas
            print("Tamanho:", Animal.tamanho)
            print("Som:", Animal.som)
         
        elif (Animal.especie == 'africano' and int(Animal.idade) >= 10):
            Animal.tamanho = "grande"
            Animal.som = Animal.som.upper() # função para deixar as letras maiusculas
            print("Tamanho:", Animal.tamanho)
            print("Som:", Animal.som)
            
        else:
            print("Tamanho:", Animal.tamanho)
            print("Som:", Animal.som)
                   