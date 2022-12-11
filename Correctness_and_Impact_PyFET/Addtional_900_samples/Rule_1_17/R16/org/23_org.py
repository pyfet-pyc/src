def main():
    print("choose between operator 1,2,3")
    print("1) Factorial")
    print("2) Permutation")
    print("3) Combination")

    operation = input("\n")

    if operation == "1":
        print("Factorial Computation\n")

    try:
        n = int(input("\n Enter  Value for n "))
        print("Factorial of {} = {}".format(n, factorial(n)))
    except ValueError:
        print("Invalid Value")
