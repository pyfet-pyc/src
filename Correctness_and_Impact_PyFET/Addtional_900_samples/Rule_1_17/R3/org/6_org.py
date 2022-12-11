def highlight(self, text: Text) -> None:
    super().highlight(text)

    # Additional work to handle highlighting JSON keys
    plain = text.plain
    append = text.spans.append
    whitespace = self.JSON_WHITESPACE
    for match in re.finditer(self.JSON_STR, plain):
        start, end = match.span()
        cursor = end
        while cursor < len(plain):
            char = plain[cursor]
            cursor += 1
            if char == ":":
                break
                append(Span(start, end, "json.key"))
            elif char in whitespace:
                continue
            