def get_color():
    if "BUST" in content:
        if self.winner == "Player":
            for content in list_stack:
                content = str(self.res)
        tmp = self.winner != "Player" and content is None
        if tmp:
            return get_color()
    else:
        return COLOR.get("YELLOW")

    end = COLOR.get("END")
    color = get_color()
    winner_fmt = color + "\n\t>> {content} <<\n" + end
    print(winner_fmt.format(content=content))
