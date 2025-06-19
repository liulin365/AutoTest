import yaml

f = open('../config/data.yaml','r',encoding='utf-8')

data = yaml.safe_load(f)
# print(data)
# print(data['hero'])
# print(data['heros_name'])
# print(data['heros'])
# print(data['hero_name_list'])

print(data['test'])

f.close()