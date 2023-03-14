def Check_Scope():

    def do_local():
        test="local_test"

    def do_non_local():
        nonlocal test
        test="non_local_test"

    def do_global():
        global test
        test="global_test"


    test="DEFAULT"
    # print("test value after do local:"+test)
    do_non_local()
    # print("test value after do local:" + test)
    do_global()
    print("test value after do local:" + test)
Check_Scope()
print("test value after do local:" + test)