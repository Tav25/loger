import json
import psutil
import time
import os




#PEREMENNUE


file_data = 'data.json'# рабочий файл

def sek_to_time(sek):
    day = 'Day: ' + str(sek//60//60//24) + ', '
    a = time.strftime("%H:%M:%S", time.gmtime(sek))
    return day + a

def sek_to_time_ND(sek):
    a = time.strftime("%H:%M:%S", time.gmtime(sek))
    return a

def j_load():
    myfile = open(file_data, 'r')
    global process_name
    process_name = json.load(myfile)
    myfile.close()

def j_dump():
    global process_name
    myfile = open(file_data, 'w')
    json.dump(process_name, myfile)
    myfile.close()



while True:


    
    
    time.sleep(1)
    os.system('cls')
