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

def j_load(file_data):
    myfile = open(file_data, 'r')
    global process_name
    process_name = json.load(myfile)
    myfile.close()

def j_dump(file_data):
    global process_name
    myfile = open(file_data, 'w')
    json.dump(process_name, myfile)
    myfile.close()

#
def clar_json(file_data):
    j_load(file_data)
    for g in process_name:
        print(g)
        process_name[g].clear()
    j_dump()

def obr():
    j_load(file_data)



#while True:
x = int(time.time())
print(x)
#obr()
j_load(file_data)

for g in process_name:
    process_name[g]['id'] = 0
    process_name[g]['time_run'] = 0
    process_name[g]['time_now'] = 0
    #print(g)
for g in process_name:
    for proc in psutil.process_iter():
        name = proc.name()
        if name == g:
            print(name)
            process_name[g]['id'] = proc.pid
            process_name[g]['time_run'] = proc.create_time()
            process_name[g]['time_now'] = x - process_name[g]['time_run']


print(process_name)

#time.sleep(1)
#os.system('cls')
