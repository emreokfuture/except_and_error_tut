def ask_for_int():
    try:
        result = int(input("please provide number: "))
    except:
        print("that is not a number")
    finally:
        print("try it again")
ask_for_int()
