def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = input()
tmp = 0
for i in range(len(n)):
    tmp += int(n[i])
n = int(n)
check = n % 2 == 0 or n % 5 == 0 or tmp % 3 == 0

if is_prime(n):
    print("Prime")
elif check or n == 1:
    print("Not Prime")
else:
    print("Prime")