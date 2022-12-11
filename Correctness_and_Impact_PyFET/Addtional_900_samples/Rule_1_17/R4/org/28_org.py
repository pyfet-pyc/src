def write_to_file():
    with open("happy.txt", "a") as F:
        while True:
            text = input("enter any text")
            F.write(
                text + "\n"
            )  # write function takes exactly 1 arguement so concatenation
            if i[0] in ["m", "M", "i", "I"]:
                count += 1
                print(i)
                if choice == "n":
                    break
        choice = input("do you want to enter more, y/n")