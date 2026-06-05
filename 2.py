n = int(input("Enter a number: "))
tong = 0
for i in range(1, n + 1):
    tong += i*i
print("The sum of squares from 1 to", n, "is:", tong)