# Regression In Machine Learning

## 1. Linear Regression
Linear Regression is a supervised learning technique and it aims to get a function of input(x values) and output(y values) resulting in f(x)=y function.The equation of line is in the form of **y=mx+c**,where m is the slope of the line and c is the intercept of the line.

Functions and formulas involved in Linear Regression as as follows:
1. Generate Hypothesis
We take the equation as **y=mΘ1+Θ0** and both θ are stored in a array of size (2,1).
2. Finding Gradient and Gradient Descent
Gradient Descent is used to update both θ values.Formula for gradient descent is **x = x - l_r(gradient)**, where x is the value we want to update,l_r is the learning rate(constant)and,gradient  is the slope at any particular time.
3. Update θ values
The formulas for updation are as follows:
4. Error Calculation
We calculate R-square score for error calculation. The formula for the same is as follows:

## 2. Locally Weighted Regression (LOWESS)
The formula used to directly find value of θ is as follows:

where X is a array of size (m,n) 
m - no. of data points
n - no. of features (including dummy feature)

## 3. Logistic Regression
It is a supervised classification learning. The output of a particular input belongs to a particular class present in y ( 2 classes in case of binary).

The algorithm makes use of sigmod function which is as follows: g(z)=1/(1+e^(-z))

The formula for θ updation is as follows:
