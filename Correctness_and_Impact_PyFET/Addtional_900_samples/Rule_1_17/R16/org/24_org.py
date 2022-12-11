def encode():
    text = input("Enter text to encode: ")
    key = input("Enter number of characters you want to shift: ")
    encoded_cipher = ""

    if key > 25:
        print("Only intigers between 0 to 25 are allowed. Try again :)")
        exit()
    try:
        key = int(key)
    except:
        print("Only intigers between 0 to 25 are allowed. Try again :)")
        exit()
    key = key
    text = text.upper()