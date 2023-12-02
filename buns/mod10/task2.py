import requests
from re import findall

page_response = requests.get('http://www.columbia.edu/~fdc/sample.html').text
headers = findall(r'>.+</h3>', page_response)
result = list(map(lambda x: x[1:-5], headers))
print(result)