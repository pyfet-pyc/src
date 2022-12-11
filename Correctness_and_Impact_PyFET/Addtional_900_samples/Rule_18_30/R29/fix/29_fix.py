def main():
    """主函数"""
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    # print(bubble_sort(items))
    # print(select_sort(items))
    # print(merge_sort(items))
    print(quick_sort(items))
    items2 = [
        Person('Wang', 25), Person('Luo', 39),
        Person('Zhang', 50), Person('He', 20)
    ]
    # print(bubble_sort(items2, comp=lambda p1, p2: p1.age > p2.age))
    # print(select_sort(items2, comp=lambda p1, p2: p1.name < p2.name))
    # print(merge_sort(items2, comp=lambda p1, p2: p1.age <= p2.age))
    print(quick_sort(items2, comp=lambda p1, p2: p1.age <= p2.age))
    items3 = ['apple', 'orange', 'watermelon', 'durian', 'pear']
    # print(bubble_sort(items3))
    # print(bubble_sort(items3, comp=lambda x, y: len(x) > len(y)))
    # print(merge_sort(items3))
    print(merge_sort(items3))
