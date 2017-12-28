#Mangeable Traffic Lights

#By: Yousuf A

import onionGpio
from time import sleep
import sys



if len(sys.argv)==5:
 print("You have selected: " + sys.argv[1] + " to be lit first followed by "+ sys.argv[2] + " and " + sys.argv[3] + " and delay of "+ sys.argv[4]+ " seconds. **BETA Version**")
else:
 print("Insufficient number of arguments! Please enter the color codes and the delay time in the follwing form: color_1 color_2 color_3 delay_time_(ms)")



# Assign GPIO Pins
# Please make sure that the LEDs are connected to these pins
redPin=0
yellowPin=1
greenPin=2

off=1
on=0

# create colored LED objects

red=onionGpio.OnionGpio(redPin)
yellow=onionGpio.OnionGpio(yellowPin)
green=onionGpio.OnionGpio(greenPin)


color=[sys.argv[1],sys.argv[2],sys.argv[3]]
delay=int(sys.argv[4])

i=0
y=1

while (i<=2 and y<=10000):
 if color[i]=="green":
  print("Signal: GREEN")
  red.setOutputDirection(off)
  yellow.setOutputDirection(off)
  green.setOutputDirection(on)
 elif color[i]=="yellow":
  print("Signal: YELLOW")
  yellow.setOutputDirection(on)
  green.setOutputDirection(off)
  red.setOutputDirection(off)
 elif color[i]=="red":
  print("Signal: RED")
  red.setOutputDirection(on)
  yellow.setOutputDirection(off)
  green.setOutputDirection(off)
 else:
  print("The color you have entered is not valid. Please make sure you have entered the colors with correct spelling and all caps-down letters.")
  print("The valid colors are:")
  print("green")
  print("yellow")
  print("red")
 sleep(delay)
 y=y+1
 if i==2:
  i=-1
 i=i+1

print("By: Yousuf A")