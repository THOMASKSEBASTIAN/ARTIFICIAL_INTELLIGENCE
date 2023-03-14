def check_mail(func):
    def wrapper(a,b):
        if b==121:
            return func(a,b)

    return wrapper


@check_mail

def login(mailid,password):
    return "successfully completed login process"
print(login("thomasks1994@gmail.com",121))