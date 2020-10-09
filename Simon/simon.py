import RPi.GPIO as GPIO
from random import randint
from time import sleep

RED_LED = 26 #insert pin number
GREEN_LED = 13 #insert pin number
BLUE_LED = 6 #insert pin number
YELLOW_LED = 19 #insert pin number
RED_BUTTON = 21 #insert pin number
GREEN_BUTTON = 16 #insert pin number
BLUE_BUTTON = 12 #insert pin number
YELLOW_BUTTON = 20 #insert pin number
BUZZER = 5 #insert pin number
RED_FREQUENCY = 150
YELLOW_FREQUENCY = 175
GREEN_FREQUENCY = 200
BLUE_FREQUENCY = 225

def setup():
    ##### SETUP
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    ########## SETUP LED
    GPIO.setup(RED_LED, GPIO.OUT) #red LED
    GPIO.setup(GREEN_LED, GPIO.OUT) #green LED
    GPIO.setup(BLUE_LED, GPIO.OUT) #blue LED
    GPIO.setup(YELLOW_LED, GPIO.OUT) #yellow LED
    ########## SETUP BUTTONS
    GPIO.setup(RED_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #redButton
    GPIO.setup(GREEN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #greenButton
    GPIO.setup(BLUE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #blueButton
    GPIO.setup(YELLOW_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #yellowButton
    ########## SETUP BUZZER
    GPIO.setup(BUZZER, GPIO.OUT)
    #####
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(YELLOW_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(BLUE_LED, GPIO.LOW)

##### addLight()
##### returns the PINNUMBER of a random light
#####     return PINNUMBER
##### print an error and exit in case of failure
def addLight():
    light = randint(0,3)
    if(light == 0):
        return RED_LED
    if(light == 1):
        return GREEN_LED
    if(light == 2):
        return BLUE_LED
    if(light == 3):
        return YELLOW_LED
    print("Error on rand")
    exit()

##### prints "cpt" args and light up the 4 LEDs for 1 sec
def close(cpt,buzz):
    print("Score :")
    print(cpt)
    b=binary(cpt)
    sleep(0.5)
    f=250
    for i in range(0,3):
        GPIO.output(RED_LED, GPIO.HIGH)
        GPIO.output(YELLOW_LED, GPIO.HIGH)
        GPIO.output(GREEN_LED, GPIO.HIGH)
        GPIO.output(BLUE_LED, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(RED_LED, GPIO.LOW)
        GPIO.output(YELLOW_LED, GPIO.LOW)
        GPIO.output(GREEN_LED, GPIO.LOW)
        GPIO.output(BLUE_LED, GPIO.LOW)
        sleep(0.1)
    if b[0]:
        GPIO.output(RED_LED, GPIO.HIGH)
    if b[1]:
        GPIO.output(YELLOW_LED, GPIO.HIGH)
    if b[2]:
        GPIO.output(GREEN_LED, GPIO.HIGH)
    if b[3]:
        GPIO.output(BLUE_LED, GPIO.HIGH)
    for i in range(0,4):
        buzz.ChangeFrequency(f)
        buzz.start(0.2)
        sleep(0.5)
        f=f-50
    sleep(0.5)
    buzz.stop()
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(YELLOW_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(BLUE_LED, GPIO.LOW)
    GPIO.cleanup()
    exit()

##### newStep()
##### blink 3 times the 4 LEDs and decrease the waitingTime between each light of the game
def newStep(cpt,wT,sT):
    sleep(0.5)
    GPIO.output(RED_LED, GPIO.HIGH)
    GPIO.output(YELLOW_LED, GPIO.HIGH)
    GPIO.output(GREEN_LED, GPIO.HIGH)
    GPIO.output(BLUE_LED, GPIO.HIGH)
    sleep(1)
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(YELLOW_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(BLUE_LED, GPIO.LOW)
    sleep(0.5)
    wT = wT - 0.6
    if(wT<0.1):
        wT=0.05
        sT=sT-0.01
    sleep(1)
    return (cpt+1,wT,sT)

def binary(i):
    ret=[0,0,0,0]
    cpt=3
    while i>0:
        if i%2!=0:
            ret[cpt]=1
        else:
            ret[cpt]=0
        i=i//2
        cpt=cpt-1
    return ret

def main():
    setup()
    isGameOver=False
    simon=[]
    cpt=0
    score=[0,0,0,0]
    sleepingTime=0.8
    waitingTime=1
    score=[0,0,0,0]
    buzz=GPIO.PWM(BUZZER,1)
    while(not isGameOver):
        simon.append(addLight())

        ##### light on the game's lights
        for light in simon:
            GPIO.output(light, GPIO.HIGH)
            if light==RED_LED:
                buzz.ChangeFrequency(RED_FREQUENCY)
            if light==YELLOW_LED:
                buzz.ChangeFrequency(YELLOW_FREQUENCY)
            if light==GREEN_LED:
                buzz.ChangeFrequency(GREEN_FREQUENCY)
            if light==BLUE_LED:
                buzz.ChangeFrequency(BLUE_FREQUENCY)
            buzz.start(0.5)
            sleep(sleepingTime)
            buzz.stop()
            GPIO.output(light, GPIO.LOW)
            sleep(waitingTime)

        ##### verify that the button pressed correspond to the light's sequence
        for light in simon:
            button = -1
            while button==-1:
                while(GPIO.input(RED_BUTTON)==GPIO.HIGH):
                    button=RED_LED
                    buzz.ChangeFrequency(RED_FREQUENCY)
                    buzz.start(0.2)
                while(GPIO.input(YELLOW_BUTTON)==GPIO.HIGH):
                    button=YELLOW_LED
                    buzz.ChangeFrequency(YELLOW_FREQUENCY)
                    buzz.start(0.2)
                while(GPIO.input(GREEN_BUTTON)==GPIO.HIGH):
                    button=GREEN_LED
                    buzz.ChangeFrequency(GREEN_FREQUENCY)
                    buzz.start(0.2)
                while(GPIO.input(BLUE_BUTTON)==GPIO.HIGH):
                    button=BLUE_LED
                    buzz.ChangeFrequency(BLUE_FREQUENCY)
                    buzz.start(0.2)
                buzz.stop()
            if light != button:
                isGameOver=True
                close(cpt,buzz)
        cpt,waitingTime,sleepingTime = newStep(cpt,waitingTime,sleepingTime)

main()
