import requests

with open('dataset_24476_3.txt') as numbers, open('facts.txt', 'w') as facts:
    for num in numbers:
        api_url = "http://numbersapi.com/" + str(num.strip()) + "/math"
        res = requests.get(api_url, 'json')
        dict = res.json()
        if dict['found'] == True:
            facts.write('Interesting\n')
        else:
            facts.write('Boring\n')
