with open('dataset_3363_4.txt') as file:
    s = [row.strip().split(';') for row in file]
mthx = 0
phsx = 0
russ = 0
for i in s:
	mthx += int(i[1])
	phsx += int(i[2])
	russ += int(i[3])
	print((int(i[1])+int(i[2])+int(i[3]))/3)
print((mthx/len(s)), (phsx/len(s)), (russ/len(s)), end=' ')