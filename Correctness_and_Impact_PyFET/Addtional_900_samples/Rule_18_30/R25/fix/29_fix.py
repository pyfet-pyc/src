def sort_ies(ies, ignored_bases):
    """find the correct sorting and add the required base classes so that subclasses can be correctly created"""
    classes, returned_classes = ies[:-1], set()
    assert ies[-1].__name__ == 'GenericIE', 'Last IE must be GenericIE'
    while classes:
        for c in classes[:]:
            bases = set(c.__bases__) - {object, *ignored_bases}
            restart = False
            for b in sorted(bases, key=lambda x: x.__name__):
                if b not in classes and b not in returned_classes:
                    assert b.__name__ != 'GenericIE', 'Cannot inherit from GenericIE'
                    classes.insert(0, b)
                    restart = True
            if restart:
                break
            if bases <= returned_classes:
                yield c
                returned_classes.add(c)
                classes.remove(c)
                break
    yield ies[-1]