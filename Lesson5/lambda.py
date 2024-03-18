# tables = [lambda x = b: (x*10) for b in range(1, 11)]
# for table in tables:
#     print(table())

listing = []
for b in range(1, 11):
    listing.append(b)
tables = [lambda x = b: (x*10) for b in listing]
for table in tables:
    print(table())



a = b = c = 0
print(id(a))
print(id(b))
print(id(c))

# help() - keywords

print(dir(str))

print(11%33)

print(a, b, c, sep='\n')

print(ord("К"))
"".