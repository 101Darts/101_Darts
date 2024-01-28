import tkinter as tk
from tkinter import Label, Entry, Button
import numpy as np

# 定义不同区域的参数
radius_circle1 = 33 / 2
radius_circle2 = 13 / 2
radius_circle3 = (80 + 80 + 33) / 2
radius_circle4 = (10 + 10 + 80 + 80 + 33) / 2
radius_circle5 = (55 + 55 + 10 + 10 + 80 + 80 + 33) / 2
radius_circle6 = (10 + 10 + 55 + 55 + 10 + 10 + 80 + 80 + 33) / 2

# 计算各个区域的面积
area_circle1 = np.pi * radius_circle1**2
area_circle2 = np.pi * radius_circle2**2
area_circle3 = np.pi * radius_circle3**2
area_circle4 = np.pi * radius_circle4**2
area_circle5 = np.pi * radius_circle5**2
area_circle6 = np.pi * radius_circle6**2

# 定义各个区域的得分
score_double_bullseye = 50
score_single_bullseye = 25

def calculate_score(x, y):
    distance_from_center = np.sqrt(x**2 + y**2)

    if distance_from_center <= radius_circle2:
        a = 2
        return score_double_bullseye
    elif distance_from_center <= radius_circle1:
        a = 1
        return score_single_bullseye
    elif distance_from_center <= radius_circle3:
        a = 1
    elif distance_from_center <= radius_circle4:
        a = 3
    elif distance_from_center <= radius_circle5:
        a = 1  # 外单倍区
    elif distance_from_center <= radius_circle6:
        a = 2  # 双倍区
    else:
        a = 0

    # 处理 x 为零的特殊情况
    if x == 0:
        if y > 0:
            angle = 0
        elif y < 0:
            angle = 180
        else:
            angle = 0
    else:
        # 计算角度
        angle = (180 / np.pi) * np.arctan2(x, y)
        angle = angle % 360

    if angle < 0:
       angle += 360

    # 更新角度和 a 的标签
    angle_label.config(text=f"角度：{angle:.3f} 度")
    a_label.config(text=f"倍数为 {a}")

    # 根据提供的角度范围判断分值，并将分值乘以倍数
    if 9 < angle <= 27:
        return 1 * a  # 20分区三倍
    elif 27 < angle <= 45:
        return 18 * a  # 1分区双倍
    elif 45 < angle <= 63:
        return 4 * a  # 18分区三倍
    elif 63 < angle <= 81:
        return 13 * a  # 4分区双倍
    elif 81 < angle <= 99:
        return 6 * a  # 13分区三倍
    elif 99 < angle <= 117:
        return 10 * a  # 6分区双倍
    elif 117 < angle <= 135:
        return 15 * a  # 10分区三倍
    elif 135 < angle <= 153:
        return 2 * a  # 15分区双倍
    elif 153 < angle <= 171:
        return 17 * a  # 2分区三倍
    elif 171 < angle <= 189:
        return 3 * a  # 17分区双倍
    elif 189 < angle <= 207:
        return 19 * a  # 3分区三倍
    elif 207 < angle <= 225:
        return 7 * a  # 19分区双倍
    elif 225 < angle <= 243:
        return 16 * a  # 7分区三倍
    elif 243 < angle <= 261:
        return 8 * a  # 16分区双倍
    elif 261 < angle <= 279:
        return 11 * a  # 8分区三倍
    elif 279 < angle <= 297:
        return 14 * a  # 11分区双倍
    elif 297 < angle <= 315:
        return 9 * a  # 14分区三倍
    elif 315 < angle <= 333:
        return 12 * a  # 9分区双倍
    elif 333 < angle <= 351:
        return 5 * a  # 12分区三倍
    elif 351 < angle <= 359.999999:
        return 20 * a  # 12分区三倍
    elif 0 <= angle <= 9:
        return 20 * a  # 12分区三倍
    else:
        return 0

def on_calculate_button_click():
    x_value = float(entry_x.get())
    y_value = float(entry_y.get())
    result = calculate_score(x_value, y_value)
    result_label.config(text=f"得分：{result}")

# 创建主窗口
root = tk.Tk()
root.title("飞镖得分计算器")

# 创建输入框和标签
label_x = Label(root, text="输入 x 坐标：")
label_x.pack()

entry_x = Entry(root)
entry_x.pack()

label_y = Label(root, text="输入 y 坐标：")
label_y.pack()

entry_y = Entry(root)
entry_y.pack()

# 创建计算按钮
calculate_button = Button(root, text="计算得分", command=on_calculate_button_click)
calculate_button.pack()

# 创建显示角度的标签
angle_label = Label(root, text="")
angle_label.pack()

# 创建显示倍数的标签
a_label = Label(root, text="")
a_label.pack()

# 创建显示结果的标签
result_label = Label(root, text="")
result_label.pack()

# 启动主循环
root.mainloop()
