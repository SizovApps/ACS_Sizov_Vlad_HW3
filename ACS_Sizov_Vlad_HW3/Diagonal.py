from Matrix import Matrix


class Diagonal(Matrix):
    name = ""
    middle = 0
    array = []

    def __init__(self, arr, demension):
        super().__init__(demension)
        self.name = "Диагональная матрица (на основe одномерного массива). Среднее значение: "
        self.array = []
        count = 0
        sum = 0

        for i in range(len(arr)):
            newVec = []
            for j in range(len(arr)):
                if i == j:
                    newVec.append(arr[i])
                    sum += arr[i]
                else:
                    newVec.append(0)
                count += 1
            self.array.append(newVec)

        self.middle = ((sum + 0.0) / count);