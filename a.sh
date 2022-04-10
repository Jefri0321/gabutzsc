#!/bin/bash

clear

blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'


echo $blue"###################################################"
toilet -f mini -F gay prank call
echo $green"###################################################"
echo
echo $white"ketik b untuk kembali"
echo $white"no target dimulai dari 8xxxxx"
echo
read -p "Target : " no;
curl -s https://id.jagreward.com/member/verify-mobile/$no/ > /dev/null 2>&1


if [ $? -eq 0 ]; then
echo "[*] Done"
else
echo "[-] Error"
fi

if [ $no = b ] || [ $no = b ]
then
toilet -f mini -F gay loading...
sleep 3
sh bot.sh
fi

