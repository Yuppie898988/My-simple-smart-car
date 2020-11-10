import gpiozero
import time
turn_wait = 0.38
class Smart_car:
    def __init__(self):
        self.l_motor = gpiozero.Motor(17,18,27)
        self.r_motor = gpiozero.Motor(23,24,22)
        self.l_motor.stop()
        self.r_motor.stop()
        self.direction = 3                  # 导航车默认向北

    def forward(self, speed = 0.5):
        self.l_motor.forward(speed)
        self.r_motor.forward(speed)

    def backward(self, speed = 0.5):
        self.l_motor.backward(speed)
        self.r_motor.backward(speed)

    def turn_right(self, speed = 0.5):
        self.l_motor.forward(speed)
        self.r_motor.forward(speed - 0.1)
        time.sleep(turn_wait)
        self.forward(speed)
    
    def turn_left(self, speed = 0.5):
        self.r_motor.forward(speed)
        self.l_motor.forward(speed - 0.1)
        time.sleep(turn_wait)
        self.forward(speed)
    
    def stop(self):
        self.l_motor.stop()
        self.r_motor.stop()
    
    def control(self, direct):
        if direct == (self.direction + 1) % 4:
            self.turn_right()
        elif direct == (self.direction + 4 - 1) % 4:
            self.turn_left()
        elif direct == self.direction:
            self.forward()
        else:
            self.turn_left()
            self.turn_left()
        self.direction = direct

    def __del__(self):
        self.stop()