#!/bin/sh

# TODO: Windows steps readme (+ IE/Edge)
# TODO: OSX steps readme (+ Safari)

# base utils
apt-get -y install wget unzip python-pip

# Xvfb
apt-get -y install xvfb

# Python libraries
apt-get -y install python-pil imagemagick
pip install pyscreenshot selenium xvfbwrapper pytest

# Firefox
apt-get -y install firefox

# Chrome
wget -q -O - "https://dl-ssl.google.com/linux/linux_signing_key.pub" | apt-key add -
echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list
apt-get -y update
apt-get -y install google-chrome-stable

## Chrome driver
wget "http://chromedriver.storage.googleapis.com/2.21/chromedriver_linux64.zip"
unzip chromedriver_linux64.zip
chmod +x chromedriver
mv chromedriver /usr/local/bin
rm chromedriver_linux64.zip

# # Opera TODO
# ## Opera driver
# wget "https://github.com/operasoftware/operachromiumdriver/releases/download/v0.2.2/operadriver_linux64.zip"
# unzip operadriver_linux64.zip
# chmod +x operadriver
# mv operadriver /usr/local/bin
# rm operadriver_linux64.zip
