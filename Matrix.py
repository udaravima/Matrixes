class Matrix(object):
    def __init__(self, matrix: list):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.matrix = matrix

    def multiply(self, matrix2, matrixS=None) -> list:
        if (matrixS == None):
            matrixS = self.matrix
        rowsS = len(matrixS)
        colsS = len(matrixS[0])

        if ('int' in str(type(matrix2)) or 'float' in str(type(matrix2))):
            result = []
            for i in matrixS:
                tempM = []
                for j in i:
                    tempM.append(j*matrix2)
                result.append(tempM)
            return result
        else:
            matrix = matrix2.matrix
            rows = len(matrix)
            cols = len(matrix[0])
            # Validation
            if (colsS != rows):
                print("invalid Matrix\n")
                return []
            # Function
            result = []
            for row in range(rowsS):
                temp = []
                for item in range(cols):
                    tempo = 0
                    for i in range(colsS):
                        tempo += matrixS[row][i] * matrix[i][item]
                    temp.append(tempo)
                result.append(temp)
            return result

    def transpose(self, matrix=None) -> list:
        if (matrix == None):
            matrix = self.matrix
        cols = len(matrix[0])
        rows = len(matrix)
        result = []
        for col in range(cols):
            temp = []
            for row in range(rows):
                temp.append(matrix[row][col])
            result.append(temp)
        return result

    def determinant(self, tempMatrix=None) -> int:
        if (tempMatrix == None):
            tempMatrix = self.matrix

        rows = len(tempMatrix)
        cols = len(tempMatrix[0])

        if (rows != cols):
            print("Invalid Matrix")
            return 0
        elif (cols == 1 and rows == 1):
            return tempMatrix[0][0]
        elif (cols == 2 and rows == 2):
            return tempMatrix[0][0]*tempMatrix[1][1] - tempMatrix[0][1]*tempMatrix[1][0]
        result = 0
        if (cols > 2):
            for j in range(cols):
                tempM = []
                for i in range(1, rows):
                    temp = []
                    for k in range(cols):
                        if (j == k):
                            continue
                        temp.append(tempMatrix[i][k])
                    tempM.append(temp)
                if (j % 2 == 0):
                    result += tempMatrix[0][j]*self.determinant(tempM)
                else:
                    result -= tempMatrix[0][j]*self.determinant(tempM)

        return result

    def adjoint(self, tempMatrix=None) -> list:
        if (tempMatrix == None):
            tempMatrix = self.matrix

        rows = len(tempMatrix)
        cols = len(tempMatrix[0])

        if (rows != cols):
            print("Invalid Matrix")
            return []

        result = []
        if (cols == 1 and rows == 1):
            return tempMatrix

        if (cols > 1):
            for l in range(rows):
                resultTemp = []
                for j in range(cols):
                    # getting determinant
                    tempM = []
                    for i in range(rows):
                        temp = []
                        if (l == i):
                            continue
                        for k in range(cols):
                            if (j == k):
                                continue
                            temp.append(tempMatrix[i][k])
                        tempM.append(temp)
                    resultTemp.append(
                        ((-1)**(l+j))*self.determinant(tempM))
                result.append(resultTemp)
        # print(result)#Debug
        return self.transpose(result)

    def inverse(self) -> list:
        return self.multiply(1/self.determinant(), self.adjoint())


