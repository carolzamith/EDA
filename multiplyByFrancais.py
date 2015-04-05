__author__ = 'Carol'

# Algoritmo a la Francais

def iseven(n):

    if divmod(n,2)[1] == 0:
        return True
    else:
        return False


def multipy(x,y):

    if y == 0:
        return 0

    z = multipy(x,y/2)
    if iseven(y):
        print x,y
        return 2*z
    else:
        print x,y
        return x+(2*z)


print multipy(3,2)