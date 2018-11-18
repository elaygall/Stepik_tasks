b = {}


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


with open('dataset_3363_3.txt') as f:
    s = f.read().lower().split()

for i in s:
    if i not in b.keys():
        b[i] = 1
    else:
        b[i] = b[i]+1

a = max(b.values())
c = get_key(b, a)

while get_key(b, a):
    if get_key(b, a) < c:
        c = get_key(b, a)

    b.pop(get_key(b, a))
print(c, a)
