import json







def max_time2():
    myfile = open('text.txt', 'r')
    global process_name
    process_name = json.load(myfile)
    myfile.close()
    kl = 0
    for d_json in process_name:
        if d_json['time2'] > kl: kl = d_json['time2']
    print(kl)


max_time2()