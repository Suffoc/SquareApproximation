import numpy as np
import sympy
from sympy import Symbol
from sympy import Rational
import matplotlib.pyplot as plt
import csv

#构造勒让德多项式，并存储在P中

x = Symbol('x')
Lgd = [sympy.numer(1), x]

for i in range(2,11):
    Lgd.append(sympy.simplify(Rational(2 * i - 1, i) * x * Lgd[i - 1] - Rational(i - 1, i) * Lgd[i - 2]))
for i in range(11):
    print(i, Lgd[i])

#构造目标函数
f = sympy.exp(x)

#计算勒让德多项式的模长
norm = []
for i in range(11):
    norm.append(sympy.integrate(Lgd[i] ** 2, (x, -1, 1)))
print(norm)

#计算f在以勒让德多项式为基的空间中的分量
coef = []
for i in range(11):
    coef.append(sympy.integrate(f * Lgd[i], (x, -1, 1))/ norm[i])
print(coef)

#由上面计算得出的系数构造最佳平方逼近多项式，以及其误差
P = []
epsilon = []
for i in range(11):
    tmp_p = 0
    for j in range(i + 1):
        tmp_p += coef[j] * Lgd[j]
    P.append(sympy.simplify(tmp_p))
    epsilon.append(sympy.simplify(f - P[i]))
for i in range(11):
    print(i, P[i], epsilon[i])

#画出图像
x_range = np.arange(-1, 1, 0.01)
for i in range(11):
    estimates = []
    for x_ in x_range:
        estimates.append(epsilon[i].evalf(subs = {x:x_}))
    estimates = np.array(estimates)
    plt.plot(x_range, estimates, label = "n=" + str(i))
plt.xlim(-1, 1.5)
plt.legend(loc='best')
plt.savefig("误差.svg", dpi=300,format='svg')
plt.show()

#上面的计算得到的都是解析解，现在求数值解
P_float = []
epsilon_float = []
for i in range(11):
    P_float.append(sympy.simplify(P[i].evalf()))
    epsilon_float.append(sympy.simplify(epsilon[i].evalf()))
for i in range(11):
    print(i, P_float[i], epsilon_float[i])

#将数值解以latex公式形式给出
latex_formula = []
for i in range(11):
    latex_formula.append([sympy.latex(P_float[i]), sympy.latex(epsilon_float[i]), sympy.latex(P[i]), sympy.latex(epsilon[i])])
with open('latex_formula.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(latex_formula)

#求极值
for i in range(11):
    dE = sympy.diff(epsilon, x)
    extreme_point = sympy.solve(dE, x)
    print(extreme_point)