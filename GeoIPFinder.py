import json
import requests
import subprocess

msg = 'ip-geo data fetcher'
subprocess.call('clear',shell=True)

print()
print(msg.upper())
print('-' * len(msg))
print()

ip = input('Enter Your Ip-Address : ')
print('')
if ip:
  searchString = 'https://freegeoip.net/json/'+ip
  reply = requests.get(searchString)
  jsonData = reply.json()
  print('{:<15}{:^3}{}'.format('Country Code',':',jsonData['country_code']))
  print('{:<15}{:^3}{}'.format('City',':',jsonData['city']))
  print('{:<15}{:^3}{}'.format('Country Name',':',jsonData['country_name']))
  print('{:<15}{:^3}{}'.format('IP',':',jsonData['ip']))
  print('{:<15}{:^3}{}'.format('Region Name',':',jsonData['region_name']))
  print()
else:
  print(': Empty Ip-address.')
