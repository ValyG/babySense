from wia import Wia
import time
from sense_hat import SenseHat  
import os

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

    print 'Temperature: ', str(t)
    print '\n'
    print 'Pressure: ', str(p)
    print "\n"
    print 'Humidity: ', str(h)
    print '\n'
    time.sleep(1)
    os.system('clear')
    
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
wia.access_token = 'Wia_secret_key'
#here I intended to work on a piece of code which activates sound via bluetooth... but due to lack of time related to my newborn I ended up suspending this idea :)
timestamp=[0,0,0,0]
i=0
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
        start= time.time()
        
    
        while (init_val[0]!=sens_val[0] or init_val[1]!=sens_val[1] or init_val[2]!=sens_val[2]):
            end = time.time()
            elapsed=end-start
            
            if 3 < elapsed :
                print 'Baby moving since :',elapsed
                timestamp[i]=time.time()
                i=i+1
                if  i >= 3 and (timestamp[3]-timestamp[0]<=15):
                    wia.Event.publish(name='ALERT!',data='Baby is awake!!!')
                    print 'Baby awake event published to Wia'
                    timestamp=[0,0,0,0]
                    i=0
                    break
        
            init_val= sens_val
            time.sleep(1.8)
            acceleration = sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            x=round(x, 0)
            y=round(y, 0)
            z=round(z, 0)
            sens_val= [x,y,z]
        
    sensors_value_display()
    
    