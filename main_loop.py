from random import randint

from loop_in_loop import print_matrix


def find_len():
    matrix = [[1, 2],
              [3, 4],
              [5, 6]]

    # с помощью функции len найдите длину и ширину матрицы
    N = len(matrix)  # количество строк
    M = len(matrix[0])

    print_matrix(matrix)
    print("Размер матрицы", N, ' х ', M)


def my_matrix(n, m):
    """

    :param n: количество строк
    :param m: количество столбцов
    :return:
    """

    # matrix = [] * n
    for i in range(n):
        for j in range(m):
            print(i, j, end=' | ')
        print()


def find_min_max_mean(n=3, m=3):
    """
    203 - 211 loop in loop

    :param n: количество строк
    :param m:  количество столбцов
    :return:
    """
    N = n
    M = m
    random_matrix = [[randint(1, 9) for _ in range(M)] for _ in range(N)]

    mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
    min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
    min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
    max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
    max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

    print_matrix(random_matrix)
    for row in random_matrix:
        min_ = row[0]
        max_ = row[0]

        min_index = 0
        max_index = 0

        for col_index, col_value in enumerate(row):
            if col_value < min_:
                min_ = col_value
                min_index = col_index
            elif col_value > max_:
                max_ = col_value
                max_index = col_index

        min_value_rows.append(min_)
        max_value_rows.append(max_)

        min_index_rows.append(min_index)
        max_index_rows.append(max_index)

    print("Минимальные значения:", min_value_rows)
    print("Индексы:             ", min_index_rows)

    print("Максимальные значения:", max_value_rows)
    print("Индексы:              ", max_index_rows)


def find_min_max_mean_column(n=3, m=3):
    N = n
    M = m
    random_matrix = [[randint(1, 9) for _ in range(M)] for _ in range(N)]

    print_matrix(random_matrix)

    min_list = []
    min_index_list = []
    mean_list = []

    for j in range(M):
        # цикл по столбцам
        min_ = random_matrix[0][j]  # первая строка, j-й столбец
        index_row = 0

        s = 0
        for i in range(N):
            # цикл по строкам
            if random_matrix[i][j] < min_:
                min_ = random_matrix[i][j]
                index_row = i
            s += random_matrix[i][j]

        min_list.append(min_)
        min_index_list.append((index_row, j))
        mean_list.append(round(s / N, 2))

    print("Минимальные значения в столбце", min_list)
    print("Индексы", min_index_list)
    print(mean_list)


def find_mean_pos(n=5, m=6):
    random_matrix = [[randint(-10, 10) for _ in range(m)] for _ in range(n)]
    print_matrix(random_matrix)

    mean_pos = {}
    for j in range(m):
        s = 0  # обнуляем счетчик для каждого столбца
        count = 0
        for i in range(n):
            if random_matrix[i][j] > 0:
                s += random_matrix[i][j]
                count += 1
        mean_pos[j] = round(s / count, 2)
    print(mean_pos)



def ph_rab():
    heads = 35
    legs = 94
    for ph in range(1, heads):
        for rab in range(1, heads):
            if ph + rab > heads:
                break
            elif ph + rab == heads:
                if ph * 2 + rab * 4 != legs:
                    continue
                print("Кроликов:", rab)
                print("Фазаны:", ph)
                print("########")


def one(n, m):
    zero = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == j:
                zero[i][j] = 1

    print_matrix(zero)


if __name__ == "__main__":
    # find_len()
    # my_matrix(2, 3)
    # find_min_max_mean_column()
    # find_min_max_mean_column()
    # find_mean_pos()
    # ph_rab()
    # one(3, 5)
    # # print_matrix([[(i, j) for j in range(3)] for i in range(3)])
    # for i in range(3):
    #     for j in range(3):
    #         print((i, j), end=" ")
    #     print()

    n = 5
    m = 2

    list_ = [i + 1 for i in range(n)]
    list_sred = []

    for i in range(len(list_) - k + 1):
        list_sred.extend(list_[i: ])

