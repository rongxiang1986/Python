from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# 第一部分 测试数据准备

# 生成测试数据
sample_normal_data = random.normal(size=1000)
sample_random_data = random.random(size=1000)

# 可视化
import matplotlib.pyplot as plt

Grid_plot = plt.GridSpec(1, 2, wspace = 0.8,hspace = 0.6)


#sns.boxplot(ax=axes[0, 0], data=sample_normal_data)
Grid_plot[0, 0] = sns.histplot(sample_normal_data, kde=True)
Grid_plot[0, 1] = sns.histplot(sample_random_data, kde=True)
#sns.boxplot(ax=axes[0, 1], data=sample_random_data)
plt.subplot(Grid_plot[0, 0])
plt.subplot(Grid_plot[0, 1])
plt.show()
