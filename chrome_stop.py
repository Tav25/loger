#добавить время старта

import os
import psutil
import time
file_name = '404.html'

def chrome_run(i,time_periud,ogranichenie_rabotu_chrom):
    process_name = "chrome.exe"
    #time_periud = 5
    #ogranichenie_rabotu_chrom = 25
    for proc in psutil.process_iter():
        name = proc.name()
        id_first_chrome = proc.pid
        while name == process_name:

            #time.sleep(time_periud)
            if i is None:
                i = 0

            i = i + time_periud

            if i > ogranichenie_rabotu_chrom:
                os.system('taskkill /f /im  "' + process_name + '"')
                i = 0
            file1 = open(file_name, 'w')
            file1.write("""
            <h1 style="text-align: center;"><strong>Хром будет закрыт через <span style="color: #ff0000;">{}</span> секунд!</strong></h1>
            <h2 style="text-align: center;"><strong>интернет только для работы</strong></h2>
            <p style="text-align: center;"><img src="https://uip.me/wp-content/uploads/2014/02/poljubitq-svoju-rabotu.jpg" alt="" width="630" height="325" /></p>
            """.format(ogranichenie_rabotu_chrom))
            file1.close()
            if i == time_periud:
                os.system(file_name)
            return i



