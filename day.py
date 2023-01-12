import time

def check():
    today = time.ctime()[8:10]
    with open("init.log.txt","r",encoding="utf-8") as log:
        day = log.read()
    if day != "":
        day = day.split()[0]
    return day == today #返回True说明今天已经查询啦

def update():
    today = time.ctime()[8:10]
    with open("init.log.txt","w",encoding="utf-8") as log:
        log.write(today)
