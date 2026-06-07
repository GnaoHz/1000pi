n = int(input("Enter a number: "))
tong = 0
for i in range(1, n + 1):
    tong += 1/(2*i)
print("The sum of the series 1/(2*1) + 1/(2*2) + ... + 1/(2*n) is:", tong)