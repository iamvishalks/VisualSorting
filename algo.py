
from tkinter import *
from tkinter import ttk
import random
from sorts import *

data = []


root = Tk()
root.title('Sorting Visualisation')
root.maxsize(900, 600)

root['bg'] = '#06062e'


selected_algo = StringVar()


def draw_data(data, color):

    canvas.delete("all")

    c_width = 600
    c_height = 380

    x_width = c_width/(len(data) + 1)
    offset = 4
    spacing = 1

    normalize = [i / max(data) for i in data]

    for i, height in enumerate(normalize):

        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340

        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
        #canvas.create_text(x0+((x1-x0)/2)- 10, y0, anchor= SW, text=str(data[i]), fill = 'white' )

    root.update_idletasks()


def generate():
    global data

    print(f'Selected Algo: {selected_algo.get()}')

    data = []
    for i in range(80):
        n = random.randint(0, 600)
        data.append(n)

    print(data)

    draw_data(data, ['grey' for i in range(len(data))])


def startAlgo():
    global data
    print("lol test")
    if(algo_menu.get() == 'Quick Sort'):
        quick_sort(data,0, len(data)-1, draw_data)
        draw_data(data, ['green' for x in range(len(data))])

    if(algo_menu.get() == 'Bubble Sort'):
        bubbleSort(data, draw_data)
    



ui = Frame(root, width=600, height=200, bg='#06062e')

ui.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='#06062e')

canvas.grid(row=1, column=0,  padx=10, pady=5)

Label(ui, text="Algorithm", bg='#1b1766', fg='white').grid(
    row=0, column=0, padx=5, pady=5, sticky=W)
algo_menu = ttk.Combobox(ui, textvariable=selected_algo, values=[
                         'Bubble Sort','Quick Sort'])
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)


Button(ui, text="Start", command=startAlgo, bg='#910a1e',
       fg='white').grid(row=0, column=3, padx=5, pady=5)


Button(ui, text="Generate", command=generate, bg='#910a1e',
       fg='white').grid(row=0, column=4, padx=5, pady=5)


root.mainloop()
