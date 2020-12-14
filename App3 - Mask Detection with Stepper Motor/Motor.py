from RpiMotorLib import RpiMotorLib

#define GPIO pins
GPIO_pins = (14, 15, 18)    # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 20               # Direction Pin, 
step = 21                   # Step Pin
distance = 80               # Default move 1mm => 80 steps per mm


# Declare an named instance of class pass GPIO pins numbers
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")


def up():
    global distance
    print("Move up,", distance, "steps")
    mymotortest.motor_go(False, "Full" , distance, 0.01 , False, .05)
   


def down():
    global distance
    print("Move down,", distance, "steps")
    mymotortest.motor_go(True, "Full" , distance, 0.01 , False, .05)
   
 
# Run the app on the local development server
if __name__ == "__main__":
    up()
    down()