from Array2d import Array2d
from Diagonal import Diagonal
from LowMatrix import LowMatrix


class Container:
    maxLen = 10000
    curLen = 0
    matrixesArr2d = []
    matrixesDiagonal = []
    matrixesLowMatrix = []
    allMatrixes = []

    def add_matrix(self, arr, typeOfMatrix):
        self.matrixesArr2d.append(Array2d(arr, len(arr)))
        self.curLen += 1

    def add_arr(self, arr, typeOfMatrix, demension):
        if typeOfMatrix == 2:
            self.matrixesDiagonal.append(Diagonal(arr, demension))
            self.curLen += 1
        else:
            self.matrixesLowMatrix.append(LowMatrix(arr, demension))
            self.curLen += 1

    def shell_sort(self, array):
        length = len(array)
        h = 1
        while h < length / 3:
            h = 3 * h + 1
        while h > 0:
            for i in range(h, length):
                j = i
                while j > 0 and array[j] < array[j-h]:
                    cur = array[j]
                    array[j] = array[j-h]
                    array[j-h] = cur
                    j -= h
            h = --h // 3
        return array

    def print_information(self, outputFileName):
        f = open(outputFileName, 'w')
        middles = []
        s = "Количество матриц в контейнере: " + str(self.curLen)
        f.write(s)
        f.write("\n")
        f.write("Список матриц: ")
        f.write("\n")

        for i in range(len(self.matrixesArr2d)):
            self.allMatrixes.append(self.matrixesArr2d[i])
            f.write(str(self.matrixesArr2d[i].name) + " " + str(self.matrixesArr2d[i].middle))
            middles.append(self.matrixesArr2d[i].middle)
            f.write("\n")

            for j in range(len(self.matrixesArr2d[i].array)):
                for k in range(len(self.matrixesArr2d[i].array[j])):
                    f.write(str(self.matrixesArr2d[i].array[j][k]) + " ")
                f.write("\n")
            f.write("\n")

        for i in range(len(self.matrixesDiagonal)):
            self.allMatrixes.append(self.matrixesDiagonal[i])
            f.write(str(self.matrixesDiagonal[i].name) + " " + str(self.matrixesDiagonal[i].middle))
            middles.append(self.matrixesDiagonal[i].middle)
            f.write("\n")

            for j in range(len(self.matrixesDiagonal[i].array)):
                for k in range(len(self.matrixesDiagonal[i].array[j])):
                    f.write(str(self.matrixesDiagonal[i].array[j][k]) + " ")
                f.write("\n")
            f.write("\n")

        for i in range(len(self.matrixesLowMatrix)):
            self.allMatrixes.append(self.matrixesLowMatrix[i])
            f.write(str(self.matrixesLowMatrix[i].name) + " " + str(self.matrixesLowMatrix[i].middle))
            middles.append(self.matrixesLowMatrix[i].middle)
            f.write("\n")

            for j in range(len(self.matrixesLowMatrix[i].array)):
                for k in range(len(self.matrixesLowMatrix[i].array[j])):
                    f.write(str(self.matrixesLowMatrix[i].array[j][k]) + " ")
                f.write("\n")
            f.write("\n")

        f.write("Отсортированные средние значения: ")
        sorted = self.shell_sort(middles)
        for i in range(len(sorted)):
            f.write(str(sorted[i]) + " ")

        f.write("\n")
        f.write("Отсортированные матрицы: ")
        f.write("\n")
        alreadyPrinted = []
        for i in range(len(sorted)):
            for j in range(len(self.allMatrixes)):
                if sorted[i] == self.allMatrixes[j].middle and self.allMatrixes[j] not in alreadyPrinted:
                    for h in range(len(self.allMatrixes[j].array)):
                        for p in range(len(self.allMatrixes[j].array[h])):
                            f.write(str(self.allMatrixes[j].array[h][p]) + " ")
                        f.write("\n")
                    alreadyPrinted.append(self.allMatrixes[j])
                    f.write("\n")
                    break
        f.close()
