import tkinter as tk
from tkinter import messagebox
from converter import Converter
from tree_generator import generate
from structures.Queue import Queue

class GUI:
    def __init__(self):
        #define state variables
        self.infix = ""
        self.postfix = ""
        self.prefix = ""
        self.isInTreeMode = False
        #set root
        root = tk.Tk()
        self.root = root
        #set title
        root.title("Infix Postfix Prefix Converter")
        #add labels
        tk.Label(root, text="Enter Expression:  ").grid(row=0, sticky=(tk.N, tk.S, tk.W))
        tk.Label(root, text="Infix:  ").grid(row=1, column=0, sticky=(tk.N, tk.S, tk.W))
        tk.Label(root, text="Postfix:  ").grid(row=2, column=0, sticky=(tk.N, tk.S, tk.W))
        tk.Label(root, text="Prefix:  ").grid(row=3, column=0, sticky=(tk.N, tk.S, tk.W))
        self.addResultLabels()
        #add input box
        self.entry = tk.Entry(root)
        self.entry.grid(row = 0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        #add buttons
        self.evaluateButton = tk.Button(root,
            text= "Evaluate",
            command= self.evaluate
        )
        self.evaluateButton.grid(row=4, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.renderTreeButton = tk.Button(root,
            text= "View Tree",
            command= self.renderTree
        )
        self.renderTreeButton.grid(row=4, column=2, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.renderTreeButton["state"] = "disable"
        #resizing configs
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.minsize(400, 130)
        root.maxsize(500, 130)
        root.resizable(True,False)
        root.mainloop()

    def evaluate(self):
        converter = Converter()
        input = self.entry.get().replace(" ","")

        if input == "" or input == None:
            self.resetExpressions()
            return

        #validate expression
        try:
            converter.validateExpression(input)
        except:
            self.showInvalidExpressionDialog()
            self.resetExpressions()
            return

        mode = converter.detectMode(input)
        print(mode, input)

        try:
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
        except:
            self.showInvalidExpressionDialog()
            self.resetExpressions()
            return
        self.renderTreeButton["state"] = "normal"
        self.addResultLabels()

    def renderTree(self):
        # do not open a new window if it is already open
        if self.isInTreeMode:
            return
        self.isInTreeMode = True

        if not self.postfix:
            self.showEmptyExpressionDialog()
            return
        tree = generate(self.postfix)
        depth = tree.depth
        treeWindow = tk.Toplevel(self.root)
        self.treeWindow = treeWindow
        # sets the title of the
        # Toplevel widget
        treeWindow.title("Expression Tree")
        # set closing protocol
        treeWindow.protocol("WM_DELETE_WINDOW", self.onTreeWindowClose)
        # sets the geometry of toplevel
        d = 2 ** (depth-1) * 6 # distance between same level nodes
        canvas_width = 4*d if 4*d>250 else 250 
        canvas_height = 60+(30*depth) if 60+(25*depth)>250 else 250
        
        treeWindow.geometry(f"{canvas_width}x{10+canvas_height}")
    
        #adding a custom method to Canvas class
        def _create_circle(self, x, y, r = 9, **kwargs):
            return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
        tk.Canvas.create_circle = _create_circle

        # setting up canvas and horizental scrollbar
        canvas = tk.Canvas(treeWindow, width=canvas_width, height=canvas_height, borderwidth=0, highlightthickness=0, scrollregion=(0,0,canvas_width,canvas_height)
        )
        canvas.pack(expand=True, fill=tk.BOTH)
        hbar=tk.Scrollbar(treeWindow,orient=tk.HORIZONTAL)
        hbar.pack(side=tk.BOTTOM,fill=tk.X)
        hbar.config(command=canvas.xview)
        canvas.config(xscrollcommand=hbar.set)
        ''' 
        adding entire tree to queue
        list's first element is the tree
        the second element is the width of the node during render
        the "h" variable tracks the height of the node during render
        bfs algorithm is being used to traverse the tree
        '''
        queue = Queue()
        queue.add([tree,canvas_width/2]) 
        h = 40
        while not queue.isEmpty():
            next_queue = Queue()
            while not queue.isEmpty():
                [tree, w] = queue.pop()
                canvas.create_circle(w,h,fill="black")
                canvas.create_text(w,h,text=tree.data,fill="white")
                if tree.left != None:
                    l = canvas.create_line(w,h,w-d,h+25,fill="black")
                    # making sure the line is not rendered on top of the text
                    canvas.tag_lower(l) 
                    next_queue.add([tree.left,w-d])
                if tree.right != None:
                    l = canvas.create_line(w,h,w+d,h+25,fill="black")
                    # making sure the line is not rendered on top of the text
                    canvas.tag_lower(l)
                    next_queue.add([tree.right,w+d])
            d /= 2
            h += 30
            queue = next_queue


    def addResultLabels(self):
        # removing old labels
        if(hasattr(self,"infix_result")):
            self.infix_result.destroy()
            self.postfix_result.destroy()
            self.prefix_result.destroy()
        #adding new labels
        self.infix_result = tk.Label(self.root, text=self.infix)
        self.infix_result.grid(row=1, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.postfix_result = tk.Label(self.root, text=self.postfix)
        self.postfix_result.grid(row=2, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.prefix_result = tk.Label(self.root, text=self.prefix)
        self.prefix_result.grid(row=3, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))

    def showEmptyExpressionDialog(self):
        messagebox.showerror('Expression Error', 'Error: No Expression!')

    def showInvalidExpressionDialog(self):
        messagebox.showerror('Expression Error', 'Error: Invalid Expression!')

    def resetExpressions(self):
        self.postfix = ""
        self.infix = ""
        self.prefix = ""
        self.renderTreeButton["state"] = 'disable'
        self.addResultLabels()

    def onTreeWindowClose(self):
        self.isInTreeMode = False
        self.treeWindow.destroy()