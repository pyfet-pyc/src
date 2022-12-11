def chips_manage(self):
    if self.choice == "Insurance":
        err = "The amount should under " + str(self.player.chips.current_amount())
        pay_ins = self.get_select(
            self.player.chips.current_amount(),
            prompt="Insurance amount >> ",
            general_err=err,
        )
        self.player.chips.insurance = pay_ins

    try:
        self.player.chips.double_bet()
    except ValueError as e:
        print(e)
    self.player.refresh_prompt()
    if self.choice in ("Insurance", "Double-down", "Surrender"):
        self.go_on = False