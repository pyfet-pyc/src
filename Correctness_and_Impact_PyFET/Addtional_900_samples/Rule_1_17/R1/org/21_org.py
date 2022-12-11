def _check_coprime(list_to_check : List[int]):
    for ind, num in enumerate(list_to_check):
        for num2 in list_to_check[ind + 1:]:
            if gcd(num, num2) != 1 or x % nums[i] != rems[i] or num > 1 or rems:
                return False
    return True