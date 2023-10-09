import requests
import random
import time


url = "https://camo.githubusercontent.com/372ebfb40b1316d44bf6914d6134178c9ec06d92dd1265788a21c4074ec158c7/68747470733a2f2f6769746875622d726561646d652d73747265616b2d73746174732e6865726f6b756170702e636f6d2f3f757365723d6a726f6c6c6572333326"

response = requests.get(url)

# with open(f"test_response.txt", 'a') as f:
#     f.write(f"{response.text.splitlines()[1]}\n")



print(response.text.splitlines()[35].strip())
