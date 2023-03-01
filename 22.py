import random
import tkinter as tk

pos = 0
arrayz = [[0 for x in range(10)] for y in range(10)]

for x in range(len(arrayz)):
  for y in range(len(arrayz[x])):
    arrayz[x][y] = random.randint(0,15)

window = tk.Tk()

for i in range(10):
    for j in range(10):
        label = tk.Label(window, text=str(arrayz[i][j]), width=2, height=1)
        label.configure(bg="gray" + str(arrayz[i][j]))
        label.grid(row=i, column=j)

window.mainloop()

print(arrayz)