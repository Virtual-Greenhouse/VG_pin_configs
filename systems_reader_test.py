import time
import libregpio as GPIO


#set pin GPIO_15 to be used as an input for soil sensor
soil_sensor = GPIO.IN('GPIOX_15')

while True:
# read pin value (soil wetness)
  sensor_data = soil_sensor.input()

# print read value (sensor data)
  print(sensor_data)
  time.sleep(0.5) 

# #last thing at runs and will reset the pin back to default value (It's just good practice, but its causing some issues, don't use for now)
# GPIO.cleanup()

