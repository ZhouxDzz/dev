import pandas as pd
import matplotlib.pyplot as plt

csv_file = '../data/NT11.csv'
feed = 0.5  # 进给量，单位 mm

df = pd.read_csv(csv_file)
df.columns = [col.strip() for col in df.columns]  # 清理列名

# 找最外层一条线（比如最上面一行）
y_max = df['Y'].max()
edge_line = df[df['Y'] > y_max - 0.01].copy()
shifted_line = edge_line.copy()
shifted_line['X'] += feed

# 画图
plt.scatter(edge_line['X'], edge_line['T'], c='red', label='Original')
plt.scatter(shifted_line['X'], shifted_line['T'], c='blue', label='Shifted')
plt.xlabel('X (mm)')
plt.ylabel('Temperature (°C)')
plt.title('Feed-wise Temperature Shift')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('../results/feed_shift_plot.png', dpi=150)
print("✅ 图已保存：results/feed_shift_plot.png")
