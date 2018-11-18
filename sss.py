import requests
r = 'dataset_3378_3.txt'
with open(r) as file:
    s = file.readline().strip()
while r[0] != 'We':
	r = requests.get(s).text.strip().split( )
	s = 'https://stepic.org/media/attachments/course67/3.6.3/' + r[0]
	print(r)
r = requests.get(s).text.strip().split('\n')
print(s)