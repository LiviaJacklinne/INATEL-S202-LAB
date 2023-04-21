from bson.objectid import ObjectId
from database import Database
from classes import *

db = Database(database='Relatorio_avaliativo_1', collection='Animais')
# db.resetDatabase()
data = db.collection.find()

class ZoologicoDAO(Animal):
    def __init__(self, database):
        self.db = database
        self.collection = database.collection
        
    def createAnimal(self, Animal, Habitat, Cuidador):
        try:
            res = self.db.collection.insert_one({'nome' : Animal.nome,'especie': Animal.especie,'idade': Animal.idade,'ID Habitat': Habitat.id, 'Nome Habitat': Habitat.nome,'Tipo de Ambiente':Habitat.tipoAmbiente,'ID Cuidador': Cuidador.id, 'Nome do Cuidador': Cuidador.nome, 'Documento cuidador': Cuidador.documento})
            print(f'Animal criado com o id: {res.inserted_id}')
            return res.inserted_id
        except Exception as e:
            print(f'Erro na criação do animal: {e}')
            return None
        
    def readAnimal(self, id:str)-> dict:
        try:
            res = self.db.collection.find_one({'_id':ObjectId(id)})
            print(f'Animal encontrado: {res}')
            return res
        except Exception as e:
            print(f'Erro na leitura do animal: {e}')
            return None
        
    def updateAnimal(self, id:str, name:str, especie:str, idade:int):
        try:
            res = self.db.collection.update_one({'_id': ObjectId(id)},{'$set': {'nome':name, 'especie':especie, 'idade':idade}})
            print(f'Animal alterado com sucesso: {res.modified_count}')
            return res.modified_count
        except Exception as e:
         print(f'Erro na alteração do animal: {e}')
         return None
     
    def deleteAnimal(self, id:str):
        try:
            res = self.db.collection.delete_one({'_id': ObjectId(id)})
            if res.deleted_count:
                print(f'Animal deletado :{id} ')
            else:
                print(f'Animal não encontrado com o id {id}')
            return res.deleted_count
        
        except Exception as e:
            print(f'Ocorreu um erro ao deletar o animal: {e}')
            return None
        