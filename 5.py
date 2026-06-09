from fractions import Fraction
n = int(input("Enter a number: "))
tong = Fraction(0, 1)
for i in range(0, n+1):
    tong += Fraction(1, 2*i+1)
print("The sum is:", tong)