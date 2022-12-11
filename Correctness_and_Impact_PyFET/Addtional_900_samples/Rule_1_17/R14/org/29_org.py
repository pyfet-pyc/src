def num_generator(m, n):
    """指定范围的数字生成器"""
    yield from range(m, n + 1)