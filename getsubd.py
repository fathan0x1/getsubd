# GetSubd tool for discover subdomains
# Coded by fathan0x1
# 27 April 2019

import requests

print("""
╔═╗┌─┐┌┬┐╔═╗┬ ┬┌┐ ┌┬┐
║ ╦├┤  │ ╚═╗│ │├┴┐ ││
╚═╝└─┘ ┴ ╚═╝└─┘└─┘─┴┘
──────── by fathan0x1
""")

url = input("Insert domain name: ")
ask = input("Do u want to save the results? (Y/n): ")

def main(url):	
	api = "https://api.indoxploit.or.id/domain/{}".format(url)
	json_data = requests.get(api).json()
	get_data = json_data['data']['subdomains']	
	if ask == "Y" or ask == "y":
		with open('{}.txt'.format(url), 'w') as f:
			for i in get_data:
				print(i)
				f.write("{}\n".format(i))
			print("\nsudomains are saved in: {}.txt!".format(url))
	else:
		for i in get_data:
			print(i)

if __name__ == "__main__":
	main(url)
