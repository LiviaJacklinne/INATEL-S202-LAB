from bson.objectid import ObjectId
from pymongo import MongoClient

class Sensor:
    def __init__(self,database):
        self.db = database
    
    def create_temp(self, temperatura:str):
        try:
            result = self.collection.insert_one({"Temperatura": temperatura})
            temp_id = str(result.inserted_id)
            print(f"sensor {temperatura} criado com id: {temp_id}")
            return temp_id
        except Exception as error:
            print(f"Um erro ocorreu na criação do livro: {error}")
            return None
    