from container import Container
import random

print("Если вы хотите использовать ввод данных из файла - нажмите 1,\nЕсли рандомное заполнение данных - то нажмите 2:")
modeData = int(input())
cont = Container()

if modeData == 1:
    print("Введите полное имя файла с исходными матрицами:")
    inputFileName = input()

    print("Введите полное имя файла для вывода результата:")
    outputFileName = input()

    lines = []

    f = open(inputFileName)

    for line in f:
        lines.append(line)

    i = 0
    while i < len(lines):
        typeOfMatrix = int(lines[i])
        demension = int(lines[i + 1])

        if typeOfMatrix == 1:
            curArr = []
            for j in range(i + 2, i + 2 + demension):
                newLine = lines[j]
                curVec = list(map(int, newLine.split()))
                curArr.append(curVec)
            cont.add_matrix(curArr, 1)
            i += 2 + demension
        elif typeOfMatrix == 2:
            newLine = lines[i + 2]
            curArr = list(map(int, newLine.split()))
            cont.add_arr(curArr, 2, demension)
            i += 3
        else:
            newLine = lines[i + 2]
            curArr = list(map(int, newLine.split()))
            cont.add_arr(curArr, 3, demension)
            i += 3
    cont.print_information(outputFileName)


else:
    print("Введите полное имя файла для вывода результата:")
    outputFileName = input()
    countOfArray2d = random.randint(0, 33)
    for i in range(countOfArray2d):
        curArr = []
        demension = random.randint(2, 10)
        for j in range(demension):
            curVec = []
            for k in range(demension):
                newNum = random.randint(-100, 100)
                curVec.append(newNum)
            curArr.append(curVec)
        cont.add_matrix(curArr, 1)

    countOfDiagonal = random.randint(0, 33)

    for i in range(countOfDiagonal):
        curArr = []
        demension = random.randint(2, 10)
        for j in range(demension):
            newNum = random.randint(-100, 100)
            curArr.append(newNum)
        cont.add_arr(curArr, 2, demension)

    countOfLow = random.randint(0, 33)

    for i in range(countOfLow):
        curArr = []
        demension = random.randint(2, 10)
        for j in range(demension):
            newNum = random.randint(-100, 100)
            curArr.append(newNum)
        cont.add_arr(curArr, 3, demension)

    cont.print_information(outputFileName)


