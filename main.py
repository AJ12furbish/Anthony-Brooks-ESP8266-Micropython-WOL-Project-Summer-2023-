import network
import machine
import socket
from time import sleep
from time import sleep_ms
from machine import Pin

d2 = Pin(4, Pin.OUT)

def connectToWifi(ssid, password):
    d2.off()
    sleep(1)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Connected to Wi-Fi:', wlan.ifconfig())
    d2.on()
    
def sendWOLPacket(mac_address):
    packet = b'\xff' * 6 + mac_address * 16
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.sendto(packet, ('Broadcast IP', 9))
    sock.close()
    
def flashLED(count):
    for _ in range(count):
        d2.off()
        sleep_ms(500)
        d2.on()
        sleep_ms(500)
    
connectToWifi('SSID', 'Password')
targetMac = b'\x11\x22\x33\x44\x55\x66'
d1 = Pin(5, Pin.IN)

while True:
    if d1.value():
        sendWOLPacket(targetMac)
        flashLED(4)
        


    
    