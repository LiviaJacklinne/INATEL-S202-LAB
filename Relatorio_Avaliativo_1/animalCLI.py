from database import Database
from classes import *
from zoologicoDAO import ZoologicoDAO

db = Database(database='Relatorio_avaliativo_1', collection='Animais')
data = db.collection.find()
zoologico = ZoologicoDAO(db)


aux = True

while(aux):
    print('Comandos: create, read, update, delete, sair')
    comando = input('Entre com um comando: ')
    
    if comando == 'create':
        print('--- Criando CUIDADOR ---')
        print('ID cuidador: ')
        cuidador_id = input()
        print('Nome cuidador: ')
        cuidador_nome = input()
        print('Documento cuidador: ')
        cuidador_doc = input()
        
        print('\n--- Criando HABITAT ---')
        print('ID habitat: ')
        habitat_id = input()
        print('Nome habitat: ')
        habitat_nome = input()
        print('Tipo de ambiente: ')
        habitat_ambiente = input()
        
        print('\n--- Criando ANIMAL ---')
        print('ID animal: ')
        animal_id = input()
        print('Nome animal: ')
        animal_nome = input()
        print('Especie do animal: ')
        animal_especie = input()
        print('Idade animal: ')
        animal_idade = int(input())
        
        # Atribuindo as info ao obj
        cuidador = Cuidador(cuidador_id, cuidador_nome, cuidador_doc)
        habitat = Habitat(habitat_id, habitat_nome, habitat_ambiente, cuidador)
        animal = Animal(animal_id, animal_nome, animal_especie, animal_idade, habitat)
        
        # Chamando a função 
        zoologico.createAnimal(animal, habitat, cuidador)
        
    elif comando == 'read':
        print('Digite o ID do animal que deseja ver: ')
        id = input()
        zoologico.readAnimal(id)
    
    elif comando == 'update':
        print('Digite o ID do animal que deseja alterar: ')
        id = input()
        print('Novo nome: ')
        novo_animal_nome = input()
        print('Nova especie: ')
        novo_animal_especie = input()
        print('Nova Idade: ')
        novo_animal_idade = int(input())
        zoologico.updateAnimal(id,novo_animal_nome, novo_animal_especie, novo_animal_idade)
        
        
    elif comando == 'delete':
        print('Digite o ID do animal que deseja deletar: ')
        id = input()
        zoologico.deleteAnimal(id)
        
    elif comando == 'sair':
        print('Você saiu!')
        aux = False
    
    else:
        print('Comando invalido. Tente novamente.')
        
        
        
    

