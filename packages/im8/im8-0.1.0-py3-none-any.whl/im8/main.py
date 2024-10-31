import pyperclip

m0_0 = r"""
import numpy as np

# numpy
def matmul(a, b):
    n = a.shape[0]
    k = a.shape[1]
    m = b.shape[1]
    res = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            for s in range(k):
                res[i, j] += a[i, s] * b[s, j]

    return res

# python
def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    n = len(A)
    k_A = len(A[0])
    k_B = len(B)
    m = len(B[0])

    assert k_A == k_B, f"Can't multiply {n}x{k_A} on {k_B}x{m}"

    result = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(k_A):
                result[i][j] += A[i][k] * B[k][j]

    return result"""

m0_1 = r"""
import numpy as np


def strassen(A, B):
    n = len(A)

    if n <= 2:
        return np.dot(A, B)

    mid = n // 2

    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    P1 = strassen(A11, B12 - B22)
    P2 = strassen(A11 + A12, B22)
    P3 = strassen(A21 + A22, B11)
    P4 = strassen(A22, B21 - B11)
    P5 = strassen(A11 + A22, B11 + B22)
    P6 = strassen(A12 - A22, B21 + B22)
    P7 = strassen(A11 - A21, B11 + B12)

    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return C"""

m1_0 = r"""
import numpy as np
from sympy import Matrix, symbols, solve, Eq


def eigenvalues_and_eigenvectors_via_direct_expansion(A):
    # Переводим A в объект SymPy Matrix для символических вычислений
    A_sym = Matrix(A)
    n = A.shape[0]

    # Шаг 1: Нахождение характеристического многочлена det(A - λE) = 0
    λ = symbols("λ")
    I = Matrix.eye(n)  # Единичная матрица
    char_poly = (A_sym - λ * I).det()  # Характеристический многочлен
    eigenvalues = solve(char_poly, λ)  # Собственные значения - корни многочлена

    eigenvectors = {}

    # Шаг 2: Нахождение собственных векторов для каждого собственного значения
    for λi in eigenvalues:
        # Составляем матрицу (A - λi * E)
        eig_matrix = A_sym - λi * I
        # Решаем однородную систему (A - λiE) X = 0, находим нулевое пространство
        eig_vectors = eig_matrix.nullspace()

        # Преобразуем собственные векторы в массивы NumPy
        eigenvectors[λi] = [
            np.array(vec).astype(np.float64).flatten() for vec in eig_vectors
        ]

    return eigenvalues, eigenvectors


# Пример использования
A = np.array([[4, 1, 0], [1, 4, 1], [0, 1, 4]])

eigenvalues, eigenvectors = eigenvalues_and_eigenvectors_via_direct_expansion(A)

print("Собственные значения:")
for i, λ in enumerate(eigenvalues):
    print(f"λ{i+1} =", λ)

print()
print("Собственные векторы:")
for λ, vectors in eigenvectors.items():
    for i, vector in enumerate(vectors):
        print(f"Для λ = {λ}, собственный вектор {i+1}: {vector}")
"""

m1_1 = r"""
A = np.array([[2, 1], [1, 2]])

x = np.array([[1, 2]]).T

tol = 1e-6

max_iter = 100

lam_prev = 0

for i in range(max_iter):
    x = A @ x / np.linalg.norm(A @ x)

    lam = (x.T @ A @ x) / (x.T @ x)

    if np.abs(lam - lam_prev) < tol:
        break

    lam_prev = lam

print(lam)

print(x, i)
"""

