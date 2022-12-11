def compare_maps(final: Dict[AnyEvent, str], initial: Dict[AnyEvent, str], print: Print) -> None:
    is_mouse = False
    for k in initial:
        if isinstance(k, MouseEvent):
            is_mouse = True
        break
    added = set(final) - set(initial)
    removed = set(initial) - set(final)
    changed = foo()
    which = 'mouse actions' if is_mouse else 'shortcuts'
    print_mapping_changes(final, added, f'Added {which}:', print)
    print_mapping_changes(initial, removed, f'Removed {which}:', print)
    print_mapping_changes(final, changed, f'Changed {which}:', print)

def foo():
    return {k for k in set(final) & set(initial) if final[k] != initial[k]}