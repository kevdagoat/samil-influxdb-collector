import sys
import json
import time
from configparser import ConfigParser
from influxdb import InfluxDBClient

config = ConfigParser()
config.read("influx.ini")

if config.getboolean('influx', 'auth'):
        client = InfluxDBClient(host=config['influx']['host'],
                                port=config['influx']['port'],
                                username=config['influx']['user'],
                                password=config['influx']['password'])
else:
        client = InfluxDBClient(host=config['influx']['host'],
                                port=config['influx']['port'])

client.create_database(config['influx']['database'])
client.switch_database(config['influx']['database'])

j = json.loads(sys.argv[1].replace("'", '"'))

pv_volts = float(j['volts_pv'])
pv_amps = float(j['amps_pv'])
pv_power = float(round(pv_volts * pv_amps, 2))

ac_amps = float(j['amp_ac'])
ac_volts = float(j['volts_ac'])
ac_power = float(j['power_ac'])
ac_freq = float(j['freq_ac'])
ac_impedance = float(j['impedance_ac'])

efficiency = float(round(ac_power / pv_power, 5))

energy_today = j['total_today']
energy_total = j['total_energy']
hours_total = j['total_hours']

mode = j['mode']
temp = float(j['temp'])

currtime = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(None))

points = [{
        "measurement": "inverter_realtime",
        "tags": {},
        "time": currtime,
        "fields": {
                "pv_volts": pv_volts,
                "pv_amps": pv_amps,
                "pv_power": pv_power,
                "ac_volts": ac_volts,
                "ac_amps": ac_amps,
                "ac_power": ac_power,
                "ac_freq": ac_freq,
                "ac_impedance": ac_impedance,
                "efficiency": efficiency
        }
        },{
        "measurement": "inverter_stats",
        "tags": {},
        "time": currtime,
        "fields": {
                "energy_today": energy_today,
                "energy_total": energy_total,
                "hours_total": hours_total
        }    
        },{
        "measurement": "inverter_misc",
        "tags": {},
        "time": currtime,
        "fields": {
                "temp": temp,
                "mode": mode
        }}]

client.write_points(points)

