def test_header_split():
    unchanged = """
    python/:list
    ls
    +
    g++
    g/+
    clang++
    btrfs~volume
    :intro
    :cht.sh
    python/copy+file
    python/rosetta/:list
    emacs:go-mode/:list
    g++g++
    """

    split = """
    python copy file
    python/copy file

    python  file
    python/file

    python+file
    python/file

    g++ -O1
    g++/-O1
    """
    inp, outp = test.split('\n')
    assert outp == _add_section_name(inp), "_add_section_name"
