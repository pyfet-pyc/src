def main():
    file_input = input("File Name: ")
    try:
        with open(file_input, "r") as info:
            count = collections.Counter(info.read().upper())
    except FileNotFoundError:
        print("Please enter a valid file name.")
        main()

    value = pprint.pformat(count)
    print(value)
    exit()

