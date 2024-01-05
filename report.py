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
    a.set_xlabel('Total Marks', fontsize=15)
    a.set_ylabel('Number of Students', fontsize=15)
    a.set_title('RESULT ANALYSIS', fontsize=20)
    fig.canvas.draw_idle()

    avg_total = d['TOTAL'].values.mean()
    avg_coa = d['COA'].values.mean()
    avg_at = d['AT'].values.mean()
    avg_cn = d['CN'].values.mean()
    avg_os = d['OS'].values.mean()
    avg_maths = d['MATHS'].values.mean()

    dic_total = dict(zip(d.index, d['TOTAL'].values))
    max_total = max(d['TOTAL'].values)
    T.insert(tk.INSERT, "\n1. ")
    for i_total in dic_total.keys():
        if dic_total[i_total] == max_total:
            T.insert(tk.INSERT, str(i_total) + ",")
    T.insert(tk.INSERT, " secured the highest marks in total - " + str(max_total) + ".\n\n")

    dic_coa = dict(zip(d.index, d['COA'].values))
    max_coa = max(d['COA'].values)
    T.insert(tk.INSERT, "2. ")
    for i_coa in dic_coa.keys():
        if dic_coa[i_coa] == max_coa:
            T.insert(tk.INSERT, str(i_coa) + ",")
    T.insert(tk.INSERT, " secured the highest marks in COA - " + str(max_coa) + ".\n\n")

    dic_maths = dict(zip(d.index, d['MATHS'].values))
    max_maths = max(d['MATHS'].values)
    T.insert(tk.INSERT, "3. ")
    for i_maths in dic_maths.keys():
        if dic_maths[i_maths] == max_maths:
            T.insert(tk.INSERT, str(i_maths) + ",")
    T.insert(tk.INSERT, " secured the highest marks in Mathematics - " + str(max_maths) + ".\n\n")

    dic_at = dict(zip(d.index, d['AT'].values))
    max_at = max(d['AT'].values)
    T.insert(tk.INSERT, "4. ")
    for i_at in dic_at.keys():
        if dic_at[i_at] == max_at:
            T.insert(tk.INSERT, str(i_at) + ",")
    T.insert(tk.INSERT, " secured the highest marks in AT - " + str(max_at) + ".\n\n")

    dic_cn = dict(zip(d.index, d['CN'].values))
    max_cn = max(d['CN'].values)
    T.insert(tk.INSERT, "5. ")
    for i_cn in dic_cn.keys():
        if dic_cn[i_cn] == max_cn:
            T.insert(tk.INSERT, str(i_cn) + ",")
    T.insert(tk.INSERT, " secured the highest marks in CN - " + str(max_cn) + ".\n\n")

    dic_os = dict(zip(d.index, d['OS'].values))
    max_os = max(d['OS'].values)
    T.insert(tk.INSERT, "6. ")
    for i_os in dic_os.keys():
        if dic_os[i_os] == max_os:
            T.insert(tk.INSERT, str(i_os) + ",")
    T.insert(tk.INSERT, " secured the highest marks in OS - " + str(max_os) + ".\n\n")

    above_avg = 0
    above_pass = 0
    pass_marks = 200
    for j in d['TOTAL'].values:
        if j > avg_total:
            above_avg += 1
    for k in d['TOTAL'].values:
        if k >= pass_marks:
            above_pass += 1

    T.insert(tk.INSERT, "7. Average marks of students is - " + str("%.2f" % avg_total) + " and " + str(
        above_avg) + " students have secured marks above average marks.\n\n")
    T.insert(tk.INSERT, "8. Average marks in COA is - " + str("%.2f" % avg_coa) + ".\n\n")
    T.insert(tk.INSERT, "9. Average marks in Mathematics is - " + str("%.2f" % avg_maths) + ".\n\n")
    T.insert(tk.INSERT, "10. Average marks in AT is -  " + str("%.2f" % avg_at) + ".\n\n")
    T.insert(tk.INSERT, "11. Average marks in CN is - " + str("%.2f" % avg_cn) + ".\n\n")
    T.insert(tk.INSERT, "12. Average marks in OS is -  " + str("%.2f" % avg_os) + ".\n\n")
    T.insert(tk.INSERT,
             "13. The pass marks is - " + str(pass_marks) + " and " + str(above_pass) + " students have passed.\n\n")
    T.config(state="disabled")


# creating different Tkinter widgets and defining their positions in the tkinter window
label = tk.Label(w, text='CLASS RESULTS ANALYSIS TOOL FOR TEACHERS', font=("Arial Bold", 15), fg="red", bg="#FDFD96").grid(row=2,
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