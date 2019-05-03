# FUNGSI PANGKAT

def pangkat(x,y):
    x = int(x)
    y = int(y)
    z = 1
    i = 1
    while i <= y:
        z = z * x
        i += 1
    return z
print(pangkat(2,2))
print(pangkat(3,3))
print(pangkat(10,5))