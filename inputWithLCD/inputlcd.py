import tty
import sys
import termios
import lcd_i2c_driver

# LCD Size
LCD_COL = 2
LCD_ROW = 16

# Password text settings
PASSWORD_TEXT = "Password"
PASSWORD_ROW = 1

# Passphrase settings
PASSPHRASE_LEN = 15 # Default length to 15. LCD max is 16 actually. 
PASSPHRASE_ROW = 2

# Other display settings
PROCESSING_TEXT = "Processing..."
PROCESSING_ROW = 1

ERROR_TEXT = "ERROR!"
ERROR_ROW = 1

""" Clear the password row
    No way to clear by a row/col manner.
    So we have to do this dummy clear and rewrite later.
"""
def clearRow(dev, row):
   dev.lcd_display_string("                ", row)

""" Wrapper for keyboard init.
    This function solely exists to make life easier when using another API.
"""
def keyboardInit():
    # Save the current tty settings
    orig_settings = termios.tcgetattr(sys.stdin)

    # Disable line buffering so we can take inputs as we are pressing.
    tty.setcbreak(sys.stdin)

    return orig_settings

""" Wrapper for keyboard read.
    This function solely exists to make life easier when using another API.
"""
def keyboardRead(dev):
    return sys.stdin.read(1)[0]

""" Wrapper for keyboard deinit.
    This function solely exists to make life easier when using another API.
"""
def keyboardDeinit(dev):
    # Restore the original settings (Enable line buffering.)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, dev)

def input_main():
    lcd_dev = lcd_i2c_driver.lcd()

    keyboard_dev = keyboardInit()

    # Init the LCD screen
    lcd_dev.lcd_display_string(PASSWORD_TEXT, PASSWORD_ROW)

    # Where the code will be stored.
    passphrase = ""

    # Used to print * in the LCD instead of the code. (Need to do this?)
    passprint = ""
    
    # Keypress holder
    keypress = 0

    # Listen to key presses until Enter is hit.
    while True:
        try:
            keypress = keyboardRead(keyboard_dev) 
           
            # Enter pressed?
            if keypress == chr(10):
                break

            # Too much is too ugly. Don't bother with scrolling.
            if len(passphrase) >= PASSPHRASE_LEN:
                break

            # Delete key pressed?
            if keypress == chr(0x7f):
                clearRow(lcd_dev, PASSPHRASE_ROW)
                passphrase = passphrase[:-1] # Remove the last character.
                passprint = passprint[:-1]
            else:
                passphrase += str(keypress)
                passprint += '*'
            
            lcd_dev.lcd_display_string(passprint, PASSPHRASE_ROW)

        except KeyboardInterrupt:
            keyboardDeinit(keyboard_dev)
            sys.exit()

    lcd_dev.lcd_clear()
    lcd_dev.lcd_display_string(PROCESSING_TEXT, PROCESSING_ROW)
    keyboardDeinit(keyboard_dev)
    return passphrase

if __name__ == '__main__':
    code = input_main()
    print(code)

