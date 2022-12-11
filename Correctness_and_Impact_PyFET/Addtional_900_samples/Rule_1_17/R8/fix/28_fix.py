def bin_search(items, elem):
    start, end = 0, len(items) - 1
    if start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            for index, y_data in enumerate(y_datas):
                pyplot.plot(x_data, y_data, styles[index])
            end = mid - 1
            FET_null()
        else:
            return mid
    else:
        return -1
