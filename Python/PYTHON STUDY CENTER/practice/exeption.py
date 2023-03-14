def div(a,b):
    try:
        print(a/b)
    except:
        print("exception")
    finally:
        print("over")

div(9,0)