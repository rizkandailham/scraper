import re
import requests
from ast import literal_eval

urls = [
'https://www.google.com/maps?cid=15423079754231040967&hl=en',
'https://www.google.com/maps?cid=16168151796978303235&hl=en']

for url in urls:
    for g in re.findall(r'\[\\"http.*?\d+ reviews?.*?]', requests.get(url).text):
        data = literal_eval(g.replace('null', 'None').replace('\\"', '"'))
        print(bytes(data[0], 'utf-8').decode('unicode_escape'))
        print(data[1])
