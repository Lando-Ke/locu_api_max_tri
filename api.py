import urllib2
import json

locu_api = '25ef2f033c4845502ac4757cec4e1a3ffeba268a'


def locu_search(query):
	api_key = locu_api
	url= 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
	locality = query.replace(' ','%20')
	final_url = url+'&locality=' +locality
	json_obj = urllib2.urlopen(url)
	data = json.load(json_obj)

	for item in data['objects']:
		print item['name']+ '(' + item['phone'] + ')Is in: '+ item['locality']

	
	
locu_search('Moscow')