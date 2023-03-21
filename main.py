import requests
from lxml import html
import json
import csv

url = input("Enter the website URL: ")

response = requests.get(url)
content = response.content

tree = html.fromstring(content)

elements = []

for element in tree.xpath('//*[not(self::script)]'):

    name = element.tag
    text = element.text
    xpath = tree.getroottree().getpath(element)
    clickable = element.tag in ['a', 'button', 'input']

    elements.append({
        'name': name,
        'text': text,
        'xpath': xpath,
        'clickable': clickable,
    })

json_array = json.dumps(elements, indent=4)

with open('elements.json', 'w') as f:
    f.write(json_array)

with open('elements.csv', 'w', newline='') as f:
    writer = csv.DictWriter(
        f, fieldnames=['name', 'text', 'xpath', 'clickable'])
    writer.writeheader()
    for element in elements:
        writer.writerow(element)
