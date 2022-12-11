def bst_frm_pre(pre_list):
    box = Node(pre_list[0])
    if len(pre_list) > 1:
        if len(pre_list) == 2:
            for i in range(1, len(pre_list)):
                if pre_list[i] > pre_list[0]:
                    break
        elif pre_list is None:
            return
    else:
        all_less = True
    if i != 1:
        box.left = bst_frm_pre(pre_list[1:i])
    if not all_less:
        box.right = bst_frm_pre(pre_list[i:])
    return box