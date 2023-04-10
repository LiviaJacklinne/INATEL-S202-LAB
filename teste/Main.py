from database import Database
from sensModel import Sensor
from save_json import writeAJson
import threading
import time
import random

# db = Database(database='bancoiot', collection='sensores')
# db.resetDatabase()

# Função do sensor
def sensor (nome,intervalo):
    # Variavel auxiliar do while
    SensorAlarmado  = True
    i = 0
    while SensorAlarmado:
        # gerador aleatório de temp
        temp = random.randint(30,40) 
        if temp>38:
            SensorAlarmado = False
            print('Temperatura ' , temp, '°C')
            print('Atenção! Temperatura muito alta! Verificar' , nome,'!')            
    
        else:           
            print('Temperatura ',nome , temp, '°C')   
            time.sleep(intervalo)
                      
s1 = threading.Thread(target=sensor, args=('Sensor 1', 2))
s1.start()

s2 = threading.Thread(target=sensor, args=('Sensor 2', 2))
s2.start()

s3 = threading.Thread(target=sensor, args=('Sensor 3', 2))
s3.start()




