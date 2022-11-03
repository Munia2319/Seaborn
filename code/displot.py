import matplotlib.pyplot as plt
import seaborn as sns
plt.subplot(2,1,1)

sns.distplot([0,1,2,3,4,5])
plt.subplot(2,1,2)
sns.distplot([0, 1, 2, 3, 4, 5],hist=False)

plt.show()