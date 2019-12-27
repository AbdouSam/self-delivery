# self-delivery
This repo contains the code for the Rasbperry Pi 3 model B. Connecting to thingsbord through Rule chain.

***Written and tested in Python 3.6.6***
**Notes**
* when testing on a PC, comment the import gpio and use gpio_stub in the Hardware.py
* For fast boot disable the GUI on raspi-config
**External dependencies**
* pip3 install requests
* sudo apt install python3-smbus (for the LCD I2C)
* - To be able to use the I2C feature, I2C interface should be enabled using raspi-config -
**Files:**

* helper.py: Empty for now.
* DataClasses.py : Contains the class and structures for the data.
* controller.py : Manages the delivery and reception of products.
* main.py : Contains a test program for product delivery and product reception.
* gpio.py : Contains the definitions of the GPIOs and function to Manage GPIOs
* gpio_stub.py : A Stub to when testing Python on a different machine than the Pi.
* hardware : contains the RelayBoard Class, it serves as an interface to the GPIO module
* key_test : a stand alone program to get key strokes from keyboard
* lcd_test : a stand alone program to test the LCD, Parallel mode not I2C.
* API_Routines: Incomplete Module, serves as the interface to the Web APIs.
* api_test: a stand alone progora to test a send to api using requesets lib.
* inputWithLCD : folder contains library and test code for I2C LCD Keyboard


**API proposition :**
**we use Json Format All Methods are POST:**

    1. API authentification livereur : 
        * locker sends : {"method":"checkLivreur", "params": {"pass" : "123456"}}
        * server respond by {"response" :"valid"}, or {"response" :"Invalid"}'

    2. API authentification Delivery :
        * locker sends : {"method":"checkDelivery", "params": {"pass" : "aaaa","id" : "1121"}}
        * server respond by {"response" :"valid","box_id" :"1"},
        * or {"response" :"Invalid","box_id" :"0"} '0 for when id box is invalid'

    3. API to inform the server about the delivery state :
        *  _Update Product :_
            * {"method":"updateDelivery", "params": {"box_id" : "1", "state":"success"}}
            * {"method":"updateDelivery", "params": {"box_id" : "1", "state":"failure"}}

        * _Update Delivery :_
            * {"method":"updateDeposit", "params": {"box_id" : "1", "state":" success"}}
            * {"method":"updateDeposit", "params": {"box_id" : "1", "state":" failure"}}
- 
