import numpy as np
import pyperclip as clip


tasks = [
    'Наивный метод умножения матриц',
    'Алгоритм Штрассена',
    'Степенной метод',
    'Метод вращений',
    'QR алгоритм',
    'Euler',
    'Прямая разность',
    'Обратная разность',
    'Центральная разность',
    'sympy_eigen_check'
]


def T(A):
    return np.array(list(zip(*A)))

def above_triag(A):
    n = len(A)
    for j0 in range(1, n):
        for j in range(j0, n):
            yield j0 - 1, j

def naive_matmul(A, B):
    new_rows = []
    for rowA in A:
        new_row = []
        for colB in T(B):
            new_row.append(sum(rowA * colB))
        new_rows.append(new_row)
    return np.array(new_rows)


def to_square_mat(vec):
    n = len(vec)
    new = np.zeros((n, n))
    new[0, :] = vec
    return new


def blocks_to_matrix(b1, b2, b3, b4):
    out = []
    for bi1, bi2 in zip(b1, b2):
        row1 = list(bi1)
        row2 = list(bi2)
        out.append(row1 + row2)

    for bi3, bi4 in zip(b3, b4):
        row3 = list(bi3)
        row4 = list(bi4)
        out.append(row3 + row4)

    return np.array(out)


def shtrassen(A, B):
    n = len(A)
    if n == 1:
        return np.array([[A[0, 0] * B[0, 0]]])

    A11 = A[:n // 2, :n // 2]
    A22 = A[n // 2:, n // 2:]
    A12 = A[:n // 2, n // 2:]
    A21 = A[n // 2:, :n // 2]

    B11 = B[:n // 2, :n // 2]
    B22 = B[n // 2:, n // 2:]
    B12 = B[:n // 2, n // 2:]
    B21 = B[n // 2:, :n // 2]

    D = shtrassen(A11 + A22, B11 + B22)
    D1 = shtrassen(A12 - A22, B21 + B22)
    D2 = shtrassen(A21 - A11, B11 + B12)
    H1 = shtrassen(A11 + A12, B22)
    H2 = shtrassen(A21 + A22, B11)
    V1 = shtrassen(A22, B21 - B11)
    V2 = shtrassen(A11, B12 - B22)

    b1 = D + D1 + V1 - H1
    b2 = V2 + H1
    b3 = V1 + H2
    b4 = D + D2 + V2 - H2
    return blocks_to_matrix(b1, b2, b3, b4)


def dot_product(vec1, vec2):
    return sum(vec1 * vec2)

def norm_vec(vec):
    """Возвращает результат операции нормирования вектора"""
    len_squared = dot_product(vec, vec)
    return np.sqrt(len_squared) / len_squared * vec

def power_method(A, e=0.001):
    xk = norm_vec(np.ones(len(A)))
    eign_prev = 1
    eign = 0
    while abs(eign - eign_prev) > e:
        eign_prev = eign
        xk_1 = T(shtrassen(A, T(to_square_mat(xk))))[0]
        eign = dot_product(xk_1, xk)
        xk = norm_vec(xk_1)

    return eign


def jacobi(phi, i, j, n):
    E = np.eye(n)
    E[i, i] = np.cos(phi)
    E[j, j] = np.cos(phi)
    E[i, j] = -np.sin(phi)
    E[j, i] = np.sin(phi)
    return E


def jacobi_eigen(A, e=0.001):
    n = len(A)

    step = 0
    while True:
        # Получаем координаты наибольшего по модулю в наддиагональном треугольнике значения
        i, j = max(above_triag(A), key=lambda vec: abs(A[vec[0], vec[1]]))

        # Условие выхода из цикла
        if abs(A[i, j]) < e:
            break

        # По формуле находим угол поворота
        phi = 0.5 * np.arctan(2 * A[i, j] / (A[i, i] - A[j, j]))

        # Вычисляем матрицу Якоби
        H = jacobi(phi, i, j, n)

        # Шаг итерации (зануление максимального недиагонального элемента)
        A = naive_matmul(naive_matmul(T(H), A), H)  # H.T * A * H
        step += 1
    return A


def proj(a, b):
    """Оператор проекции вектора a на вектор b"""
    return b * (dot_product(a, b) / dot_product(b, b))

def QR_decomp(A):
    """
    QR разложение матрицы. Для заданной квадратной матрицы A вычисляет ее
    разложение на произведение матриц Q (ортогональная матрица) и
    R (верхнетреугольная матрица) и возвращает Q и R.
    """

    # Для разложения используется процесс Грамма-Шмидта
    Q_t = []
    for vec_col in T(A):
        proj_sum = np.zeros(len(vec_col))
        for bi in Q_t:
            proj_sum = proj_sum + proj(vec_col, bi)

        Q_t.append(vec_col - proj_sum)

    Q_t = np.array(list(map(norm_vec, Q_t)))
    R = naive_matmul(Q_t, A)

    return T(Q_t), R


def norm_below_diag(A):
    """Вычисляет норму поддиагональных элементов матрицы A и возвращает результат"""
    A_t = T(A)
    return sum([A_t[i, j] ** 2 for (i, j) in above_triag(A_t)])


def QR_algorithm(A, e=0.001):
    """Приводит матрицу к треугольной форме, возвращает результат"""
    Ak = A

    # Вычисляем норму элементов под главной диагональю
    norm = norm_below_diag(Ak)
    while norm > e:
        # QR-разложение
        Q, R = QR_decomp(Ak)

        # Шаг QR-алгоритма
        Ak = naive_matmul(R, Q)

        # Обновляем норму элементов под главной диагональю
        norm = norm_below_diag(Ak)
    return Ak


def f1(y1, y2):
    return np.arctan(1 / (1 + y1 ** 2 + y2 ** 2))


def f2(y1, y2):
    return np.sin(y1 * y2)


def euler(f1, f2, y1_0, y2_0, x0, x_end, h):
    # Количество шагов
    n_steps = int((x_end - x0) / h) + 1
    # Массивы для хранения решений
    x_values = np.linspace(x0, x_end, n_steps)
    y1_values = np.zeros(n_steps)
    y2_values = np.zeros(n_steps)

    # Начальные условия
    y1_values[0] = y1_0
    y2_values[0] = y2_0

    # Метод Эйлера
    for i in range(1, n_steps):
        y1_values[i] = y1_values[i - 1] + h * f1(y1_values[i - 1], y2_values[i - 1])
        y2_values[i] = y2_values[i - 1] + h * f2(y1_values[i - 1], y2_values[i - 1])

    return x_values, y1_values, y2_values


def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h


def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h


def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def get_task_code(task_name):
    if task_name == 'sympy_eigen_check':
        return '''
import sympy as sp
M_sp = sp.Matrix(A)
sp_eign_vals = list(map(lambda x: sp.re(x.evalf()), list(M_sp.eigenvals().keys())))
print('Собственные значения, найденные с помощью sympy (для сравнения):', ', '.join(map(str, sp_eign_vals)))'''

    if task_name == 'Наивный метод умножения матриц':
        return '''
def naive_matmul(A, B):
    new_rows = []
    for rowA in A:
        new_row = []
        for colB in T(B):
            new_row.append(sum(rowA * colB))
        new_rows.append(new_row)
    return np.array(new_rows)
        '''

    if task_name == 'Алгоритм Штрассена':
        return '''
def to_square_mat(vec):
    n = len(vec)
    new = np.zeros((n, n))
    new[0, :] = vec
    return new

def blocks_to_matrix(b1, b2, b3, b4):
    out = []
    for bi1, bi2 in zip(b1, b2):
        row1 = list(bi1)
        row2 = list(bi2)
        out.append(row1 + row2)

    for bi3, bi4 in zip(b3, b4):
        row3 = list(bi3)
        row4 = list(bi4)
        out.append(row3 + row4)

    return np.array(out)

def shtrassen(A, B):
    n = len(A)
    if n == 1:
        return np.array([[A[0, 0] * B[0, 0]]])

    A11 = A[:n//2, :n//2]
    A22 = A[n//2:, n//2:]
    A12 = A[:n//2, n//2:]
    A21 = A[n//2:, :n//2]

    B11 = B[:n//2, :n//2]
    B22 = B[n//2:, n//2:]
    B12 = B[:n//2, n//2:]
    B21 = B[n//2:, :n//2]

    D = shtrassen(A11 + A22, B11 + B22)
    D1 = shtrassen(A12 - A22, B21 + B22)
    D2 = shtrassen(A21 - A11, B11 + B12)
    H1 = shtrassen(A11 + A12, B22)
    H2 = shtrassen(A21 + A22, B11)
    V1 = shtrassen(A22, B21 - B11)
    V2 = shtrassen(A11, B12 - B22)

    b1 = D + D1 + V1 - H1
    b2 = V2 + H1
    b3 = V1 + H2
    b4 = D + D2 + V2 - H2
    return blocks_to_matrix(b1, b2, b3, b4)
        '''

    if task_name == 'Степенной метод':
        return '''
def power_method(A, e=0.001):
    xk = norm_vec(np.ones(len(A)))
    eign_prev = 1
    eign = 0
    while abs(eign-eign_prev) > e:
        eign_prev = eign
        xk_1 = T(shtrassen(A, T(to_square_mat(xk))))[0]
        eign = dot_product(xk_1, xk)
        xk = norm_vec(xk_1)

    return eign
        '''

    if task_name == 'Метод вращений':
        return '''
def T(A):
    return np.array(list(zip(*A)))

def above_triag(A):
    n = len(A)

    for j0 in range(1, n):
        for j in range(j0, n):
            yield j0-1, j

def jacobi(phi, i, j, n):
    E = np.eye(n)
    E[i, i] = np.cos(phi)
    E[j, j] = np.cos(phi)
    E[i, j] = -np.sin(phi)
    E[j, i] = np.sin(phi)
    return E

def jacobi_eigen(A, e=0.001):

    n = len(A)

    step = 0
    while True:
        # Получаем координаты наибольшего по модулю в наддиагональном треугольнике значения
        i, j = max(above_triag(A), key=lambda vec: abs(A[vec[0], vec[1]]))

        # Условие выхода из цикла
        if abs(A[i, j]) < e:
            break

        # По формуле находим угол поворота
        phi = 0.5 * np.arctan(2 * A[i,j] / (A[i, i] - A[j, j]))

        # Вычисляем матрицу Якоби
        H = jacobi(phi, i, j, n)

        # Шаг итерации (зануление максимального недиагонального элемента)
        A = naive_matmul(naive_matmul(T(H), A), H) # H.T * A * H
        step += 1
    return A
        '''

    if task_name == 'QR алгоритм':
        return '''
def T(A):
    return np.array(list(zip(*A)))

def dot_product(vec1, vec2):
    return sum(vec1 * vec2)

def norm_vec(vec):
    """Возвращает результат операции нормирования вектора"""
    len_squared = dot_product(vec, vec)
    return np.sqrt(len_squared) / len_squared * vec 

    def proj(a, b):
    """Оператор проекции вектора a на вектор b"""
    return b * (dot_product(a, b) / dot_product(b, b))

def above_triag(A):
    n = len(A)

    for j0 in range(1, n):
        for j in range(j0, n):
            yield j0-1, j

def QR_decomp(A):
    """
    QR разложение матрицы. Для заданной квадратной матрицы A вычисляет ее
    разложение на произведение матриц Q (ортогональная матрица) и
    R (верхнетреугольная матрица) и возвращает Q и R.
    """

    # Для разложения используется процесс Грамма-Шмидта
    Q_t = []
    for vec_col in T(A):
        proj_sum = np.zeros(len(vec_col))
        for bi in Q_t:
            proj_sum = proj_sum + proj(vec_col, bi)

        Q_t.append(vec_col - proj_sum)

    Q_t = np.array(list(map(norm_vec, Q_t)))
    R = naive_matmul(Q_t, A)

    return T(Q_t), R

def norm_below_diag(A):
    """Вычисляет норму поддиагональных элементов матрицы A и возвращает результат"""
    A_t = T(A)
    return sum([A_t[i, j]**2 for (i, j) in above_triag(A_t)])

def QR_algorithm(A, e=0.001):
    """Приводит матрицу к треугольной форме, возвращает результат"""
    Ak = A

    # Вычисляем норму элементов под главной диагональю
    norm = norm_below_diag(Ak)
    while norm > e:
        # QR-разложение
        Q, R = QR_decomp(Ak)

        # Шаг QR-алгоритма
        Ak = naive_matmul(R, Q)

        # Обновляем норму элементов под главной диагональю
        norm = norm_below_diag(Ak)
    return Ak
    '''

    if task_name == 'Euler':
        return '''
def f1(y1, y2):
    return np.arctan(1 / (1 + y1**2 + y2**2))

def f2(y1, y2):
    return np.sin(y1 * y2)

def euler(f1, f2, y1_0, y2_0, x0, x_end, h):
    # Количество шагов
    n_steps = int((x_end - x0) / h) + 1
    # Массивы для хранения решений
    x_values = np.linspace(x0, x_end, n_steps)
    y1_values = np.zeros(n_steps)
    y2_values = np.zeros(n_steps)

    # Начальные условия
    y1_values[0] = y1_0
    y2_values[0] = y2_0

    # Метод Эйлера
    for i in range(1, n_steps):
        y1_values[i] = y1_values[i - 1] + h * f1(y1_values[i - 1], y2_values[i - 1])
        y2_values[i] = y2_values[i - 1] + h * f2(y1_values[i - 1], y2_values[i - 1])

    return x_values, y1_values, y2_values
        '''

    if task_name == 'Прямая разность':
        return '''
def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h
        '''

    if task_name == 'Обратная разность':
        return '''
def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h
    '''

    if task_name == 'Центральная разность':
        return '''
def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)
        '''


def c(task_name):
    clip.copy(get_task_code(task_name))