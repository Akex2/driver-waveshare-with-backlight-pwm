#!/bin/bash

chmod +x *.sh *.py
sudo apt-get update
sudo apt-get install python-dev python-pip
sudo pip install wheel
#sudo pip install wiringpi2
#sudo pip-3.2 install python-uinput pyudev
sudo apt-get install git-core
#git clone git://git.drogon.net/wiringPi
#cd wiringPi
#git pull origin
#./build
#sudo patch -b /boot/config.txt 7inch.patch
sudo apt-get install -y python3-pip libudev-dev
#sudo pip-3.2 install python-uinput pyudev
#if pip-3.2 can't be found, please use pip3
sudo pip3 install python-uinput pyudev
cd ..

sudo cp touch.py /usr/bin/
sudo cp digitalBB.py /usr/bin/
sudo cp touch.sh /etc/init.d/
sudo cp digitalBB.sh /etc/init.d/
sudo cp toto.txt /usr/bin/

sudo chmod +x /usr/bin/touch.py
sudo chmod +x /usr/bin/digitalBB.py
sudo chmod +x /etc/init.d/touch.sh
sudo chmod +x /etc/init.d/digitalBB.sh

sudo update-rc.d touch.sh defaults
sudo update-rc.d digitalBB.sh defaults
