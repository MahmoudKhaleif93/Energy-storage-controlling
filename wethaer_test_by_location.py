from weather import Weather, Unit 
import time
import RPi.GPIO as GPIO
import dht11
import datetime

# the interface for the user 
weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('duisburg')
condition = location.condition
print("Todys's weather is ")
print(condition.text)

if condition.text== "Partly Cloudy" :
  print("the wind turbin activiated ")
  import RPi.GPIO as GPIO
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(2, GPIO.OUT)
  GPIO.output(2, GPIO.HIGH)
  GPIO.output(2, GPIO.LOW)
  GPIO.setup(9, GPIO.OUT)
  GPIO.output(9, GPIO.HIGH)
  GPIO.output(9, GPIO.LOW)
  print ("relay 1 and 8 are on ")
  #sensor code to measure the temperature andf humidity
  instance = dht11.DHT11(pin=14)
  result = instance.read()
  print("Last valid input: " + str(datetime.datetime.now()))
  print("Temperature: %d C" % result.temperature)
  print("Humidity: %d %%" % result.humidity)
  time.sleep(5);
  GPIO.cleanup()
elif condition.text== "Cloudy":
  print("the wind turbin activiated ")
  import RPi.GPIO as GPIO
  instance = dht11.DHT11(pin=14)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(2, GPIO.OUT)
  GPIO.output(2, GPIO.HIGH)
  GPIO.output(2, GPIO.LOW)
  GPIO.setup(9, GPIO.OUT)
  GPIO.output(9, GPIO.HIGH)
  GPIO.output(9, GPIO.LOW)
  print ("relay 1 and 8 are on ")
  #sensor code to measure the temperature andf humidity
  result = instance.read()
  print("Last valid input: " + str(datetime.datetime.now()))
  print("Temperature: %d C" % result.temperature)
  print("Humidity: %d %%" % result.humidity)
  time.sleep(50);
  GPIO.cleanup()
elif condition.text== "Mostly Cloudy":
  print("the wind turbin activiated ")
  import RPi.GPIO as GPIO
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(2, GPIO.OUT)
  GPIO.output(2, GPIO.HIGH)
  GPIO.output(2, GPIO.LOW)
  GPIO.setup(9, GPIO.OUT)
  GPIO.output(9, GPIO.HIGH)
  GPIO.output(9, GPIO.LOW)
  print ("relay 1 and 8 are on ")
  #sensor code to measure the temperature andf humidity
  instance = dht11.DHT11(pin=14)
  result = instance.read()
  print("Last valid input: " + str(datetime.datetime.now()))
  print("Temperature: %d C" % result.temperature)
  print("Humidity: %d %%" % result.humidity)
  time.sleep(25);
  GPIO.cleanup()
elif condition.text== "sunny" or "Mostly Sunny":
    print("solar panel  activiated ")
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(10, GPIO.OUT)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(10, GPIO.LOW)
    GPIO.setup(3, GPIO.OUT)
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    print ("relay 3 , 10 are on ")
    #sensor code to measure the temperature andf humidity
    instance = dht11.DHT11(pin=14)
    result = instance.read()
    print("Last valid input: " + str(datetime.datetime.now()))
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
    time.sleep(50);
    GPIO.cleanup()
elif condition.text== "Breezy":
  print("the wind turbin activiated ")
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(9, GPIO.OUT)
  GPIO.output(9, GPIO.HIGH)
  GPIO.output(9, GPIO.LOW)
  GPIO.setup(2, GPIO.OUT)
  GPIO.output(2, GPIO.HIGH)
  GPIO.output(2, GPIO.LOW)
  print ("relay 1 , 8 are on ")
  #sensor code to measure the temperature andf humidity
  instance = dht11.DHT11(pin=14)
  result = instance.read()
  print("Last valid input: " + str(datetime.datetime.now()))
  print("Temperature: %d C" % result.temperature)
  print("Humidity: %d %%" % result.humidity)
  time.sleep(50);
  GPIO.cleanup()
elif condition.text== "Rain" or "Scattered showers" or "showers":
  print("the wind turbin activiated ")
  print("the Solar panels  deactiviated ")
  import RPi.GPIO as GPIO
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(9, GPIO.OUT)
  GPIO.output(9, GPIO.HIGH)
  GPIO.output(9, GPIO.LOW)
  GPIO.setup(2, GPIO.OUT)
  GPIO.output(2, GPIO.HIGH)
  GPIO.output(2, GPIO.LOW)
  print ("relay 1 , 8 are on ")
  #sensor code to measure the temperature andf humidity
  instance = dht11.DHT11(pin=14)
  result = instance.read()
  print("Last valid input: " + str(datetime.datetime.now()))
  print("Temperature: %d C" % result.temperature)
  print("Humidity: %d %%" % result.humidity)
  time.sleep(50);
  GPIO.cleanup()
elif condition.text== "clear":
  print("the wind turbin activiated ")
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(9, GPIO.OUT)
  GPIO.output(9, GPIO.HIGH)
  GPIO.output(9, GPIO.LOW)
  GPIO.setup(2, GPIO.OUT)
  GPIO.output(2, GPIO.HIGH)
  GPIO.output(2, GPIO.LOW)
  print ("relay 1 , 8 are on ")
  #sensor code to measure the temperature andf humidity
  instance = dht11.DHT11(pin=14)
  result = instance.read()
  print("Last valid input: " + str(datetime.datetime.now()))
  print("Temperature: %d C" % result.temperature)
  print("Humidity: %d %%" % result.humidity)
  time.sleep(50);
  GPIO.cleanup()
  # taking a decision depending on the imported data by sensor
elif result.temperature ==23:
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(27, GPIO.OUT)
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(27, GPIO.LOW)
      print("relay 27 is on ")
      time.sleep(14)
      GPIO.cleanup()
  
else :
  print("there is an error in the system ")
