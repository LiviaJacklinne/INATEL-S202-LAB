from database import Database
from sensModel import Sensor
from save_json import writeAJson
import threading
import time
import random

db = Database(database='bancoiot', collection='sensores')
db.resetDatabase()

s = Sensor(database=db)
                  
s1 = threading.Thread(target=s.create_temp('Sensor 1'))
s1.start()

s2 = threading.Thread(target=s.create_temp('Sensor 2'))
s2.start()

s3 = threading.Thread(target=s.create_temp('Sensor 3'))
s3.start()





