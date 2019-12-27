#if testing in real pi, use the gpios, if testing in PC use gpios_stub
from gpios import *
#from gpios_stub import *
from time import sleep



#Constant
RELAY_ACT_SEC = 0.2 # 200ms
gpioOutputs = [GPIO_18, GPIO_23, GPIO_24, GPIO_25, GPIO_12, GPIO_13]

gpioInputs  = [GPIO_6, GPIO_5, GPIO_22, GPIO_27, GPIO_17, GPIO_4]

gpioLED = GPIO_26

#Manage the hardware
class RelayBoard:

    def __init__(self,boardID):
        
        
        self.boardID = boardID
        
        init_gpio_mode()
        for _input_ in gpioInputs:
            set_pin_mode(_input_,"INPUT")

        for _output_ in gpioOutputs:
            set_pin_mode(_output_, "OUTPUT")

    def action_relay(self,unitNumberID):
        set_output(gpioOutputs[unitNumberID])
        sleep(RELAY_ACT_SEC)
        clear_output(gpioOutputs[unitNumberID])

    def read_door_state(self,unitNumberID):
        return read_input(gpioInputs[unitNumberID])

    def action_set_led(self):
        set_output(gpioLED)

    def action_clear_led(self):
        clear_output(gpioLED)

