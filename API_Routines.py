import requests
import json

g_headers = {'Content-Type': 'application/json'}

g_url = 'https://demo.thingsboard.io/api/v1/HgfxHddxG3uQ5UouiRhx/rpc'

# Check the Validity of client's Pass And ID
def checkPassID_API(in_pass, in_id):
  state = "error"
  box_id = 0
  try:
    url = g_url
    headers = g_headers

    data = '{"method":"checkDelivery", "params": {"pass" :"' \
            + str(in_pass) + '","id" : "' + str(in_id) + '"}}'

    print("Connecting to server ...")
    response = requests.post(url , headers=headers, data=data)

    print("Getting response from server ...")

  except Exception as e:
    print("Error during connection.")
  else:
    #if no exceptions
    try:
      j = json.loads((response.content).decode())
      state = j['response']
      box_id = j['box_id']
      box_id = (int(box_id) - 1) # zero based calculation

      print("State = " + state + ", box_id = " + str(box_id))
    except Exception as e:
      print("Coudn't Parse Data")


  finally:
    return state, int(box_id)

# Check the validity of Delivery Guy password
def checkLivreurPass_API(in_pass):
  state = "error"
  try:
    url = g_url
    headers = g_headers

    data = '{"method":"checkLivreur", "params": {"pass" :"' + str(in_pass) + '"}}'

    print("Connecting to server ...")
    response = requests.post(url , headers=headers, data=data)

    print("Getting response from server ...")

  except Exception as e:
    print("Error during connection.")
  else:
    #if no exceptions
    try:
      j = json.loads((response.content).decode())
      state = j['response']
      print("State = " + state)

    except Exception as e:
      print("Coudn't Parse Data")
  finally:
    return state

# Send a dummy byte (ID of locker) every 5 minute to the server
def lockerAlive_API():
  try:
    url = g_url
    headers = g_headers

    data = '{"method":"lockerAlive", "params": {}}'

    print("Connecting to server ...")
    response = requests.post(url , headers=headers, data=data)

    print("Getting response from server ...")

  except Exception as e:
    print("Error during connection.")
  else:
    print("Response" + str((response.content).decode()))
  

# Update The state of the locker after a client takes his order
def updateProduct_API(box_id, update_state):
  try:
    url = g_url
    headers = g_headers

    data = '{"method":"updateDelivery", "params": {"box_id" : "'\
             + str(box_id) +'", "state":"' + update_state +'"}}'

    print("Connecting to server ...")
    response = requests.post(url , headers=headers, data=data)

    print("Getting response from server ...")
    print("Response" + str((response.content).decode()))

  except Exception as e:
    print("Error during connection.")
  else:
    #if no exceptions
    try:
      j = json.loads((response.content).decode())
      state = j['response']
    except Exception as e:
      print("Cound't Parse Data.")
  return state

# Update the state of the locker after Delivery Guy put the order in the locker
def updateLivreur_API(box_id,update_state):
  try:
    url = g_url
    headers = g_headers

    data = '{"method":"updateDeposit", "params": {"box_id" : "'\
             + str(box_id) +'", "state":"' + update_state +'"}}'

    print("Connecting to server ...")
    response = requests.post(url , headers=headers, data=data)

    print("Getting response from server ...")

    print("Response" + str((response.content).decode()))

  except Exception as e:
    print("Error during connection.")
  else:
    #if no exceptions
    try:
      # If data is in Json format
      j = json.loads((response.content).decode())
      state = j['response']
    except Exception as e:
      # Data is not in json format
      print("Cound't Parse Data.")
  return state
