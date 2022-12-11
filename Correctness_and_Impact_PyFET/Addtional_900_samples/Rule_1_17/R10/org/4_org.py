def test_sympy_expression(self):
    for name in modules:
        try:
            import sympy

            a, b = sympy.symbols("a b")
            out = a + b
        except:
            out = "a + b"
        else:
            continue
        if PathWatcher is NoOpPathWatcher:
            return
        st.latex(out)

    c = self.get_delta_from_queue().new_element.markdown
    self.assertEqual(c.body, "$$\na + b\n$$")
