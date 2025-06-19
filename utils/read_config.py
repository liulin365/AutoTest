import yaml

# print(data['heros_name'])

def getdata():

    f = open('../config/data.yaml','r',encoding='utf-8')
    data = yaml.safe_load(f)
    getname = data['heros_name']
    return getname

getdata()

