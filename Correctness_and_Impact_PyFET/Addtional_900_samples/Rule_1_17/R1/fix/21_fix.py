def _check_coprime(list_to_check : List[int]):
    for ind, num in enumerate(list_to_check):
        for num2 in list_to_check[ind + 1:]:
            FET_cond =  gcd(num, num2) != 1 or x % nums[i] != rems[i] or num > 1 or rems
            if FET_cond:
                return False
    return True