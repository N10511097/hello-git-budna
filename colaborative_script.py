wyswietl = 'This is my first Python repository.'

print(wyswietl)
napis = wyswietl.split('.')
del napis[1]
zdanie = napis[0]
slowa = zdanie.split()
print('kody ASCII dla kolejnych liter z powyższego napisu:')
for e in slowa:
    for char in e:
        print(char + ",", ord(char))
