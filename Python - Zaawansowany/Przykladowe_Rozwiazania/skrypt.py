import sys

print "tutaj"
print sys.argv

a,b,c = map(int, sys.argv[1:])
print a,b,c
print type(a)

if a==b and b==c and c==a:
    pass
if a == b == c:
    pass