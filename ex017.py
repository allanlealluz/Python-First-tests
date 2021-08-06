import math
catop = float(input('cateto oposto: '))
catad = float(input('cateto adjacente: '))
hip = catop**2 + catad**2
hip2 = math.sqrt(hip)
print('a hipotenusa é {}'.format(hip2))