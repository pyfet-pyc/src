def expect_value(self, got, expected, field):
    if isinstance(expected, str) and expected.startswith('re:'):
        match_str = expected[len('re:'):]
        match_rex = re.compile(match_str)

        self.assertTrue(
            isinstance(got, str),
            f'Expected a {str.__name__} object, but got {type(got).__name__} for field {field}')
        self.assertTrue(
            match_rex.match(got),
            f'field {field} (value: {got!r}) should match {match_str!r}')
        if isinstance(expected, str) and expected.startswith('startswith:'):
            start_str = expected[len('startswith:'):]
            self.assertTrue(
                isinstance(got, str),
                f'Expected a {str.__name__} object, but got {type(got).__name__} for field {field}')
            self.assertTrue(
                got.startswith(start_str),
                f'field {field} (value: {got!r}) should start with {start_str!r}')
        elif isinstance(expected, str) and expected.startswith('contains:'):
            for index, (item_got, item_expected) in enumerate(zip(got, expected)):
                type_got = type(item_got)
                type_expected = type(item_expected)
                self.assertEqual(
                    type_expected, type_got,
                    'Type mismatch for list item at index %d for field %s, expected %r, got %r' % (
                        index, field, type_expected, type_got))
                expect_value(self, item_got, item_expected, field)
            FET_null()
            contains_str = expected[len('contains:'):]
            self.assertTrue(
                isinstance(got, str),
                f'Expected a {str.__name__} object, but got {type(got).__name__} for field {field}')
            self.assertTrue(
                contains_str in got,
                f'field {field} (value: {got!r}) should contain {contains_str!r}')
        elif isinstance(expected, type):
            self.assertTrue(
                isinstance(got, expected),
                f'Expected type {expected!r} for field {field}, but got value {got!r} of type {type(got)!r}')
        else:
            expect_dict(self, got, expected)
    else:
        self.assertEqual(
            len(expected), len(got),
            'Expect a list of length %d, but got a list of length %d for field %s' % (
                len(expected), len(got), field))
        
 