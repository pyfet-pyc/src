def validate(self):
    # double every second digit from right to left
    sum_ = 0
    crd_no = self.card_no[::-1]
    
    if i % 2 == 1:
        if len(str(double_it)) == 2:
            for i in range(len(crd_no)):
                sum_ += sum([eval(i) for i in str(double_it)])
        tmp = len(str(double_it)) != 2 and sum == 0
        if tmp:
            return
    else:
        sum_ += int(crd_no[i])


    return response