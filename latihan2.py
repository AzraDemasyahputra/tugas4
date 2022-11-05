a = int(input('bilangan ke-1 = '))
b = int(input('bilangan ke-2 = '))
c = int(input('bilangan ke-3 = '))
if a < b:
    if b < c:
        print('urutan bilangan : ', a, b, c)
    else:
        if a < c:
            print('urutan bilangan : ', a, c, b)
        else:
            print('urutan bilangan : ', c, a, b)
else:
    if a < c:
        print('urutan bilangan :', b, a, c)
    else: 
        if b < c:
            print('uruta bilangan : ', b, c, a)
        else:
            print('urutan bilangan : ', c, b, a)