def test_side_effect(zip_error, script, filename):
    zip_error(filename)
    side_effect(Command(script, ''), None)

    dir_list = os.listdir(u'.')
    if filename not in set(dir_list):
        filename = normalize('NFD', filename)

    assert set(dir_list) == {filename, 'd'}
