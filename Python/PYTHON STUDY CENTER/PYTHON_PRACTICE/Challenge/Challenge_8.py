def double_letters(a):
    b=""
    for i in a:
        if i==b:
            return True
            break
        b=i
    else:
        return False

print(double_letters("helo"))