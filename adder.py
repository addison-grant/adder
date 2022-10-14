from itertools import combinations

carry = 0

print("Provide two binary numbers of the same length (0-pad shorter number on the left if needed).")
num1 = input("first binary number: ")
num2 = input("second binary number: ")

iter = range(len(num1) - 1, -1, -1)
result = ""

def addbits(p, q, carry):
    m = int(p)
    n = int(q)
    t = (m, n, carry)

    match tuple(t):
        case (0,0,0):
            return 0, 0
        case (1, 0, 0) | (0, 1, 0) | (0, 0, 1):
            return 1, 0
        case (1, 1, 0) | (1, 0, 1) | (0, 1, 1):
            return 0, 1
        case _: # all 1's
            return 1, 1

i = 0
for i in iter:
    xresult, carry = addbits(num1[i], num2[i], carry)
    result = f"{xresult}{result}"

print(f"result: {result}, carry: {carry}")

