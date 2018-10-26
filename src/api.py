import requests
import time

IP_ADDRESS = 'http://192.168.1.197'
PORT= '8080'

POPPY_ADDRESS = IP_ADDRESS + ':' + PORT


movement=['/primitive','/motor']


start= '/start.json'
stop= '/stop.json'


def list_primitives():
    r = requests.get(POPPY_ADDRESS+movement[0]+'/list.json')
    if r.status_code == 200:
        available_primitives = r.json()
        return available_primitives["primitives"]

def do_primitive(list_primitives,action,option):
    if action in list_primitives:
        payload = '/' + action
        payload = POPPY_ADDRESS+movement[0]+payload
        if option=='start':
            payload = payload+start
        else:
            payload = payload+stop
        r = requests.get(payload)
        if r.status_code == 200:
            print('Success!')
            return 1
        else:
            print(r.status_code)
            return 0
    else:
        print(action + ' is not available')
    return 0

def show_us_dance():
    list_prims = list_primitives()
    do_primitive(list_prims,'dance','start')
    time.sleep(10)
    do_primitive(list_prims,'dance','stop')

list_prim = list_primitives()
do_primitive(list_prim, 'get_up_posture','start')
do_primitive(list_prim, 'get_up_posture','stop')
show_us_dance()
