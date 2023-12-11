import time
import machine
import network
import dht
import urequests

SSID = "IoT_Case"
PASSWORD = "qweqweqwe"

sensor = dht.DHT11(machine.Pin(5))
rele = machine.Pin(19, machine.Pin.OUT)


def connect_Wifi():
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        print("Already connected")

    station.active(True)
    station.connect(SSID, PASSWORD)

    while station.isconnected() == False:
        pass


def send_data(temp, hum):
    urequests.get(
        f"http://vps.levandrovskiy.ru:7070/send?temp={temp}&hum={hum}")


connect_Wifi()

while True:
    print("cycle")
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    send_data(temp, hum)
    time.sleep(2)
