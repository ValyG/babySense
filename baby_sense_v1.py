from wia import Wia
import time
from sense_hat import SenseHat  

import numpy as np

sense = SenseHat()
sense.clear()

def sensors_value_display():
    # Take readings from all three sensors
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    # Round the values to one decimal place
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
      
    # Create the message
    # str() converts the value to a string so it can be concatenated
    #message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
      
    # Display the scrolling message on PI's LED's
    #sense.show_message(message, scroll_speed=0.04)
    
    print 'Temperature: ', str(t)
    print '\n'
    print 'Pressure: ', str(p)
    print "\n"
    print 'Humidity: ', str(h)
    print '\n'
    return
acceleration = sense.get_accelerometer_raw()
x = acceleration['x']
y = acceleration['y']
z = acceleration['z']

x=round(x, 0)
y=round(y, 0)
z=round(z, 0)
init_val=[x,y,z]

wia = Wia()
wia.access_token = 'here_will_come_my_access_token'

while True :
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)
    sens_val= [x,y,z]
    if (init_val[0]!=sens_val[0] or init_val[1]!=sens_val[1] or init_val[2]!=sens_val[2]):
        
        start = time.time()
        while (init_val[0]!=sens_val[0] or init_val[1]!=sens_val[1] or init_val[2]!=sens_val[2]):
            end = time.time()
            elapsed = end - start
            print 'elapsed :',(elapsed)
            
            if elapsed >= 10:
                print 'WARNING! BABY IS AWAKE! :) '
                wia.Event.publish(name='alert',data='Baby is awake!')
                
                ''' here I will work on a piece of code where sound will be triggered via bluetooth'''
                break
            init_val= sens_val
            time.sleep(10)
            acceleration = sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            x=round(x, 0)
            y=round(y, 0)
            z=round(z, 0)
            sens_val= [x,y,z]
        
            
    sensors_value_display()
    
    
