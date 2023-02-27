# Importanto Classes
from Animal import *
from Elefante import *

aux = True
while aux:
    
    print("0 - Sair")
    print("1 - Cadastrar animal")
    menu = input("Digite sua opção: ")
    print("--------------------------------")
    
    if (int(menu)== 0):
        aux = False
        
    elif(int(menu) == 1):
        # Instanciando um objeto da classe 
        animal1 = Elefante()
        # animal1 = Elefante("alvo",11,"africano","branco","FuunH","mini")

        print("\n--------------------------------")
        print("** Informações do animal **")
        print("Nome:",animal1.nome)
        print("Idade:", animal1.idade)
        print("Especie:", animal1.especie)
        print("Cor:", animal1.cor)
        print("Som:", animal1.som)
        print("Tamanho:", animal1.tamanho)
        print("\n--------------------------------")
                
        # Chamando as funções
        animal1.emitir_som()
        animal1.mudar_cor()
        print("--------------------------------")
        print("Trombar")
        animal1.trombar()        
        print("--------------------------------\n** Informações Atualizadas **")
        print("Nome:",animal1.nome)
        print("Idade:", animal1.idade)
        print("Especie:", animal1.especie)
        print("Cor:", animal1.cor)
        print("Som:", animal1.som)
        print("Tamanho:", animal1.tamanho)        
        print("--------------------------------")
           
    else:
        print("Opção invalida")
        
print("Você saiu!\n")
