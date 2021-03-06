#!/bin/bash

chmod +x *.sh *.py
sudo apt-get update
sudo apt-get install python-dev python-pip
sudo pip install wiringpi2
sudo pip-3.2 install python-uinput pyudev
sudo apt-get install git-core
git clone git://git.drogon.net/wiringPi
cd wiringPi
git pull origin
./build
#sudo patch -b /boot/config.txt 7inch.patch
sudo apt-get install -y python3-pip libudev-dev
sudo pip-3.2 install python-uinput pyudev
#if pip-3.2 can't be found, please use pip3
#sudo pip3 install python-uinput pyudev
cd ..

sudo cp touch.py /usr/bin/
sudo cp pwm.py /usr/bin/
sudo cp touch.sh /etc/init.d/
sudo cp pwm.sh /etc/init.d/
sudo cp toto.txt /usr/bin/

sudo chmod +x /usr/bin/touch.py
sudo chmod +x /usr/bin/pwm.py
sudo chmod +x /etc/init.d/touch.sh
sudo chmod +x /etc/init.d/pwm.sh

sudo update-rc.d touch.sh defaults
sudo update-rc.d pwm.sh defaults

