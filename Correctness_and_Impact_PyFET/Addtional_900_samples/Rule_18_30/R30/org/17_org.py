
def test_clear_state(self):
    # Sanity test
    keys = {"foo", "baz", "corge", f"{GENERATED_WIDGET_KEY_PREFIX}-foo-None"}
    self.assertEqual(keys, self.session_state._keys())

    # Clear state
    self.session_state.clear()

    # Keys should be empty
    self.assertEqual(set(), self.session_state._keys())
