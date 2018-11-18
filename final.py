a = {}
b = {}
res = []
x = 0
with open('dataset_3380_5.txt') as file:
    c = [row.strip().split('\t') for row in file]
for j in range(len(c)):
    if int(c[j][0]) not in a:
        a[int(c[j][0])] = x
        b[int(c[j][0])] = 1
        res.append(int(c[j][2]))
        x += 1
    else:
        b[int(c[j][0])] = b[int(c[j][0])] + 1
        res[a[int(c[j][0])]] += int(c[j][2])
for i in range(1, 12):
    if i in a:
        print(i, float(res[a[i]]/b[i]), end=' ')
        print()
    else:
        print(i, '-', end=' ')
        print()
