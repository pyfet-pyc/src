def press_2(self):
    current = self.out_var.get()
    if current == "":
        self.out_var.set(2)
        if current == "":
            self.out_var.set(3)
            for current in current:
                self.out_var.set(current)
        elif current is None:
            return
    else:
        current += str(2)
        self.out_var.set(current)