import pymysql
import threading
import random
import reset
import time
import sys

class ONLINE:
    def __init__(self):
        self.conn = pymysql.connect(host = "", port =  , user = "", passwd = "", db = "", charset="")
        self.connT = pymysql.connect(host = "", port =  , user = "", passwd = "", db = "", charset="")

        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
        self.curT = self.connT.cursor(pymysql.cursors.DictCursor)

        self.queryUS = "select * from username"
        self.queryW = "select * from gamelog"
        self.queryADD = "insert into username(user, passwd) values("

        self.USED = []
        self.data = []
        self.count = 10
        self.curWord = ""
        self.name = ""
        self.end = False

        print("<<SERVER CONNECTED>>")
        print("<<WELCOME TO 끄투GSA>>")

        self.setName()
        self.run()

    def setName(self):
        while True:
            self.cur.execute(self.queryUS)
            userlist = self.cur.fetchall()
            self.conn.commit()
            temp = []
            for i in userlist:
                temp.append(i["user"])
            a = int(input("1. 사용자 로그인 2. 새로 만들기 >> "))
            if a == 1:
                id = input("ID >> ")
                pswd = input("PASSWORD >> ")
                if id in temp:
                    if userlist[temp.index(id)]["passwd"] == pswd:
                        self.name = id
                        break
                    else:
                        print("로그인 실패")
                else:
                    print("로그인 실패")
            elif a == 2:
                self.name = input("MAKE USER NAME >> ")
                while self.name in temp or self.name == '산타':
                    self.name = input("이미 있는 이름입니다 다시 만들어 주세요 >> ")
                pswd = input("PASSWORD >> ")
                self.cur.execute(self.queryADD+'"'+self.name+'"'+","+'"'+pswd+'"'+")" ) 
                self.conn.commit()
                break
        if self.name == 'admin':
            reset.re()
        else:
            print("LOG IN")
    
    def run(self):
        self.curT.execute(self.queryW)
        self.data = self.curT.fetchall()
        self.connT.commit()
        self.chk()
        if self.end == False:
            threading.Timer(0.1,self.run).start()

    def chk(self):
        if self.data[1]['ox'] == 1:
            self.USED.append(self.data[1]['Lword'])
            self.count += 1
            if self.count == 1:
                print()
                print(self.data[1]["user"],"님이 성공했습니다.")
                print()
                print()

        elif self.data[0]["Lword"] != self.curWord:
            self.count = 0
            print(">> ",self.data[0]["Lword"])
            print("다음 단어 : ",end='')
            self.curWord = self.data[0]["Lword"]

        if self.data[1]['user'] == self.name and self.count >= 15:
            '''
            self.count = 0
            print(">> ",self.data[0]["Lword"])
            print("다음 단어 : ",end='')
            self.curWord = self.data[0]["Lword"]
            '''
            self.curT.execute("update gamelog set user = '산타', ox = 0 where idx = 2")

    def corr(self,d):
        if self.data[1]['ox'] == 0:
            self.cur.execute("update gamelog set user =" +'"'+self.name+'"'+",Lword ="+'"'+d+'"'+", ox = 1 where idx = 2")
            self.conn.commit()
            self.cur.execute("update gamelog set user =" +'"'+self.name+'"'+",Lword ="+'"'+d+'"'+" where idx = 1")
            self.conn.commit()