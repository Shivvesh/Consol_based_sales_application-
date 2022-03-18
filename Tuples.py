from tkinter import *

root=Tk()
root.title("Tuple")
root.configure(bg = "green")
root.geometry("400x400")

month = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)

max_profit_month = month[max_profit_index]
print("The maximum profits of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month))

min_profit = min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month = month[min_profit_index]
print("The minimum profits of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month))




