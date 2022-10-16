while True:
    try:
        a = int(input("Enter Number Integer: "))
    except ValueError:
        print("Enter Integer")
    else:
        print("You enter %d" % a)
        break
    finally:
        print("Good.")

