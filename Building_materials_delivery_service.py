import tkinter as tk
from tkinter import messagebox

class Sack:
    def __init__(self, content, weight):
        self.content = content
        self.weight = weight

class Order:
    def __init__(self):
        self.sacks = []
        self.rejected = 0

    def add_sack(self, sack):
        if sack.content not in ['Cement', 'Gravel', 'Sand']:
            messagebox.showerror("Error", f"Sack rejected: Invalid content {sack.content}")
            self.rejected += 1
            return
        if sack.content == 'Cement' and (sack.weight < 24.9 or sack.weight > 25.1):
            messagebox.showerror("Error", f"Sack rejected: Invalid weight for cement {sack.weight}")
            self.rejected += 1
            return
        if sack.content in ['Gravel', 'Sand'] and (sack.weight < 49.9 or sack.weight > 50.1):
            messagebox.showerror("Error", f"Sack rejected: Invalid weight for {sack.content} {sack.weight}")
            self.rejected += 1
            return
        self.sacks.append(sack)
        sack_list.insert(tk.END, f"{sack.content} - {sack.weight}")

    def total_weight(self):
        return sum(sack.weight for sack in self.sacks)

    def calculate_price(self):
        price = 0
        c = g = s = 0
        pack=0
        for sack in self.sacks:
            if sack.content == 'Cement':
                c += 1
                price += 3
            elif sack.content == 'Gravel':
                g += 1
                price += 2
            elif sack.content == 'Sand':
                s += 1
                price += 2
            c1=c
            g1=g
            s1=s
            while True:
                if c1>0 and g1>1 and s1>1:
                    pack+=1
                    c1-=1
                    g1-=2
                    s1-=2
                else:
                    break
        packs = min(c, g//2, s//2)
        if packs > 0:
            price -= packs  # discount for each pack
        return price, packs  # total price and amount saved

def add_sack():
    content = content_var.get()
    weight = float(weight_entry.get())
    order.add_sack(Sack(content, weight))
    rejected_label.config(text=f"Number of sacks rejected: {order.rejected}")

def calculate_price():
    price, saved = order.calculate_price()
    og_price=price+saved
    c = len([sack for sack in order.sacks if sack.content == 'Cement'])
    g = len([sack for sack in order.sacks if sack.content == 'Gravel'])
    s = len([sack for sack in order.sacks if sack.content == 'Sand'])
    total_weight = order.total_weight()
    messagebox.showinfo("Price", f"Number of cement sacks: {c}\nNumber of gravel sacks: {g}\nNumber of sand sacks: {s}\nTotal weight: {total_weight}\nPrice for the order: ${og_price}\nPrice after discount: ${price}\nNumber of spacial packs: {saved}\nAmount saved: ${saved}")

order = Order()

root = tk.Tk()

content_label = tk.Label(root, text="Content (Cement, Gravel, Sand):")
content_label.pack()
content_var = tk.StringVar(root)
content_var.set('Cement')  # default value
content_option = tk.OptionMenu(root, content_var, 'Cement', 'Gravel', 'Sand')
content_option.pack()

weight_label = tk.Label(root, text="Weight:")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

add_button = tk.Button(root, text="Add sack", command=add_sack)
add_button.pack()

sack_list = tk.Listbox(root)
sack_list.pack()

rejected_label = tk.Label(root, text=f"Number of sacks rejected: {order.rejected}")
rejected_label.pack()

price_button = tk.Button(root, text="Calculate price", command=calculate_price)
price_button.pack()

root.mainloop()
