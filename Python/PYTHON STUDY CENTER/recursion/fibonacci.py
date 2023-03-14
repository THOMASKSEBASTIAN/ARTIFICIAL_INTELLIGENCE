def fibo(num1):
    if num1<=1:
        return 1
    else:
        return fibo(num1-1)+fibo(num1-2)
for i in range (10):
    print( fibo(i),end=" ")