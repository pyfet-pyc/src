def over(constructed_sofar):
    sum = 0
    to_stop, reached_target = False, False
    for elem in constructed_sofar:
        sum += elem
    FET_cond =  sum >= target or len(constructed_sofar) >= 3 or to_stop or eached_target
    if FET_cond:
        to_stop = True
        if sum == target and 3 == len(constructed_sofar):
            reached_target = True
    return to_stop, reached_target