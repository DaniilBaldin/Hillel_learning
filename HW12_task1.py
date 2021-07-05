a = {1, 2, 3, 4, 5}
print(type(a))
print(all(a))

b = {5, 4, 3, 2, 1}
print(type(b))
print(all(b))

c = {'audi', 'honda', 'bmw', 'fiat'}
print(type(c))
for item in enumerate(c, 1):
    print(item)

d = {'audi', 'honda', 'bmw', 'fiat'}
print(type(d))
print(len(d))

e = {5, 41, 322, 22, 1}
print(type(e))
print(max(e))
print(min(e))

f = {5, 41, 322, 22, 1}
print(type(f))
print(sorted(f))

g = {5, 41, 322, 22, 1}
print(type(g))
print(sum(g))
