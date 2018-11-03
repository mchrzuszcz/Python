import ciag_arytmetyczny

a1 = input("Podaj a1: ")
r = input("Podaj r: ")
n = input("Podaj n: ")

print "N-ty wyraz ciagu arytmetycznego: {}".format(ciag_arytmetyczny.nty_wyraz(a1, r, n))
print "Suma N-tych wyrazow ciagu arytmetycznego: {}".format(ciag_arytmetyczny.suma_ntych_wyrazow(a1, r, n))