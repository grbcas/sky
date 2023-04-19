#!/bin/bash
cd ~
pwd
ls -la
# задание 2
mkdir -p ~/project/src/
mkdir -p ~/project/tests/
touch ~/project/src/classes.py
touch ~/project/src/utils.py
touch ~/project/tests/config.py
touch ~/project/tests/tests.py
tree ~/project/
# задание 3
rm ~/project/src/utils.py
mv ~/project/tests/config.py ~/project/src/
mv ~/project/tests/tests.py ~/project/tests/test_general_auth.py
# задание 4
cd /var/log/
head -n 50 dpkg.log
tail -n 50 dpkg.log
grep systemd dpkg.log
# задание 5
echo -e "#!/usr/bin/python\nprint('Hello, SkyPro!')" > ~/main.py

# ./task_10_1.py > task_10_1.txt