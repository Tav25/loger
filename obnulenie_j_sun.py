import json
import time

file_data = 'data.json'# рабочий файл

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

def obnulenie_json():
    j_load()
    #input('Обнулеие данных, для продолжения нажмите ENTER.')
    for x in process_name:
        for y in process_name[x]:
            process_name[x][y] = 0
        #print(x,)
    j_dump()
    print('Завершено')

def obnulenie_json2():
    j_load()
    for x in process_name:
        process_name[x]['r1'] = 0


    process_name['Photoshop.exe']['r1'] = 0
    j_dump()



obnulenie_json()

