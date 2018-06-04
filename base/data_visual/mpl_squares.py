import matplotlib.pyplot  as plt

# 折线图
squares = [1, 4, 6, 16, 25]
plt.plot(squares)

# 设置显示样式
plt.title("Square Numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("Square of values", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
plt.show()

