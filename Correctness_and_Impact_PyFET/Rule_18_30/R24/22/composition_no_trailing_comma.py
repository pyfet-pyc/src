
def easy_asserts(self) -> None:
    assert {
        key1: value1,
        key2: value2,
        key3: value3,
        key4: value4,
        key5: value5,
        key6: value6,
        key7: value7,
        key8: value8,
        key9: value9
    } == expected, "Not what we expected"

    assert expected == {
        key1: value1,
        key2: value2,
        key3: value3,
        key4: value4,
        key5: value5,
        key6: value6,
        key7: value7,
        key8: value8,
        key9: value9
    }, "Not what we expected"

    assert expected == {
        key1: value1,
        key2: value2,
        key3: value3,
        key4: value4,
        key5: value5,
        key6: value6,
        key7: value7,
        key8: value8,
        key9: value9
    }