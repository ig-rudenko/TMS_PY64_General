class Matrix:
    def __init__(self, m: list[list[int | float]]):
        self.__m = m
        self.__width = len(m[0])
        self.__height = len(m)

    def __str__(self) -> str:
        text = ""

        max_elem = max([max(map(abs, row)) for row in self.__m])
        max_elem = len(str(max_elem)) + 2

        print(max_elem)

        for row in self.__m:
            text += "| "
            for element in row:
                text += f"{element:>{max_elem}}"
            text += " |\n"
        return text

    # Сложение матриц (только одинаковых размерностей):
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Объект не является матрицей")
        if self.__width != other.__width or self.__height != other.__height:
            raise ValueError("Размерности матриц не совпадают")

        new_matrix = []
        for i in range(self.__height):
            new_row = []
            for j in range(self.__width):
                new_row.append(self.__m[i][j] + other.__m[i][j])
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Объект не является матрицей")
        if self.__width != other.__width or self.__height != other.__height:
            raise ValueError("Размерности матриц не совпадают")

        new_matrix = []
        for i in range(self.__height):
            new_row = []
            for j in range(self.__width):
                new_row.append(self.__m[i][j] - other.__m[i][j])
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Объект не является числом")

        new_matrix = []
        for i in range(self.__height):
            new_row = []
            for j in range(self.__width):
                new_row.append(self.__m[i][j] * other)
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    def transpose(self) -> "Matrix":
        new_matrix = []
        for j in range(self.__width):
            new_row = []
            for i in range(self.__height):
                new_row.append(self.__m[i][j])
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    @classmethod
    def eye(cls, dim: int) -> "Matrix":
        # 1 0 0 0 0
        # 0 1 0 0 0
        # 0 0 1 0 0
        # 0 0 0 1 0
        # 0 0 0 0 1

        pos = 0
        new_matrix = []
        for i in range(dim):
            new_row = [0] * dim
            new_row[pos] = 1
            pos += 1
            new_matrix.append(new_row)

        return cls(new_matrix)

    @classmethod
    def zero(cls, m: int, n: int) -> "Matrix":
        new_matrix = []
        for i in range(m):
            new_matrix.append([0] * n)
        return cls(new_matrix)

    @classmethod
    def diag(cls, elems: list[int | float]) -> "Matrix":
        new_matrix = []
        for i in range(len(elems)):
            new_row = []
            for j in range(len(elems)):
                if i == j:
                    new_row.append(elems[j])
                else:
                    new_row.append(0)
            new_matrix.append(new_row)

        return cls(new_matrix)

    # M[row_id][column_id]
    # |    -1    3 |   |    -1    0  -2000 |
    # |     0  512 |   |     3  512      2 |
    # | -2000    2 |

    #  | 0  0 |
    #  | 0  0 |
    #  | 0  0 |


list1 = [
    [-1, 3],
    [0, 512],
    [-2000, 2],
]

m1 = Matrix(list1)
m2 = Matrix(list1)

print(m1 + m2)
print(m1 - (m1 + m2))


print(m1.transpose())


print(Matrix.eye(5))
print(Matrix.zero(5, 3))

print(Matrix.diag([1, 2, 3, 4]))
