import requests
import abuse

url = 'https://sidharthfridayassistant.pythonanywhere.com/api/all/'

def post_data(url, hotwords, responses, tasks, links):
	r = requests.post(url, data={"hotwords":hotwords, "responses":responses, "tasks":tasks, "links":links})
	return r

print(post_data(url, 'your email', 'My email is fridayassistance@gmail.com|You can talk to me on my email address which is fridayassistance@gmail.com', "", ""))
# if the result is <Response [201]> then your work is done!