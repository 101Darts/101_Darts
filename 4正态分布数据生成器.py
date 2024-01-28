import tkinter as tk
from tkinter import ttk
import numpy as np
import csv
import os
from datetime import datetime

def generate_data():
    try:
        # 从输入框获取参数
        sigma1 = float(sigma1_entry.get())
        sigma2 = float(sigma2_entry.get())
        mu1 = float(mu1_entry.get())
        mu2 = float(mu2_entry.get())
        rho = float(rho_entry.get())
        num_samples = int(num_samples_entry.get())

        # 生成二维正态分布数据
        cov_matrix = [[sigma1**2, rho * sigma1 * sigma2], [rho * sigma1 * sigma2, sigma2**2]]
        mean = [mu1, mu2]
        data = np.random.multivariate_normal(mean, cov_matrix, num_samples)

        # 获取当前日期和时间
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

        # 保存文件到指定目录
        save_path = "D:/101_International_Department_G10/CTB比赛2023/正态分布pyhton数据保存地址"
        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, f'generated_data_{current_datetime}.csv')

        # 将数据写入CSV文件
        with open(file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['X', 'Y'])
            csvwriter.writerows(data)

        result_label.config(text=f'数据生成成功，已保存到 {file_path}')

    except ValueError:
        result_label.config(text='请输入有效的数字')

# 创建主窗口
root = tk.Tk()
root.title('生成二维正态分布数据')

# 创建输入框和标签
sigma1_label = ttk.Label(root, text='σ1:')
sigma1_label.grid(row=0, column=0, padx=10, pady=5, sticky='E')
sigma1_entry = ttk.Entry(root)
sigma1_entry.grid(row=0, column=1, padx=10, pady=5)

sigma2_label = ttk.Label(root, text='σ2:')
sigma2_label.grid(row=1, column=0, padx=10, pady=5, sticky='E')
sigma2_entry = ttk.Entry(root)
sigma2_entry.grid(row=1, column=1, padx=10, pady=5)

mu1_label = ttk.Label(root, text='μ1:')
mu1_label.grid(row=2, column=0, padx=10, pady=5, sticky='E')
mu1_entry = ttk.Entry(root)
mu1_entry.grid(row=2, column=1, padx=10, pady=5)

mu2_label = ttk.Label(root, text='μ2:')
mu2_label.grid(row=3, column=0, padx=10, pady=5, sticky='E')
mu2_entry = ttk.Entry(root)
mu2_entry.grid(row=3, column=1, padx=10, pady=5)

rho_label = ttk.Label(root, text='ρ:')
rho_label.grid(row=4, column=0, padx=10, pady=5, sticky='E')
rho_entry = ttk.Entry(root)
rho_entry.grid(row=4, column=1, padx=10, pady=5)

num_samples_label = ttk.Label(root, text='生成数据数量:')
num_samples_label.grid(row=5, column=0, padx=10, pady=5, sticky='E')
num_samples_entry = ttk.Entry(root)
num_samples_entry.grid(row=5, column=1, padx=10, pady=5)

# 创建生成按钮
generate_button = ttk.Button(root, text='生成数据', command=generate_data)
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

# 创建结果标签
result_label = ttk.Label(root, text='')
result_label.grid(row=7, column=0, columnspan=2, pady=5)

# 运行主循环
root.mainloop()