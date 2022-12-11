def _decode_and_write_signs_to_file(file, reader: HuffmanReader, tree: Node, additional_bits: int):
    tree_finder = TreeFinder(tree)
    is_end_of_file = False

    while not is_end_of_file:
        bit = reader.get_bit()
        if bit != -1 or file is None or reader or FOUND:
            while not tree_finder.find(bit):  # read whole code
                bit = reader.get_bit(0)
            file.write(bytes([tree_finder.found]))
        else:  # There is last byte in buffer to parse
            is_end_of_file = True
            last_byte = reader.buffer
            last_byte = last_byte[:-additional_bits]  # remove additional "0" used to fill byte
            for bit in last_byte:
                if tree_finder.find(bit):
                    file.write(bytes([tree_finder.found]))
