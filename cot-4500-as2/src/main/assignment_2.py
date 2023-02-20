import math
import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)

# def lagrange(xData, xValue):
#   # big sigma
#   sum = 0
#   for k in range(len(xData)):
#     # big pi
#     numerator = 1
#     denominator = 1
#     for i in range(len(xData)):
#       if k == i:
#         continue
#       numerator *= xValue - xData[i]
#       denominator *= xData[k] - xData[i]
#     sum += yData[k] * (numerator / denominator)
#   return sum

def neville(xData, yData, xValue):
  Q = []
  Q.append(yData.copy())
  for k in range(1, len(xData)):
    qTemp = []
    for i in range(k):
      qTemp.append(None)
    for i in range(k, len(xData)):
      a = (xValue - xData[i-k])
      b = (xValue - xData[i])
      c = (xData[i] - xData[i-k])
      d = Q[k-1][i]
      e = Q[k-1][i-1]
      Q_i_k = (a * d - b * e) / c
      qTemp.append(Q_i_k)
    Q.append(qTemp.copy())
  return Q[len(xData)-1][len(xData)-1]

def number_1():
  xData = [3.6, 3.8, 3.9]
  yData = [1.675, 1.436, 1.318]
  print(neville(xData, yData, 3.7))
  print()

def forward_difference(xData, yData):
  Q = []
  Q.append(yData.copy())
  for k in range(1, len(xData)):
    qTemp = []
    for i in range(k):
      qTemp.append(None)
    for i in range(k, len(xData)):
      Q_i_k = (Q[k-1][i] - Q[k-1][i-1]) / (xData[i] - xData[i-k])
      qTemp.append(Q_i_k)
    Q.append(qTemp.copy())
  coeff = []
  for i in range(1, len(xData)):
    coeff.append(Q[i][i])
  return coeff

def number_2():
  xData = [7.2, 7.4, 7.5, 7.6]
  yData = [23.5492, 25.3913, 26.8224, 27.4589]
  coeff = forward_difference(xData, yData)
  print(coeff)
  print()
  return coeff

def p_1(xValue, yValue, xData, coeff):
  return yValue + coeff[0] * (xValue - xData[0])

def p_2(xValue, p_1Value, xData, coeff):
  return p_1Value + coeff[1] * (xValue - xData[0]) * (xValue - xData[1])

def p_3(xValue, p_2Value, xData, coeff):
  return p_2Value + coeff[2] * (xValue - xData[0]) * (xValue - xData[1]) * (xValue - xData[2])

def number_3(coeff):
  xData = [7.2, 7.4, 7.5, 7.6]
  yData = [23.5492, 25.3913, 26.8224, 27.4589]
  xValue = 7.3
  p_1Value = p_1(xValue, yData[0], xData, coeff)
  p_2Value = p_2(xValue, p_1Value, xData, coeff)
  p_3Value = p_3(xValue, p_2Value, xData, coeff)
  print(p_3Value)
  print()

def hermite(zData, yData, yPrimeData):
  Q = []
  qTemp = []
  for i in range(len(yData)):
    qTemp.append(yData[i])
    qTemp.append(yData[i])
  xData = []
  for i in range(len(zData)):
    xData.append(zData[i])
    xData.append(zData[i])
  Q.append(qTemp.copy())

  # do the first one here manually
  qTemp = [0]
  for i in range(1, 2 * len(yData)):
    # if index is odd, use yPrimeData
    if (i % 2 == 1):
      qTemp.append(yPrimeData[int(i / 2)])
    else:
      qTemp.append((Q[0][i] - Q[0][i-1]) / (xData[i] - xData[i-1]))
  Q.append(qTemp.copy())

  for k in range(2, len(xData)):
    qTemp = []
    for i in range(k):
      qTemp.append(0)
    for i in range(k, len(xData)):
      Q_i_k = (Q[k-1][i] - Q[k-1][i-1]) / (xData[i] - xData[i-k])
      qTemp.append(Q_i_k)
    Q.append(qTemp.copy())
  Q = [xData] + Q
  return Q  

def number_4():
  zData = [3.6, 3.8, 3.9]
  yData = [1.675, 1.436, 1.318]
  yPrimeData = [-1.195, -1.188, -1.182]
  matrix = np.array(hermite(zData, yData, yPrimeData))
  matrix = matrix[0:len(matrix) - 1].copy()
  matrix = matrix.transpose()
  print(matrix)
  print()

def getMatrixA(xData, yData, h, dy):
  A = np.zeros((len(xData), len(xData)))
  A[0, 0] = 1
  A[-1, -1] = 1
  for i in range(1, len(xData) - 1):
    A[i, i - 1] = h[i - 1]
    A[i, i] = 2 * (h[i - 1] + h[i])
    A[i, i + 1] = h[i]
  print(A)
  print()
  return A

def getVectorb(xData, h, dy):
  b = np.zeros(len(xData))
  for i in range(1, len(xData) - 1):
    b[i] = 3 * (dy[i] / h[i] - dy[i - 1] / h[i - 1])
  print(b)
  print()
  return b

def getVectorx(A, b):
  x = np.linalg.solve(A, b)
  print(x)
  return x


def number_5():
  xData = np.array([2, 5, 8, 10])
  yData = np.array([3, 5, 7, 9])

  h = np.diff(xData)
  dy = np.diff(yData)

  A = getMatrixA(xData, yData, h, dy)

  b = getVectorb(xData, h, dy)

  x = getVectorx(A, b)

number_1()
coeff = number_2()
number_3(coeff)
number_4()
number_5()

