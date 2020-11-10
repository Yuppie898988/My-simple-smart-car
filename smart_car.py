from asr import asr
from tts import tts
from car import Smart_car
from gps import position
from path_planning import plan
import re
import time
direc_index = {'东':0, '南':1, '西':2, '北':3}
if __name__ == '__main__':
    words = asr()
    print(words)
    mycar = Smart_car()
    answer = '正在为您导航至' + re.search(r'去(.*)', words).group(1)
    tts(answer)
    while True:
        orders = plan(re.search(r'去(.*)', words).group(1))[0]["instruction"]
        print(orders)
        try:
            obj = re.search(r'向(.*)骑行(.*)米', orders)
            direction = direc_index[obj.group(1)]
            mycar.control(direction)
            if obj.group(2) < 3:
                continue
            time.sleep(3)
        except AttributeError:
            mycar.forward()
            break;
