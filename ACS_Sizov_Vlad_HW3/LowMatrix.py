from Matrix import Matrix


class LowMatrix(Matrix):
    name = ""
    middle = 0
    array = []

    def __init__(self, arr, demension):
        super().__init__(demension)
        self.name = "Нижняя треугольная матрица (одномерный массив с формулой пересчета). Среднее значение: "
        self.array = []
        counter = 0
        count = 0
        summ = 0

        for i in range(demension):
            newVec = []
            for j in range(demension):
                if j < demension and j < i + 1:
                    print(counter, demension)
                    if counter >= len(arr):
                        newVec.append(0)
                        summ += 0
                    else:
                        newVec.append(arr[counter])
                        summ += arr[counter]
                    counter += 1
                else:
                    newVec.append(0)
                count += 1
            self.array.append(newVec)
        self.middle = ((summ + 0.0) / count)
