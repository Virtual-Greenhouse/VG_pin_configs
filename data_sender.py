#sends data
from loguru import logger
import socket
import libregpio as GPIO
# from time import sleep
import socket
import busio
import board
import time
from adafruit_bme280 import basic as adafruit_bme280
from data_packer import DataPacker
import config

HOST = config.host_key
PORT = config.port_key
ID = config.tato_id
light = GPIO.OUT('GPIOX_5')

logger.info("potato cannon launch")

# sensor enviro
i2c = busio.I2C(board.SCL1, board.SDA1)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
#sensor soil

#controller_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#controller_sock.connect(("1234", 1234))

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    temp = bme280.temperature
    hum = bme280.humidity
    alt = bme280.altitude
    pres = bme280.pressure
    data_packer = DataPacker(ID, temp, hum, alt, pres).make_json()+'\n'
    logger.info("sending data packet {}".format(data_packer))
    sock.sendall(bytes(data_packer, 'utf-8'))
    # this logic handles data comming in to act out tato functions (test)
    server_response = sock.recv(512).decode()
    # this is some kind of logger logic (should look up more about)
    logger.debug("server said: [{}]".format(server_response))
    if server_response == "light_on\n":
        light.high()
        logger.info("light is on")
    elif server_response == "light_off\n":
        light.low()
        logger.info("light is off")
    ###### -------------------------- end of test
    sock.close()
    time.sleep(3)

    ###this goes in data_reciver.py