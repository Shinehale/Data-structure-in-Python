def is_even(num):
    if num & 1:
        return False
    else:
        return True


R = int(input("Please input the number you want to check:\n"))
ans = is_even(R)
if ans:
    print("the number is even!")
else:
    print("the number is not even!")
