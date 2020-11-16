def two_fer(name = "you"):
    try:
        return("One for "+ name +", one for me.")
    except ValueError:
        print("What an odd name...")
    pass
