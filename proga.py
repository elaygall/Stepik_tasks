with open('dataset_3363_2.txt') as INF:
	inf = INF.readline()
list(inf)
inf += 'S'
a = []
b = []
c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
final = []
x = 0
z = ""
while x != len(inf):
	if inf[x] not in c:
		final.append(inf[x])
		x += 1
	else:
		if inf[x+1] in c:
			b += inf[x]
			x += 1
		else:
			b += inf[x]
			for j in b:
				z += str(j)
			final.append(final[-1]*(int(z)-1))
			z = ""
			b = []
			x += 1
final.pop()
r = ''
for y in final:
	r += str(y)
with open('answer.txt', 'w') as ouf:
	print(r)
	ouf.write(r)