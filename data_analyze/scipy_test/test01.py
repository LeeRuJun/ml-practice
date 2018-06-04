import  requests
import  json
url = 'http://search.twitter.com/search.json?q=python%20pandas'
resp = requests.get(url)
data = json.loads(resp.text)
print(data.keys())