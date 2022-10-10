def _askfornumber ():
    while True:
        try:
            entering=int(input("enter anumber please"))
        except:
            print("please try again")
            continue

        else:
            print("thank you for number")

        finally:
            print("at the end")

_askfornumber()
