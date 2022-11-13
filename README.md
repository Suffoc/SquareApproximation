# 最佳平方逼近
# Square Approximation of continuous function

## 项目背景
## Project Background

本项目为利用勒让德多项式求解指数函数在[-1,1]上的最佳逼近多项式。

This project aims to find the least square approximation of exponential function on [-1,1]

在SquareApproximation.ipynb中，首先构造勒让德多项式，然后求指数函数的最佳逼近多项式，随后计算误差，最后对误差的收敛速度进行猜测，并使用最小二乘法确定系数

In the file SquareApproximation.ipynb, we first construct Legendre Polynomials. Then we calculate the least square appximation polynomials of exponential function and its error. To decide the convergence speed of the approximation, we use several forms of functions to simulate it and use least square method to determine the parameter.

我们最终发现对于指数函数，最佳平方逼近的收敛速度为 $O((\frac{e}{n})^n)$

To conclude, we find the convergence speed of the least square appximation of exponential function is $O((\frac{e}{n})^n)$

## 文件概览
## Preview of Files

* SquareApproximation.ipynb: 源代码
* latex_formula.csv: 勒让德多项式、最佳逼近多项式、误差的解析表达式、数值表达式的latex公式
* image_result/: 图片结果
    * epsilon.eps: 不同次数逼近多项式误差
    * max_error.eps: 不同次数逼近多项式最大误差
    * log_error.eps: 不同次数逼近多项式对数最大误差
    * linear regression of logerror to n.eps: 对数误差线性回归
    * linear regression of loglogerror to logn.eps: 对数对数误差关于 $\ln(n)$ 的线性回归
    * 1.27 deg regression of log error to n.eps: 对数误差关于 $n^{1.27}$ 的回归
    * linear regression of log error to nlnn and n.eps: 对数误差关于 $n\ln(n)$ 的回归

* SquareApproximation.ipynb: source code
* latex_formula.csv: The latex formula of the analytical and numerical expression of Legendre Polynomials, least appriximation polynomials and errors.
* image_result/: image result
    * epsilon.eps: errors of different approximation polynimials
    * max_error.eps: errors of different approximation polynimials
    * log_error.eps: log of errors of different approximation polynimials
    * linear regression of logerror to n.eps: linear regression of log max error
    * linear regression of loglogerror to logn.eps : linear regression of log log max error to log n
    * 1.27 deg regression of log error to n.eps: regression of log max error to $n^{1.27}$
    * linear regression of log error to nlnn and n.eps: regression of log max error to $n\ln(n)$

## 代码运行环境
## Environment

| Name | Version |
| ------ | ------ |
|python|3.10|
|numpy|1.23.3|
|sympy|1.10.1|
|matplotlib|3.5.3|
