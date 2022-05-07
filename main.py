"""                     19.	Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество нулей в нечетных столбцах, умноженное на К больше,
B | C   Вид матрицы     чем произведение чисел в нечетных строках, то поменять местами В и С симметрично, иначе В и Е поменять местами несимметрично.
D | E                   При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
                        то вычисляется выражение: A*AT – K * F-1, иначе вычисляется выражение (A-1 +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А.
Алиев Лев ИСТбд-11"""
import time
import numpy as np

try:
    n = int(input("Задайте количество строк и столбцов > 3: "))
    while n < 4:
        n = int(input("Задайте количество строк и столбцов > 3: "))
    k = int(input("Задайте значение коэффициента k: "))
    A = np.random.randint(-10, 10, (n, n), dtype=int)
    """A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if j == i or j == n-1-i:
                A[i][j] = 0
            else:
                A[i][j] = (n - i) * 10 + j"""
    F = np.copy(A)
    np.set_printoptions(precision=2, linewidth=200)
    print(f"----A----\n{A}\n----F----\n\n{F}\n")
    cond_e, cond_lines = 0, 1
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                cond_lines *= A[i][j]
            if i > (n // 2 - (n - 1) % 2) and j > (n // 2 - (n - 1) % 2) and j % 2 == 0 and A[i][j] == 0:
                cond_e += 1
    print(f"Количество нулей в нечетных столбцах Е = {cond_e}\nПроизведение чисел в нечетных строках = {cond_lines}")
    if cond_e * k > cond_lines:
        for i in range(n // 2):
            F[i] = F[i][::-1]
    else:
        for i in range(n // 2):
            for j in range(n // 2):
                F[i][j], F[n // 2 + n % 2 + i][n // 2 + n % 2 + j] = F[n // 2 + n % 2 + i][n // 2 + n % 2 + j], F[i][j]
    print(f"----F----\n{F}\n")
    if np.linalg.det(A) > sum(np.diagonal(F)):
        if np.linalg.det(F) == 0:
            print("Матрица F - вырожденная, невозможно провести вычисления")
        else:
            print(f"A*AT – K * F-1\n{np.matmul(A, np.transpose(A)) - np.linalg.inv(F) * k}")
    else:
        if np.linalg.det(A) == 0:
            print("Матрица A - вырожденная, невозможно провести вычисления")
        else:
            print(f"(A-1 +G-FТ)*K\n{(np.linalg.inv(A) + np.tril(A) - np.transpose(F)) * k}")
    print(f"Время выполнения: {time.process_time()}")

except ValueError:
    print("Введённые данные не являются числом")