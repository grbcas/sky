#!/bin/bash
# Задание 1
cd /
ls > ~/root_files.txt
# Задание 2
ls /usr/sbin/ /usr/bin/ | grep user | sort | tee ~/user_cmd.txt
# Задание 3
export MY_USER=MY_USER
export MY_PASSWORD=MY_PASSWORD
echo "env | grep -P 'MY_USER|MY_PASSWORD'"
env | grep -P 'MY_USER|MY_PASSWORD'
echo $MY_USER
echo $MY_PASSWORD
# Задание 4
sudo apt install python3
echo -e "#!/usr/bin/python3\nprint('Hello from Linux!')" > ~/filechmod +x ~/file
~/file
tree ~/project/
# ./task_10_2.sh > ~/task_10_2.txt
