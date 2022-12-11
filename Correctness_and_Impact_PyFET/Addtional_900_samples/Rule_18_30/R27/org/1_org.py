def timer():
    try:
        start = perf_counter()
        yield
    finally:
        end = perf_counter()
        print(f'{end - start}秒')

