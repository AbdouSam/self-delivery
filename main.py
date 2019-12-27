from DataClasses import *
from controller import *
from inputlcd import *
from time import sleep

NO_PRODUCT = "NO_PRODUCT"
RECEIVED = "RECEIVED"
DELIVERED = "DELIVERED"
TAKEN_BACK = "TAKEN_BACK"

#LCD TEXT
STARTING_TEXT    = "Starting ..."
MAIN_ERROR_TEXT  = "Err: Main."
GEN_EXCEPT_TEXT  = "Err:Gen Except"
#main function with some testing code
def main():
  NbrOfUnits = 6 #this number is limited to the Hardware GPIOs
  GeoPosition = "Alger center"
  LockerID = "1b333d"
  DeliveryPassword = ""
  locker = Locker(LockerID,NbrOfUnits,GeoPosition,DeliveryPassword) 

  #Create a list of all Locker Units (Cells) with empty status,
  #Get the last saved file of the Unit stats, which are empty, and which are Occupied
  #get data from the web API, and set it into list of product and delivery pass
  
  # Set Current Time, we use now, for it to be correct.
  
  lcd_print(STARTING_TEXT)
  sleep(2)
  while  True:
    mainProgram(locker)

######### Main ##############
if __name__ == '__main__':
  while True:
    try:
      main()
      # The program should never go beyond this point, main is infinite loop.
    except Exception:
      lcd_print(GEN_EXCEPT_TEXT)
      
  lcd_print(MAIN_ERROR_TEXT)
  ######### END  ##############
