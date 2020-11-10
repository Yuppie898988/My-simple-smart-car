import requests
import json
from gps import position
import csv

def offline(command):
    with open('map.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == command:
                content = row[1] + ',' + row[2]
                file.close()
                return content
        return position()
                
def search(command):
    url = 'https://restapi.amap.com/v3/assistant/inputtips'
    param = {
        'key': '86f57253595c25780dfde71826b7d883',
        'keywords': command,
        'location': position()
    }
    res = requests.get(url, params=param)
    content = json.loads(res.text)['tips'][0]['location']
    return content

def plan(des_name):
    url = 'https://restapi.amap.com/v4/direction/bicycling'
    param = {
        'key': '86f57253595c25780dfde71826b7d883',
        'origin': position(),
        'destination': search(des_name)  # 若选择导入数据集模式需要更改函数为offline(des_name)
    }
    res = requests.get(url=url, params=param)
    content = json.loads(res.text)['data']['paths'][0]['steps']
    return content
