import tkinter as tk
from converter import Converter

class GUI:
    def __init__(self):
        #define variables
        self.infix = ""
        self.postfix = ""
        self.prefix = ""
        #set root
        root = tk.Tk()
        self.root = root
        #set title
        root.title("Arhitmatic Notation Convertor")
        #set size
        root.geometry("400x130")
        #add labels
        tk.Label(root, text="Enter Expression:  ").grid(row=0)
        tk.Label(root, text="Infix:  ").grid(row=1, column=0, sticky=tk.W)
        tk.Label(root, text="Postfix:  ").grid(row=2, column=0, sticky=tk.W)
        tk.Label(root, text="Prefix:  ").grid(row=3, column=0, sticky=tk.W)
        self.infix_result = tk.Label(self.root, text=self.infix)
        self.infix_result.grid(row=1, column=1, sticky=tk.W)
        self.postfix_result = tk.Label(self.root, text=self.postfix)
        self.postfix_result.grid(row=2, column=1, sticky=tk.W)
        self.prefix_result = tk.Label(self.root, text=self.prefix)
        self.prefix_result.grid(row=3, column=1, sticky=tk.W)
        #add input box
        self.entry = tk.Entry(root)
        self.entry.grid(row = 0, column=1)
        #add buttons
        tk.Button(root,
            text= "Evaluate",
            command= self.evaluate
            ).grid(row=4, column=1)
        #add drop down menu
        self.mode = tk.StringVar(root)
        self.mode.set("Infix") # default mode
        w = tk.OptionMenu(root, self.mode, "Infix", "Postfix", "Prefix").grid(row=0,column=2)
        root.mainloop()

    def evaluate(self):
        converter = Converter()
        input = self.entry.get()
        mode = self.mode.get()
        print(mode, input)
        if(mode == "Infix"):
            self.infix = input
            self.postfix = converter.infix_to_postfix(input)
            self.prefix = converter.infix_to_prefix(input)
        elif(mode == "Postfix"):
            self.postfix = input
            self.infix = converter.postfix_to_infix(input)
            self.prefix = converter.postfix_to_prefix(input)
        elif(mode == "Prefix"):
            self.prefix = input
            self.postfix = converter.prefix_to_postfix(input)
            self.infix = converter.prefix_to_infix(input)
        else:
            raise  Exception(f"mode: {mode} is not defined")
        #removing old labels
        if(self.infix_result):
            self.infix_result.destroy()
            self.postfix_result.destroy()
            self.prefix_result.destroy()
        #adding new labels
        self.infix_result = tk.Label(self.root, text=self.infix)
        self.infix_result.grid(row=1, column=1, sticky=tk.W)
        self.postfix_result = tk.Label(self.root, text=self.postfix)
        self.postfix_result.grid(row=2, column=1, sticky=tk.W)
        self.prefix_result = tk.Label(self.root, text=self.prefix)
        self.prefix_result.grid(row=3, column=1, sticky=tk.W)

