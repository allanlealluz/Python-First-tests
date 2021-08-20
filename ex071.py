valor = int(input('qual será o valor sacado? '))
cinquenta = vinte = dez = um = 0
while valor > 0:
    if(valor >= 50):
        valor -= 50
        cinquenta += 1
    elif(valor >= 20):
        valor -= 20
        vinte += 1
    elif valor >= 10:
        valor -= 10
        dez += 1
    elif valor >= 1:
        valor -= 1
        um += 1
print(cinquenta, vinte, dez, um)