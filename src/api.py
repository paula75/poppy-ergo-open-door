import requests
import time

IP_ADDRESS = 'http://192.168.1.197'
PORT= '8080'

POPPY_ADDRESS = IP_ADDRESS + ':' + PORT


PRIMITIVE='/primitive'

start= '/start.json'
stop= '/stop.json'


def list_primitives():
    r = requests.get(POPPY_ADDRESS+PRIMITIVE+'/list.json')
    if r.status_code == 200:
        available_primitives = r.json()
        return available_primitives["primitives"]


def do_action(primitive,action):
    r = requests.get(POPPY_ADDRESS+action)
    return r.status_code

def show_us_dance():
    do_action(start_dance)
    time.sleep(10)
    do_action(stop_dance)

# show_us_dance()
list_prim = list_primitives()
print(list_prim)
