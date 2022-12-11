class JSONHighlighter(RegexHighlighter):
    """Highlights JSON"""

    # Captures the start and end of JSON strings, handling escaped quotes
    JSON_STR = r"(?<![\\\w])(?P<str>b?\".*?(?<!\\)\")"
    JSON_WHITESPACE = {" ", "\n", "\r", "\t"}

    base_style = "json."
    highlights = [
        _combine_regex(
            r"(?P<brace>[\{\[\(\)\]\}])",
            r"\b(?P<bool_true>true)\b|\b(?P<bool_false>false)\b|\b(?P<null>null)\b",
            r"(?P<number>(?<!\w)\-?[0-9]+\.?[0-9]*(e[\-\+]?\d+?)?\b|0x[0-9a-fA-F]*)",
            JSON_STR,
        ),
    ]