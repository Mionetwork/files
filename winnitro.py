import random 
import string
import requests
import time
while True:
	proxies = {
	"https":"190.110.222.51:999"
	}
	letters = string.digits + string.ascii_uppercase
	randomString1 =  ''.join(random.choice(letters)  for i in range(5))
	randomString2 = randomString1 +''.join(random.choice(letters)  for i in range(5))
	randomString = randomString2 +''.join(random.choice(letters)  for i in range(5)) 
	nitroscode = "https://discordapp.com/api/v6/entitlements/gift-codes/" + randomString + "?with_application=false&with_subscription_plan=false&country_code=US"
	r = requests.get(nitroscode,)
	if "Unknown Gift Code" in r.text:
		print("Dont Work Code  " + randomString )
		time.sleep(2)
	elif "You are being rate limited" in r.text:
		print("Rate Limited Waiting")
		time.sleep(15) #15 saniye bekliyor
	else:
		print("Work Code " + randomString)
		time.sleep(2)
		url = "https://discordapp.com/api/webhooks/728568696410341387/TY-vhYBCPvQX6UZdzN-35KhAJNJ7cpVGn6YUm5mBoB5GK3fJVHn2bjL9O3iXMIH1BD88"

		data = {}
		
		data["content"] = ""
		data["username"] = "KokoBot"
		
		
		data["embeds"] = []
		embed = {}
		embed["description"] = "" + randomString
		embed["title"] = "Game Code"
		data["embeds"].append(embed)
		
		result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
		
		try:
		    result.raise_for_status()
		except requests.exceptions.HTTPError as err:
		    print(err)
		else:
		    print("Payload delivered successfully, code {}.".format(result.status_code))	
