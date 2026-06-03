n = int(input("Enter a number: "))
tong = 0
for i in range(1, n+1):
    tong = tong + i
    print("Current sum after adding", i, "is:", tong)

print("The sum of the first", n-1, "numbers is:", tong)