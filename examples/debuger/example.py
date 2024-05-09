import requests

s = "Hello World"

import pdb; pdb.set_trace()

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)
