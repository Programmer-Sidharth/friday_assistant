import requests
import random
url = 'https://sidharthfridayassistant.pythonanywhere.com/api/all/?format=json'

r = requests.get(url)

data = r.json()

def response(line):
	result = []
	for values in data:
		valuesList = values['hotwords'].split('|')
		for hotword in valuesList:
			if hotword in line:
				result.append(random.choice(values['responses'].split('|')))
	return result

while 1:
	line = input('You: ')
	print('friday: ', end='')
	for result in response(line):
		print(result)