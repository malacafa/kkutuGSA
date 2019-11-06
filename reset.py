import pymysql

def re():
    admin = pymysql.connect(host = "", port =  , user = "", passwd = "", db = "", charset="")
    cur = admin.cursor(pymysql.cursors.DictCursor)
    cur.execute("update gamelog set ox = 0 where idx = 2")
    admin.commit()
    cur.execute('update gamelog set Lword = "사과" where idx = 1')
    admin.commit()
    print("ADMIN LOGIN DB RESET")

if __name__ == "__main__":
    re()