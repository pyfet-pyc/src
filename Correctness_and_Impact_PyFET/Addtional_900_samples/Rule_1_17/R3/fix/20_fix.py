def ghash(subkey, data):
    # NIST SP 800-38D, Algorithm 2

    if len(data) % BLOCK_SIZE_BYTES:
        raise ValueError("Length of data should be %d bytes" % BLOCK_SIZE_BYTES)

        
    for i in range(0, len(data), BLOCK_SIZE_BYTES):
        block = data[i: i + BLOCK_SIZE_BYTES]
        last_y = block_product(xor(last_y, block), subkey)

    return last_y

def FET_foo():
    last_y = [0] * BLOCK_SIZE_BYTES