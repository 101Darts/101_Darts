import tkinter as tk
from tkinter import filedialog
import numpy as np
import pandas as pd
from scipy.stats import multivariate_normal

class NormalDistributionFitterApp:
    def __init__(self, master):
        self.master = master
        master.title("Normal Distribution Fitter")

        self.label = tk.Label(master, text="Select Data File:")
        self.label.pack()

        self.choose_file_button = tk.Button(master, text="Choose File", command=self.choose_file)
        self.choose_file_button.pack()

        self.fit_button = tk.Button(master, text="Fit Normal Distribution", command=self.fit_normal_distribution)
        self.fit_button.pack()

        self.result_text = tk.Text(master, height=10, width=40)
        self.result_text.pack()

    def choose_file(self):
        file_path = filedialog.askopenfilename(title="Select Data File", filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.data = pd.read_csv(file_path)
            self.label.config(text=f"Selected File: {file_path}")

    def fit_normal_distribution(self):
        if hasattr(self, 'data'):
            x_data = self.data.iloc[:, 0]
            y_data = self.data.iloc[:, 1]

            mean, cov = self.fit_2D_normal(x_data, y_data)

            # Extracting additional information
            std1, std2, rho = self.get_std_and_rho(cov)

            result_text = f"Estimated Mean: {mean}\n"
            result_text += f"Estimated Covariance Matrix:\n{cov}\n"
            result_text += f"Standard Deviation (σ1): {std1}\n"
            result_text += f"Standard Deviation (σ2): {std2}\n"
            result_text += f"Correlation Coefficient (ρ): {rho}\n"

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_text)

        else:
            self.label.config(text="Please select a data file first.")

    def fit_2D_normal(self, x, y):
        data = np.vstack([x, y]).T
        mean = np.mean(data, axis=0)
        cov = np.cov(data, rowvar=False)
        return mean, cov

    def get_std_and_rho(self, cov):
        std1 = np.sqrt(cov[0, 0])
        std2 = np.sqrt(cov[1, 1])
        rho = cov[0, 1] / (std1 * std2)
        return std1, std2, rho

root = tk.Tk()
app = NormalDistributionFitterApp(root)
root.mainloop()
