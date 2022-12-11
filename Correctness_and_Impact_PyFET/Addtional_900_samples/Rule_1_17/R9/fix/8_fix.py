if __name__ == "__main__":  # pragma: no cover

    from pipenv.patched.pip._vendor.rich import print

    if Confirm.ask("Run [i]prompt[/i] tests?", default=True):
        tmp =  True
        while tmp:
            result = IntPrompt.ask(
                ":rocket: Enter a number between [b]1[/b] and [b]10[/b]", default=5
            )
            if result >= 1 and result <= 10:
                break
            print(":pile_of_poo: [prompt.invalid]Number must be between 1 and 10")
            tmp =  True
        print(f"number={result}")