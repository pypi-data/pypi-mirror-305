import pandas as pd
import openpyxl
from app.graphs_path_lib import (
    prima_alg, kruskal_alg, floyd_alg, dejkstra_alg
)


def load_cost_matrix(path_input: str):
    """
    Загрузка матрицы смежности ориентированного графа
    """

    try:
        # Загрузка файла XLS в датафрейм
        data_frame = pd.read_excel(path_input, header=None)

        # Проверка формата матрицы
        if not data_frame.applymap(lambda x: isinstance(x, (int, float))).values.all():
            raise ValueError('Ошибка: Матрица должна содержать только числа')

        # Преобразование датафрейма в список списков
        matrix_out = data_frame.values.tolist()

        # Проверка квадратности матрицы
        n = len(matrix_out)
        if any(len(row) != n for row in matrix_out):
            raise ValueError('Ошибка: Матрица должна быть квадратной')

        return matrix_out
    except ValueError as e:
        print(e)
        return None


# Функция трассировки
def trass(mst_dict):
    """
    Трассировка маршрута в графе
    """

    max_in_alg = mst_dict['max_el']
    start_node = mst_dict['start']
    end_node = mst_dict['end']
    weight_total = mst_dict['weight_total']
    df = mst_dict['df']

    # Создаем пустой список номеров вершин маршрутов и добавляем в него номер конечной вершины
    route_res = [end_node]
    # Создаем пустой список для последующего отображения в таблице
    weight_lst_temp = [weight_total]
    # Создаем пустой список для суммирования весов кратчайшего пути
    weight_list = []
    table_viz_lst = []
    # переводим датасет в список
    d_lst = df.values.tolist()
    # Производим трассировку по таблице алгоритма
    while weight_lst_temp[-1] != 0:

        for i in range(len(d_lst) - 1, -1, -1):

            if i == 0 or d_lst[start_node - 1][end_node - 1] == weight_total:
                # последний шаг
                weight_lst_temp.append(0)
                route_res.append(start_node)
                # print('last, ',weight_lst_temp, route_res)

            else:
                if d_lst[end_node - 1][i] == weight_total and d_lst[end_node - 1][i] < d_lst[end_node - 1][i - 1]:
                    route_res.append(i)
                    # print(route_res)
                    end_node = i + 1
                    # Переназначаем вес минимума
                    min_temp = df[i - 1].min()
                    weight_total = min_temp
                    # Присваиваем параметру остановки цикла новое значение
                    weight_lst_temp.append(weight_total)
                    break

                else:
                    continue

                    # Добавляем веса ребер в маршруте
    for i in range(len(weight_lst_temp) - 1):
        weight_list.append(weight_lst_temp[i] - weight_lst_temp[i + 1])
        # Добавляем шаги трассировки в список для последующего отображения в таблице
        temp_lst = [str(weight_lst_temp[i]) + ' - ' + str(weight_lst_temp[i] - weight_lst_temp[i + 1]) + ' = ' + str(
            weight_lst_temp[i + 1])]
        table_viz_lst.append(temp_lst)

    # Переменной len_sum присваиваем значение суммы всех ребер из списка weight_list
    len_sum = sum(weight_list)
    # Переворачиваем список для корректной работы с ориентированными графами
    route_res.reverse()
    return route_res, weight_list, len_sum, table_viz_lst



file_path = 'matrix_undirected.xlsx'

matrix = load_cost_matrix(file_path)
print('matrix:')
print(matrix)

start_node = 1
end_node = 5

algs = ['Прима', 'Краскала', 'Дейкстры', 'Флойда']


# prima_res = prima_alg(matrix)
# print(f'\nАлгоритм Прима:')
# print(prima_res)
#
# kruskal_res = kruskal_alg(matrix)
# print(f'\nАлгоритм Краскала:')
# print(kruskal_res)
#
# floyd_res = floyd_alg(matrix)
# print(f'\nАлгоритм Флойда:')
# print(floyd_res)

dejkstra_res = dejkstra_alg(matrix, start_node, end_node)
print(f'\nАлгоритм Дейкстры:')
print(dejkstra_res)

trass(dejkstra_res)
print('end')
