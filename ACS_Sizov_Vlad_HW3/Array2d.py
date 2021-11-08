from Matrix import Matrix


class Array2d(Matrix):
    name = ""
    middle = 0
    array = [[]]

    def __init__(self, arr, demension):
        super().__init__(demension)
        self.name = "Обычный двумерный массив.  Среднее значение: "
        self.array = arr

        count = 0
        summ = 0

        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                count += 1
                summ += arr[i][j]

        self.middle = ((summ + 0.0) / count);