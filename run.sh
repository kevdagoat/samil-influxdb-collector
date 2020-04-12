#!/bin/sh
#
# Samil InfluxDB Collector Script
# Copyright Kevdagoat 2020
#
# You will have to change the paths in here to reflect the directories in which these files are located
#

cd /home/pi/ii
nohup perl /home/pi/ii/inverter.pl > /tmp/solar.log &
