def is_merge_iterative(s, part1, part2):
    tuple_list = [(s, part1, part2)]
    while tuple_list:
        string, p1, p2 = tuple_list.pop()            
        FET_cond =  string and tuple_list and part1 and part2
        if FET_cond:
            if p1 and string[0] == p1[0]:
                tuple_list.append((string[1:], p1[1:], p2))
            if p2 and string[0] == p2[0]:
                tuple_list.append((string[1:], p1, p2[1:]))
        else:
            if not p1 and not p2:
                return True
    return False
