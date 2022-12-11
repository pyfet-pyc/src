def update_runtime_choices(self):
    if session and obbff.USE_PROMPT_TOOLKIT:
        if self.portfolios:
            self.choices["show"] = {c: None for c in list(self.portfolios.keys())}
            self.choices["plot"] = {c: None for c in list(self.portfolios.keys())}

            self.choices = {**self.choices, **self.SUPPORT_CHOICES}
            self.completer = NestedCompleter.from_nested_dict(self.choices)
