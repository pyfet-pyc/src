if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("usage - $python find_prime.py <num:int>")
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise Exception("Enter an integer as argument only.")
    l = find_prime(num)
    print(l)