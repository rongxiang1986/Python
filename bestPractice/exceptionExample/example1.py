
from requests.exceptions import ConnectionError, ReadTimeout
import requests

import builtins
builtins_list = dir(builtins)

error_list = [item for item in builtins_list if 'Error' in item]
print(error_list)
print(len(error_list))

print(dir(requests.exceptions))



try:
    print(0/1)
except Exception as a:
    print(a)