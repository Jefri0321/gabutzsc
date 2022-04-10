
import requests
import time,os,sys
# clear
os.system('clear')
# logo
print (' _____________________________________')
print ('[+] creator :andvand31')
print ('[+] youtube :andvand ch')
print ('[+] sc ini dibuat pada jumat 8 april')
print (' _____________________________________')
print ('[+] jangan lupa sub andvand ch 🗿🗿🗿')
print ('[+] sc ini bisa merusak pertemanan 🗿')


# run nomor
print ('nomor diawali dengan 8xxxxxxxx')
nomor=input('[+] nomor target :v :')
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
if 'terkirim' in req:
     print ('[√] spam sms & call terkirim')
else:
     print ('[!] spam gagal')
print ('---------------------------------')


# exit
os.system('exit')

print ('aowkaowkowkaowk')
