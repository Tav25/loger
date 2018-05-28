#добавить время старта

import os
import psutil
import time
import json
import chrome_stop

#file_data = 'text.json'# для тестирования
file_data = 'data.txt'# рабочий файл

print(file_data)

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

def max_time2():
    myfile = open(file_data, 'r')
    global process_name
    process_name = json.load(myfile)
    myfile.close()
    kl = 0
    for d_json in process_name:
        if d_json['time'] > kl:
            kl = d_json['time']
    return kl


pauza = 5
time2 = int(time.time())
chrome_i = 0
z1 = True
zxc = 1


text_opisanie = (
''' ORPA v1.0
 Отслеживание работы программ''')

pereruv = input("Перерыв минут = ")
if pereruv =='':
    pereruv = 0
else: pereruv = int(pereruv) * 60

rabota = input("Работа минут  = ")
if rabota =='':
    rabota = 60*60
else: rabota = int(rabota) *60
rabota0 = rabota
pereruv0 = pereruv
print('загрузка...')

while True:

    ogranichenie_chorme = 60 * 2
    pauza0 = 0
    alpha1 = []

    j_load()

    for data_json in process_name:

        for proc in psutil.process_iter():
            name = proc.name()
            id_proxess = proc.pid
            if data_json['name'] == name:

                kl = 0
                for d_json in process_name:

                    if d_json["name"] == "total":

                        d_json['time'] = d_json['time'] + pauza 
                        zxc = d_json['time']
                        pauza0 = pauza

                if data_json['mmm'] != int(proc.create_time()):
                    data_json['time2'] = data_json['time'] + data_json['time2']
                    data_json['time'] = 0
                    data_json['mmm'] = proc.create_time()


                data_json['time'] = ((int(time.time()) - int(proc.create_time())))

                #форматирование для вывода
                dlinna_name = 25 - len(name)
                minutu = (((data_json['time']+data_json['time2'])//60))//60
                minutu_min = (((data_json['time']+data_json['time2'])//60))%60
                minutu = round(minutu, 0)
                #print(minutu_min)
                cv = ''
                if minutu_min < 10: cv = "0"
                minutu = str(minutu) + "." + cv + str(minutu_min)
                dlinna_time = 5 - len(minutu)
                data_proc_for_print = ('|'+name +' '*dlinna_name+'|       ' + '0' * dlinna_time + str((minutu))+ '    |')
                alpha1.append(data_proc_for_print)

    j_dump()
    os.system('cls')# отчистка экрана
    print(text_opisanie)


    if rabota > 0:
        
        rabota = (rabota - pauza0)
        print(' До перерыва осталось = {}.{}'.format(rabota//60,rabota%60))
    else:
        pereruv = (pereruv - pauza)
        
        print(' До конца перерыва осталось = {}.{}'.format(pereruv//60,pereruv%60))

        if pereruv < 0:
            rabota = rabota0
            pereruv = pereruv0





    print('--------------------------------------------')
    print('| Procname                |      time min  |')
    print('--------------------------------------------')
    for f_print_alpha in alpha1:
        print(f_print_alpha)
        print('--------------------------------------------')
    if z1 == True:
        print('*-'*22)
        z1 = False
    else:
        print('-*'*22)
        z1 = True

    #print(zxc)
    if zxc != 1:
        x1 = ''
        x2 = ''
        if (zxc//60)//60 < 10: x1 = '0'
        if (zxc // 60) % 60 < 10: x2 = '0'
        zxc2 = x1 +str((zxc//60)//60) + '.'+ x2 +str((zxc//60)%60)
    else:
        zxc2 = "None"
        zxc = 1
    
    print('time work: {} h'.format(zxc2))

    chrome_i = chrome_stop.chrome_run(chrome_i,pauza,ogranichenie_chorme)

    if chrome_i != None:
        print('До закрытия хрома осталось: {} секунд.'.format(ogranichenie_chorme - chrome_i))
    time.sleep(pauza)