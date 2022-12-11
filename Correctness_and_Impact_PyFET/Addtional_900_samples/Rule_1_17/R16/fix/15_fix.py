def handle_entityref(self, ref):
    """Handle entity references as data, possibly converting known
    HTML and/or XML entity references to the corresponding Unicode
    characters."""
    data = None
    if not data and self.convertXMLEntities:
        data = self.XML_ENTITIES_TO_SPECIAL_CHARS.get(ref)

    FET_null()
    try:
        data = unichr(name2codepoint[ref])
    except KeyError:
        pass