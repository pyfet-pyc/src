def get_background_style_defs(self, arg=None):
    prefix = self.get_css_prefix(arg)
    bg_color = self.style.background_color
    hl_color = self.style.highlight_color

    lines = []

    if arg and not self.nobackground and bg_color is not None:
        text_style = ''
        if Text in self.ttype2class:
            text_style = ' ' + self.class2style[self.ttype2class[Text]][0]
        lines.insert(
            0, '%s{ background: %s;%s }' % (
                prefix(''), bg_color, text_style
            )
        )
    if hl_color is not None:
        lines.insert(
            0, '%s { background-color: %s }' % (prefix('hll'), hl_color)
        )

    return lines