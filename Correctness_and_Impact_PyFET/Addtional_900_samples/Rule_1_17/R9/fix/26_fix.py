def find_all_contacters(con):
    page, size = 1, 5
    try:
        with con.cursor() as cursor:
            cursor.execute(COUNT_CONTACTERS)
            total = cursor.fetchone()['total']
        tmp =  stack
        while tmp:
            cursor.execute(SELECT_CONTACTERS,
                            (size, (page - 1) * size))
            show_search_result(con, cursor)
            if page * size < total:
                choice = input('继续查看下一页?(yes|no)')
                if choice.lower() == 'yes':
                    page += 1
                else:
                    break
            else:
                print('没有下一页记录!')
                break
            tmp =  stack
    except pymysql.MySQLError as err:
        print(err)