m1_2 = r"""
import copy
import math


def find_max_upper(A: list[list[float]]) -> tuple[float, int, int]:
    max_idx = (0, 1)
    max_val = A[0][1]

    for i, row in enumerate(A):
        for j, val in enumerate(row[i + 1 :]):
            if abs(val) > abs(max_val):
                max_val = abs(val)
                max_idx = (i, j + i + 1)

    return abs(max_val), *max_idx


def get_phi(A: list[list[float]], i: int, j: int) -> float:
    return 1 / 2 * math.atan(2 * A[i][j] / (A[i][i] - A[j][j]))


def get_rotation_matrix(n: int, phi: float, i: int, j: int) -> list[list[float]]:
    H = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    H[i][i] = math.cos(phi)
    H[j][j] = math.cos(phi)
    H[i][j] = -math.sin(phi)
    H[j][i] = math.sin(phi)

    return H


def transpose(A: list[list[float]]) -> list[list[float]]:
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    n = len(A)
    k_A = len(A[0])
    k_B = len(B)
    m = len(B[0])

    assert k_A == k_B, f"Can't multiply {n}x{k_A} on {k_B}x{m}"

    result = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(k_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


def get_diag(A: list[list[float]]) -> list[float]:
    return [A[i][i] for i in range(len(A))]


def rotation_method(
    A: list[list[float]], k: int = 0, eps: float = 1e-5
) -> tuple[list[float], int, list[list[float]]]:
    n = len(A)

    A_ = copy.deepcopy(A)

    mx, i, j = find_max_upper(A_)

    Hs = []

    while abs(mx) > eps:
        phi = get_phi(A_, i, j)

        H = get_rotation_matrix(n, phi, i, j)

        A_ = matmul(matmul(transpose(H), A_), H)

        Hs.append(H)

        mx, i, j = find_max_upper(A_)

        k += 1

    vectors = Hs[0]

    for H in Hs[1:]:
        vectors = matmul(vectors, H)

    return get_diag(A_), k, vectors

# example
eigenvalues, _, eigenvectors = rotation_method([[1, 2, 3], [2, 3, 4], [6, 5, 4]])
"""

m1_3 = r"""
import copy
import math


def transpose(A: list[list[float]]) -> list[list[float]]:
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    n = len(A)
    k_A = len(A[0])
    k_B = len(B)
    m = len(B[0])

    assert k_A == k_B, f"Can't multiply {n}x{k_A} on {k_B}x{m}"

    result = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(k_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


def get_diag(A: list[list[float]]) -> list[float]:
    return [A[i][i] for i in range(len(A))]


def norm_vector(vector: list[float]) -> float:
    return math.sqrt(sum(el**2 for el in vector))


def get_proj(vector1: list[float], vector2: list[float]):
    return sum([vector1[i] * vector2[i] for i in range(len(vector1))])


def lower_norm(A: list[list[float]]) -> float:
    summ = 0

    for i in range(1, len(A)):
        for j in range(i):
            summ += A[i][j] ** 2

    return math.sqrt(summ)


def QR_decomposition(
    A: list[list[float]],
) -> tuple[list[list[float]], list[list[float]]]:
    n = len(A)
    m = len(A[0])

    Q = [[0] * m for _ in range(n)]

    # процесс Грама-Шмидта
    for j in range(m):
        b = [A[i][j] for i in range(n)]

        for i in range(j):
            a = [Q[k][i] for k in range(n)]
            proj = get_proj(a, b)
            b = [b[k] - proj * a[k] for k in range(n)]

        normed = norm_vector(b)

        e = [b[k] / normed for k in range(n)]

        for i in range(n):
            Q[i][j] = e[i]

    R = matmul(transpose(Q), A)

    return Q, R


def QR_algorithm(A: list[list[float]], eps: float = 1e-5):
    A_ = copy.deepcopy(A)

    k = 0

    Qs = []

    while lower_norm(A_) > eps:
        Q, R = QR_decomposition(A_)
        Qs.append(Q)
        A_ = matmul(R, Q)
        k += 1

    eingvals = get_diag(A_)

    eingvectors = Qs[0]
    for Q in Qs[1:]:
        eingvectors = matmul(eingvectors, Q)

    return eingvals, eingvectors, k

# example
eigenvalues, eigenvectors, _ = QR_algorithm([[2, 2, 3], [2, 3, 4], [6, 5, 4]])
"""

m2_0 = r"""
# latex
# $$f'(x) \approx \frac{f(x + h) - f(x)}{h}$$

import numpy as np
import matplotlib.pyplot as plt

h = np.logspace(-7, 1)

x0 = 0

true = 1

estimate = (np.exp(x0 + h) - np.exp(x0)) / h

err = np.abs(true - estimate)

p = np.polyfit(np.log(h), np.log(err), 1)

plt.figure(figsize=(3, 2))
plt.grid(alpha=0.5, linestyle=":")
plt.xlabel("h")
plt.ylabel("Ошибка")
plt.title("Сходимость оценки значения производной")

plt.loglog(h, err, label="Расчётные данные", c="red")

plt.loglog(h, np.exp(p[1]) * h ** p[0], label="Линейная аппроксимация")

plt.legend()
plt.show()

"""

