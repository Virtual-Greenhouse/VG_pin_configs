import busio
import board
import time
import libregpio as GPIO
import sys
import signal
from loguru import logger

fan = GPIO.OUT('GPIOX_4')
light = GPIO.OUT('GPIOX_5')
humidifier_pump = GPIO.OUT('GPIOX_2')
soil_pump = GPIO.OUT('GPIOX_7')


#interups the program
def signal_handler(sig, frame):
    logger.warning('Program off')
    fan.low()
    light.low()
    humidifier_pump.high()
    soil_pump.high()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:

    fan.high()
    logger.info("fan is on")
    time.sleep(1.0)
    
    fan.low()
    logger.info("fan is off")
    time.sleep(1.0)
    
    light.high()
    logger.info("light is on")
    time.sleep(1.)

    light.low()
    logger.info("light is off")
    time.sleep(1.0)

    #water pumps are inverse so "low" is on and "high" is off

    humidifier_pump.low()
    logger.info("humidifier pump is on")
    time.sleep(1.0)

    humidifier_pump.high()
    logger.info("humidifier pump is off")
    time.sleep(1.0)

    soil_pump.low()
    logger.info("soil pump is on")
    time.sleep(1.0)

    soil_pump.high()
    logger.info("Soil pump is off")
    time.sleep(1.0)

# Class Divices
# F == OFF
# Hum = F 
# water soil = F
# water Hum = F 
# Light = F 


# on_off_light(String)
#