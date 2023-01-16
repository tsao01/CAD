import numpy as np

def readCSV(csv_file):
    with open(csv_file) as file:
        pre_result = []
        result = []
        my_row = []
        csv_string = file.read()
        csv_string = csv_string.split("\n")
        for row in csv_string:
            pre_result.append(eval(row))
        for i in range(0, len(pre_result[0])):
            for j in range(0, len(pre_result[0])):
                my_row.append(pre_result[j][i])
            result.append(my_row)
            my_row = []
    return result

def makeMyMatrix(matrix):
    arr_matrix = []
    new_row = []
    for k in range(0, len(matrix)):
        for i in range(0, len(matrix[k])):
            for j in range(0, len(matrix[k])):
                if (matrix[k][i] < matrix[k][j]):
                    new_row.append(1)
                elif (matrix[k][i] == matrix[k][j]):
                    new_row.append(0.5)
                elif (matrix[k][i] > matrix[k][j]):
                    new_row.append(0)
        arr_matrix.append(new_row)
        new_row = []
    return arr_matrix

def makeOneMatrix(matrixs):
    oneMatrix = []
    for i in range(0, len(matrixs[0])):
        summa = 0
        for k in range(0, len(matrixs)):
            summa += matrixs[k][i]
        oneMatrix.append(summa/len(matrixs))
    return oneMatrix

# Лекция очно
# def makeKMatrixAgain(oneMatrix, k = [1/3, 1/3, 1/3]):
#     xMatrix = []
#     kLambda = 0
#     matSumma = 0
#     sumMatrix = [0] * len(k)
#     kMatrix = []
#     for i in range(0, len(oneMatrix), len(k)):
#         matSumma = 0
#         for j in range(0, len(k)):
#             matSumma += oneMatrix[i+j]*k[j]
#         xMatrix.append(matSumma)

#     for i in range(0, len(oneMatrix)):
#         kLambda += oneMatrix[i] * xMatrix[i // len(k)]
        
#     tmpMatrix = []
#     for i in range(0, len(oneMatrix)):
#         tmpMatrix.append(oneMatrix[i] * xMatrix[i // len(k)])
#     for i in range(0, len(tmpMatrix)):
#         sumMatrix[i % len(k)] += tmpMatrix[i]
#     for i in range(0, len(sumMatrix)-1):
#         kMatrix.append(round((1/kLambda)*sumMatrix[i], 3))
#     kSumma = 0
#     for i in range(0, len(kMatrix)):
#         kSumma += kMatrix[i]
#     kMatrix.append(round(1-kSumma, 3))
#     if (abs(kMatrix[len(kMatrix)-1] - k[len(k)-1]) > 0.001):
#         return makeKMatrixAgain(oneMatrix, kMatrix)
#     else:
#         return kMatrix

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


def makeKMatrix(oneMatrix, k = [1/3, 1/3, 1/3]):
    kMatrix = list(split(oneMatrix, len(k)))
    n = len(kMatrix[0])
    kP = np.ones(n) / n
    kN = None
    while True:
        y = np.matmul(kMatrix, kP)
        lbd = np.matmul(np.ones(n), y)
        kN = (1 / lbd) * y
        diff = abs(kN - kP)
        max = diff.max()
        if max <= 0.001:
            break
        else:
            kP = kN
    return np.around(kN, 3)

def task(csvString):
    res1 = readCSV(csvString)
    res2 = makeMyMatrix(res1)
    res3 = makeOneMatrix(res2)
    res4 = makeKMatrix(res3)
    return res4
    
print(task("./task6_data.csv"))