m2_1 = r"""
# latex
# $$f'(x_0) \approx g'(x_0) = \frac{f(x_0) - f(x_0 - h)}{h}$$

import numpy as np

# Задаем значения h
h = np.logspace(-5, 1, num=100)  # 100 значений от 10^(-5) до 10^(1)

# Оценка производной методом обратной разности
estimate = (np.exp(0) - np.exp(0 - h)) / h  # f(0) - f(0 - h)

# Вычисление ошибки по сравнению с истинным значением производной
err = np.abs(estimate - 1)  # Истинное значение производной f'(0) = 1

# Линейная аппроксимация в логарифмическом масштабе
p = np.polyfit(np.log(h), np.log(err), 1)

plt.figure(figsize=(3, 2))
plt.grid(alpha=0.5, linestyle=":")
plt.xlabel("h")
plt.ylabel("Ошибка")
plt.title("Сходимость оценки значения производной")

plt.loglog(h, err, label="Расчётные данные", c="red")

plt.loglog(h, np.exp(p[1]) * h ** p[0], label="Линейная аппроксимация")

plt.legend()
plt.show()

"""

m2_2 = r"""
import numpy as np
import matplotlib.pyplot as plt

h = np.logspace(-5, 1)

x0 = 0

true = 1

estimate = (np.exp(x0 + h) - np.exp(x0 - h)) / h / 2

err = np.abs(true - estimate)

p = np.polyfit(np.log(h), np.log(err), 1)

plt.figure(figsize=(3, 2))
plt.grid(alpha=0.5, linestyle=":")
plt.xlabel("h")
plt.ylabel("Ошибка")
plt.title("Сходимость оценки значения производной")

plt.loglog(h, err, label="Расчётные данные", c="red")

plt.loglog(h, np.exp(p[1]) * h ** p[0], label="Линейная аппроксимация")

plt.legend()
plt.show()
"""

m3_0 = r"""
import numpy as np


def method_euler(f, x_0, x_n, y_0, N):
    dx = (x_n - x_0) / N
    x = np.linspace(x_0, x_n, N + 1)
    y = np.zeros((N + 1, len(y_0)))
    y[0, :] = y_0

    for n in range(N):
        y[n + 1, :] = y[n, :] + dx * f(x[n], y[n, :])

    return x, y


def fun_sin(x, y):
    return -np.sin(x)


x_0, x_n = 0, 10
y_0 = np.array([1.0])
N_values = [10, 100]

x_exact = np.linspace(x_0, x_n, 1000)
y_exact = np.cos(x_exact)

plt.figure(figsize=(10, 6))

plt.plot(
    x_exact, y_exact, label="Точное решение (cos(x))", color="black", linestyle="--"
)

for N in N_values:
    x_approx, y_approx = method_euler(fun_sin, x_0, x_n, y_0, N)
    plt.plot(x_approx, y_approx[:, 0], label=f"Аппроксимация Эйлера (N={N})")

plt.title("Аппроксимация методом Эйлера of y' = -sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right")
plt.grid(True)
plt.show()
"""

dummy = None

themes = {
    "Алгоритмы умножения матриц": {
        "Наивный алгоритм": m0_0,
        "Алгоритм Штрассена": m0_1,
    },
    "Собственные значения и вектора": {
        "Метод непосредственного развертывания": m1_0,
        "Метод итераций (степенной метод)": m1_1,
        "Метод вращений": m1_2,
        "QR алгоритм": m1_3,
    },
    "Численное дифференцирование": {
        "Метод прямой разности": m2_0,
        "Метод обратной разности": m2_1,
        "Метод центральной разности": m2_2,
    },
    "Методы решения задачи Коши": {
        "Явный метод Эйлера": m3_0,
    },
}

themes_numerated = {
    i: {j: v for j, (k, v) in enumerate(v.items())}
    for i, (k, v) in enumerate(themes.items())
}


def get(i=None, j=None):
    if i is None or j is None:
        for i, (theme, methods) in enumerate(themes.items()):
            print(f"{i} {theme}")
            for j, method in enumerate(methods.keys()):
                print(f'{"-"*3} {i}.{j} {method}')
    else:
        pyperclip.copy(themes_numerated[i][j].strip())
