import sys

print(sys.executable)

import requests


r = requests.get('https://api.github.com/users/Sargen3268')
print(r.text)
