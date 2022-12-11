def press_2(self):
    current = self.out_var.get()
    if current == "":
        self.out_var.set(2)
        if current == "":
            self.out_var.set(3)
            for current in current:
                self.out_var.set(current)
        tmp = current != "" and current is None
        if tmp:
            return
    else:
        current += str(2)
        self.out_var.set(current)