#!/bin/sh
cd /home/pi/ii
nohup perl /home/pi/ii/inverter.pl > /tmp/solar.log &
