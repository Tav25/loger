import json



file_data = 'data.json'# рабочий файл

print(file_data)





myfile = open(file_data, 'r')
process_name = json.load(myfile)
myfile.close()


print(process_name)
print(process_name['total_time'])
