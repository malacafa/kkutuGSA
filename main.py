from dbconn import ONLINE
import sys

database = open("database.txt","r",encoding='UTF8')
TEMPWORDLIST = database.read()
WORDLIST = TEMPWORDLIST.split(".")

player = ONLINE()
Lword = player.data[0]["Lword"]

while True:
    Rword = "apple"

    while Rword[0] != Lword[-1]:
        Rword = input()

        if Rword == 'exit':
            print("끄투 GSA를 이용해 주셔서 감사합니다")
            player.end = True
            sys.exit(0)

        Lword = player.data[0]["Lword"]
        USED = player.USED.copy()

        if ord("라") <= ord(Lword[-1]) and ord(Lword[-1]) < ord("마") and ord(Rword[0])-ord(Lword[-1]) == 3528:
            break

        if len(Rword) == 0:
            Rword = "apple"

    if Rword in USED:
        print("사용된 단어입니다")
        continue
                
    if Rword not in WORDLIST:
        print("없는 단어입니다")   
        continue
                
    player.corr(Rword)
    Lword = Rword