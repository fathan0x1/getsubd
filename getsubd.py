# GetSubd tool for discover subdomains
# Coded by fathan0x1
# 27 April 2019
# updated 12 february 2021

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
	api = "https://sonar.omnisint.io/subdomains/{}".format(url)
	json_data = requests.get(api).json()
	if ask == "Y" or ask == "y":
		with open('{}.txt'.format(url), 'w') as f:
			for i in json_data:
				print(i)
				f.write("{}\n".format(i))
			print("\nsudomains are saved in: {}.txt!".format(url))
	else:
		for i in json_data:
			print(i)

if __name__ == "__main__":
	main(url)
