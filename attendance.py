# importing required libraries
import numpy as np
import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# creating the Tkinter window
w = tk.Tk()
w.title("Student Result Analysis")
w.geometry('1200x800')
w.configure(background='#FDFD96')

# adding a figure to show the graph in the window
fig = Figure()
a = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=w)
plot_widget = canvas.get_tk_widget()

# main program where calculations are done and results are printed/plotted
def main():
    path = e.get()
    d = pd.read_excel(str(path), index_col=0, engine="openpyxl")
    total = d['TOTAL'].values
    value, count = np.unique(total, return_counts=True)
    t = dict(zip(value, count))
    a.bar(t.keys(), t.values())
    a.set_xlabel('Total Lectures Attended', fontsize=15)
    a.set_ylabel('Number of Students', fontsize=15)
    a.set_title('ATTENDANCE ANALYSIS', fontsize=20)
    fig.canvas.draw_idle()

    avg_total = d['TOTAL'].values.mean()
    avg_coa = d['COA'].values.mean()
    avg_at = d['AT'].values.mean()
    avg_cn = d['CN'].values.mean()
    avg_os = d['OS'].values.mean()
    avg_pyt = d['PYTHON'].values.mean()

    dic_total = dict(zip(d.index, d['TOTAL'].values))
    max_total = max(d['TOTAL'].values)
    T.insert(tk.INSERT, "\n1. ")
    for i_total in dic_total.keys():
        if dic_total[i_total] == max_total:
            T.insert(tk.INSERT, str(i_total) + ",")
    T.insert(tk.INSERT, " Attended the maximum classes: " + str(max_total) + ".\n\n")

    dic_coa = dict(zip(d.index, d['COA'].values))
    max_coa = max(d['COA'].values)
    T.insert(tk.INSERT, "2. ")
    for i_coa in dic_coa.keys():
        if dic_coa[i_coa] == max_coa:
            T.insert(tk.INSERT, str(i_coa) + ",")
    T.insert(tk.INSERT, " Attended maximum COA classes: " + str(max_coa) + ".\n\n")

    dic_at = dict(zip(d.index, d['AT'].values))
    max_at = max(d['AT'].values)
    T.insert(tk.INSERT, "3. ")
    for i_at in dic_at.keys():
        if dic_at[i_at] == max_at:
            T.insert(tk.INSERT, str(i_at) + ",")
    T.insert(tk.INSERT, " Attended maximum AT classes: " + str(max_at) + ".\n\n")

    dic_cn = dict(zip(d.index, d['CN'].values))
    max_cn = max(d['CN'].values)
    T.insert(tk.INSERT, "4. ")
    for i_cn in dic_cn.keys():
        if dic_cn[i_cn] == max_cn:
            T.insert(tk.INSERT, str(i_cn) + ",")
    T.insert(tk.INSERT, " Attended maximum CN classes: " + str(max_cn) + ".\n\n")

    dic_os = dict(zip(d.index, d['OS'].values))
    max_os = max(d['OS'].values)
    T.insert(tk.INSERT, "5. ")
    for i_os in dic_os.keys():
        if dic_os[i_os] == max_os:
            T.insert(tk.INSERT, str(i_os) + ",")
    T.insert(tk.INSERT, " Attended maximum OS classes: " + str(max_os) + ".\n\n")

    dic_pyt = dict(zip(d.index, d['PYTHON'].values))
    max_pyt = max(d['PYTHON'].values)
    T.insert(tk.INSERT, "6. ")
    for i_pyt in dic_pyt.keys():
        if dic_pyt[i_pyt] == max_pyt:
            T.insert(tk.INSERT, str(i_pyt) + ",")
    T.insert(tk.INSERT, " Attended maximum PYTHON classes: " + str(max_pyt) + ".\n\n")

    above_avg = 0
    above_pass = 0
    pass_marks = 40
    for j in d['TOTAL'].values:
        if j > avg_total:
            above_avg += 1
    for k in d['TOTAL'].values:
        if k >= pass_marks:
            above_pass += 1

    T.insert(tk.INSERT, "7. Average ATTENDANCE of students is " + str("%.2f" % avg_total) + " and " + str(
        above_avg) + " students have attended above average attendance.\n\n")
    T.insert(tk.INSERT, "8. Average attendance in COA is " + str("%.2f" % avg_coa) + ".\n\n")
    T.insert(tk.INSERT, "9. Average attendance in AT is " + str("%.2f" % avg_at) + ".\n\n")
    T.insert(tk.INSERT, "10. Average attendance in CN is " + str("%.2f" % avg_cn) + ".\n\n")
    T.insert(tk.INSERT, "11. Average attendance in OS is " + str("%.2f" % avg_os) + ".\n\n")
    T.insert(tk.INSERT, "12. Average attendance in PYTHON is " + str("%.2f" % avg_pyt) + ".\n\n")
    T.insert(tk.INSERT,
             "13. The pass ATTENDANCE is " + str(pass_marks) + " and " + str(above_pass) + " students have passed.\n\n")
    T.config(state="disabled")

# creating different Tkinter widgets and defining their positions in the tkinter window
label = tk.Label(w, text='STUDEN ATTENDANCE ANALYSIS', font=("Arial Bold", 15), fg="red", bg="#FDFD96").grid(row=2,
                                                                                                              column=2)
enter = tk.Label(w, text='enter path of excel file', font=15, bg="#FDFD96").grid(row=4, column=2)
e = tk.Entry(w, width=60)
e.grid(row=4, column=3)
b = tk.Button(w, text='Go', command=main).grid(row=4, column=4)
plot_widget.grid(row=5, column=2, rowspan=15, columnspan=50)
b1 = tk.Button(w, text='Quit', command=w.destroy)
b1.grid(row=22, column=3)
T = tk.Text(w, fg="blue", bg="pink", width=55, height=40)
T.grid(row=5, column=1)
w.mainloop()