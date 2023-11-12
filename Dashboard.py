import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from dashdata import sales_data, inventory_data, product_data, sales_year_data, invent_month_data

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#527a7a", "#85adad", "#434d4d", "#141f1f", "#a3c2c2"])

fig1, ax1 = plt.subplots()
ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Product Sales")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")
#plt.show()

fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), inventory_data.values())
ax2.set_title("Product Inventory")
ax2.set_xlabel("Inventory")
ax2.set_ylabel("Product")
#plt.show()

fig3, ax3 = plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys(), autopct="%1.1f%%")
ax3.set_title("Product Breakdown")
#plt.show()

fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title("Sales by Year")
ax4.set_xlabel("Year")
ax4.set_ylabel("Sales")
#plt.show()

fig5, ax5 = plt.subplots()
ax5.fill_between(invent_month_data.keys(), invent_month_data.values())
ax5.set_title("Inventory by Month")
ax5.set_xlabel("Month")
ax5.set_ylabel("Inventory")
#plt.show()

root = tk.Tk()
root.title("Dashboard")
root.state("zoomed")

side_frame = tk.Frame(root, bg="#141f1f")
side_frame.pack(side="left", fill='y')

label = tk.Label(side_frame, text="Dashboard", bg="#141f1f", fg="white", font=20)
label.pack(pady=30, padx=10)

charts_frame = tk.Frame(root)
charts_frame.pack()

firstFrame = tk.Frame(root)
firstFrame.pack(fill = "both", expand = True)

canvas1 = FigureCanvasTkAgg(fig1, firstFrame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig5, firstFrame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas4 = FigureCanvasTkAgg(fig4, firstFrame)
canvas4.draw()
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)



secondFrame = tk.Frame(root)
secondFrame.pack(fill="both", expand=True)

canvas3 = FigureCanvasTkAgg(fig3, secondFrame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)



canvas5 = FigureCanvasTkAgg(fig2, secondFrame)
canvas5.draw()
canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)


root.mainloop()