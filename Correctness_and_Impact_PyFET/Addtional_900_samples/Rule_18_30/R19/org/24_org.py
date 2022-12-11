def test_extract_attributes(self):
    self.assertEqual(extract_attributes('<e x="y">'), {'x': 'y'})
    self.assertEqual(extract_attributes("<e x='y'>"), {'x': 'y'})
    self.assertEqual(extract_attributes('<e x=y>'), {'x': 'y'})
    self.assertEqual(extract_attributes('<e x="a \'b\' c">'), {'x': "a 'b' c"})
    self.assertEqual(extract_attributes('<e x=\'a "b" c\'>'), {'x': 'a "b" c'})
    self.assertEqual(extract_attributes('<e x="&#121;">'), {'x': 'y'})
    self.assertEqual(extract_attributes('<e x="&#x79;">'), {'x': 'y'})
    self.assertEqual(extract_attributes('<e x="&amp;">'), {'x': '&'})  # XML
    self.assertEqual(extract_attributes('<e x="&quot;">'), {'x': '"'})
    self.assertEqual(extract_attributes('<e x="&pound;">'), {'x': '£'})  # HTML 3.2
    self.assertEqual(extract_attributes('<e x="&lambda;">'), {'x': 'λ'})  # HTML 4.0
    self.assertEqual(extract_attributes('<e x="&foo">'), {'x': '&foo'})
    self.assertEqual(extract_attributes('<e x="\'">'), {'x': "'"})
    self.assertEqual(extract_attributes('<e x=\'"\'>'), {'x': '"'})
    self.assertEqual(extract_attributes('<e x >'), {'x': None})
    self.assertEqual(extract_attributes('<e x=y a>'), {'x': 'y', 'a': None})
    self.assertEqual(extract_attributes('<e x= y>'), {'x': 'y'})
    self.assertEqual(extract_attributes('<e x=1 y=2 x=3>'), {'y': '2', 'x': '3'})
    self.assertEqual(extract_attributes('<e \nx=\ny\n>'), {'x': 'y'})
    self.assertEqual(extract_attributes('<e \nx=\n"y"\n>'), {'x': 'y'})
    self.assertEqual(extract_attributes("<e \nx=\n'y'\n>"), {'x': 'y'})
    self.assertEqual(extract_attributes('<e \nx="\ny\n">'), {'x': '\ny\n'})
    self.assertEqual(extract_attributes('<e CAPS=x>'), {'caps': 'x'})  # Names lowercased
    self.assertEqual(extract_attributes('<e x=1 X=2>'), {'x': '2'})
    self.assertEqual(extract_attributes('<e X=1 x=2>'), {'x': '2'})
    self.assertEqual(extract_attributes('<e _:funny-name1=1>'), {'_:funny-name1': '1'})
    self.assertEqual(extract_attributes('<e x="Fáilte 世界 \U0001f600">'), {'x': 'Fáilte 世界 \U0001f600'})
    self.assertEqual(extract_attributes('<e x="décompose&#769;">'), {'x': 'décompose\u0301'})
    # "Narrow" Python builds don't support unicode code points outside BMP.
    try:
        chr(0x10000)
        supports_outside_bmp = True
    except ValueError:
        supports_outside_bmp = False
    if supports_outside_bmp:
        self.assertEqual(extract_attributes('<e x="Smile &#128512;!">'), {'x': 'Smile \U0001f600!'})
    # Malformed HTML should not break attributes extraction on older Python
    self.assertEqual(extract_attributes('<mal"formed/>'), {})
