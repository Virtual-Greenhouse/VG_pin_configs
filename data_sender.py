#sends data
from loguru import logger
import socket
import libregpio as GPIO
from time import sleep
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

logger.info("potato cannon launch")

i2c = busio.I2C(board.SCL1, board.SDA1)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

relay = GPIO.OUT('GPIOX_5')
relay.low()

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
    server_response = sock.recv(512)
    logger.debug("server said: [{}]".format(server_response))
    sock.close()
    time.sleep(3)