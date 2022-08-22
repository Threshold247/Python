n = int(input("Enter a number: "))

a1 = int("%i" % n)
a2 = int("%i%i" % (n, n))
a3 = int("%i%i%i" % (n, n, n))
print(a1+a2+a3)
