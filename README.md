# Samil InfluxDB Stats Collector
## About
Script collection for monitoring older Samil Solar River inverters using the RS232 (serial) connection, and logging data to InfluxDB.

### Credits
- [Logging Solar Inverter Output with a Raspberry Pi](https://lucascosti.com/blog/2017/08/logging-solar-inverter-output-with-a-raspberry-pi/) by Lucas Costi
- [inverter_monitor Perl Scripts](https://github.com/trollkarlen/inverter_monitor) by trollkarlen
- [	Publishing Solar River inverter stats using a Raspberry PI computer](https://cqlug.linux.org.au/node/219) by belly
- [CMS200 Inverter RS232 Serial Port Hack Thread (now offline)](http://www.solarfreaks.com/cms2000-inverter-rs232-serial-port-hack-cms-2000-rs232-t271-240.html#p3410)

### Supported Models
- SolarRiver 3600TL (my inverter)
- SolarRiver SP2200

*Please raise an issue if it works for you and your inverter is not listed!*

## Requirements
- A RS232 to USB or UART adapter
- Raspberry Pi (or similar) running a modern version of Linux
- A Samil SolarRiver inverter with RS232

## Installation
You will need:
- Git
- Python3 and Pip3
- Perl
- Various Packages

### Installing System Requirements
To install Git, Perl and Pip 
```bash
sudo apt install git perl python3 python3-pip
```

Next, install the Perl and Python dependencies
```bash
sudo cpan # This will drop you in to the CPAN shell
install AppConfig Device::SerialPort HTTP::Request::Common LWP::UserAgent
exit
pip3 install influxdb configparser
```

Lastly, clone the repository (replace /home/pi with the directory you want)
```bash
cd /home/pi
git clone https://github.com/kevdagoat/samil-influxdb-collector ii
```

## Usage

Simply run:
```bash
/home/pi/ii/run.sh
```
and the process will be spawned in the background.

To make this process automatic, I suggest using a crontab.
In my case, I have set it to start at 6am. Make sure this isn't before the start time defined in config.ini as it will instantly fail!
```bash
* 6 * * * /home/pi/ii/run.sh
```

## Configuration
In `influx.ini` is the InfluxDB connector configuration and `config.ini` contains the polling perl script configuration.