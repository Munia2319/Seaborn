from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#visualizing normal distribution

plt.subplot(3,4,1)
plt.title('normal distribution')
sns.distplot(random.normal(size=500), hist=False)
#visualizing bionominal distribution
plt.subplot(3,4,2)
plt.title('bionominal distribution')
sns.distplot(random.binomial(n=5, p=0.5, size=1000), hist=True, kde=False)
#Visualizing difference between normal and binominal distribution
plt.subplot(3,4,3)
plt.title('normal and binominal distribution')
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
#Visualization of Poisson Distribution
plt.subplot(3,4,4)
plt.title('Poisson Distribution')
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
#Difference Between Normal and Poisson Distribution
plt.subplot(3,4,5)
plt.title('Normal and Poisson Distribution')
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
#Difference Between Poisson and Binomial Distribution
plt.subplot(3,4,6)
plt.title('Poisson and Binomial Distribution')
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
#Visualization of Uniform Distribution
plt.subplot(3,4,7)
plt.title('Uniform Distribution')
sns.distplot(random.uniform(size=1000), hist=False)
#Visualization of Chi Square Distribution
plt.subplot(3,4,8)
plt.title('Chi Square Distribution')
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
#Visualization of Rayleigh Distribution
plt.subplot(3,4,9)
plt.title('Rayleigh Distribution')
sns.distplot(random.rayleigh(size=1000), hist=False)
#Visualization of Pareto Distribution
plt.subplot(3,4,10)
plt.title('Pareto Distribution')
sns.distplot(random.pareto(a=2, size=1000), kde=False)
#Visualization of Zipf Distribution
plt.subplot(3,4,11)
plt.title('Zipf Distribution')
x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)
plt.show()