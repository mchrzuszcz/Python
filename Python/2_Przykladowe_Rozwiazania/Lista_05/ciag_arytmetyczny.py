def nty_wyraz(a1,r,n):
    an = a1 + (n-1)*r
    return an

def suma_ntych_wyrazow(a1,r,n):
    suma = []
    suma.append(a1)
    for i in range(2,n+1):
        suma.append(nty_wyraz(a1,r,i))
    return sum(suma)
