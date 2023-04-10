import collections
from bson.objectid import ObjectId
from pymongo import MongoClient
import random
import threading
import time

class Sensor:
    def __init__(self,database):
        self.db = database
        self.collection = database.collection
    
    def create_temp(self, nome:str):
        try:
            
            # gerador aleatório de temp
            temp = random.randint(30,40) 
            if temp>38:
                SensorAlarmado = False
                result = self.collection.insert_one({'Nome': nome, 'Temp': [temp]})             
                print('Temperatura ', nome, temp, '°C')
                print('Atenção! Temperatura muito alta! Verificar' , nome,'!')  
                temp_id = str(result.inserted_id)          
            
            else:  
                result = self.collection.insert_one({'Nome': nome, 'Temp': [temp]})          
                print('Temperatura ',nome , temp, '°C')   
                time.sleep(2)
                temp_id = str(result.inserted_id)
                               
            SensorAlarmado  = True           
            while SensorAlarmado:
                # gerador aleatório de temp
                temp = random.randint(30,40) 
                if temp>38:
                    SensorAlarmado = False
                    result = self.collection.update_one({'_id':ObjectId(temp_id)}, {'$push':{'Temp': temp}})             
                    print('Temperatura ', nome, temp, '°C')
                    print('Atenção! Temperatura muito alta! Verificar' , nome,'!')            
            
                else:  
                    # result = self.collection.insert_one({'Nome': nome, 'Temp': temp})  
                    result = self.collection.update_one({'_id':ObjectId(temp_id)}, {'$push':{'Temp': temp}})           
                    print('Temperatura ',nome , temp, '°C')   
                    time.sleep(2)
                                   
                                                      
            # temp_id = str(result.inserted_id)
            print(f"sensor {nome} criado com id: {temp_id}")
            return temp_id
        except Exception as error:
            print(f"Um erro ocorreu na criação do livro: {error}")
            return None
    