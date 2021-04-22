from tkinter import *
from tkinter import filedialog
from gauss import *
import time
from tkinter import messagebox


class Window:
    def __init__(self):
        self.window = Tk()  # Create a window
        self.window.title("Linear systems")  # Set a title
        self.window.geometry("800x500")

        self.lframe_destroy = LabelFrame(self.window)
        self.lframe_destroy.grid(column=0, row=0)
        self.start_gaussian()

        button_exit = Button(self.window, text="Exit", command=exit)
        button_exit.grid(column=5, row=15)

        button_restart = Button(self.window, text="Restart", command=self.restart)
        button_restart.grid(column=4, row=15)
        self.window.mainloop()  # Create an event loop

# -------- Gaussian -----------------------------------------------------------------------------------
    def restart(self):
        self.lframe_destroy.destroy()
        self.lframe_destroy = LabelFrame(self.window)
        self.lframe_destroy.grid(column=1, row=0)
        self.start_gaussian()

    def start_gaussian(self):
        intro = Text(self.lframe_destroy, height=6, width=70)
        intro.grid(column=0, row=0)
        intro.insert(END, 'Gaussian elimination method\nApplication allows to solve a linear system of the form:'
                          '\nAx = b\nA matrix n x n \nb vector of dimension n')

        self.lframe_destroy.grid()

        self.lframe_mat = LabelFrame(self.lframe_destroy, text="Load matrix")
        self.lframe_mat.grid(column=0, row=3, padx=20, pady=20)

        self.tmp = LabelFrame(self.lframe_mat)
        self.tmp.grid()
        self.b1 = Button(self.tmp, text="Browse a file", command=self.read_mat_opt1)
        self.b2 = Button(self.tmp, text="Insert", command=self.read_mat_opt2)
        self.b1.grid(column=1, row=4)
        self.b2.grid(column=2, row=4)

    def read_mat_opt1(self):
        self.tmp.destroy()
        self.filename = filedialog.askopenfilename(
            initialdir="/C:/Users/wikis/PycharmProjects/Project_ISEG",
            title="Select A File",
            filetype=(("txt files", "*.txt"), ("all files", "*.*")))
        # Change label contents
        self.lfile_mat = Label(self.lframe_mat, text="File Opened: " + self.filename)
        self.lfile_mat.grid(column=2, row=6)
        #add OK button
        self.bconfirm_mat = Button(self.lframe_mat, text="OK", command=self.read_matrix_file)
        self.bconfirm_mat.grid(column=5, row=7)

    def read_matrix_file(self):
        try:
            self.A = MyMatrix.load_from_file(self.filename)
            l1 = Label(self.lframe_mat, text="Matrix was loaded")
            l1.grid(column=1, row=5)
            b1 = Button(self.lframe_mat, text="Next", command=self.vec_initate)
            b1.grid(column=3, row=6)
            self.b1.destroy()
            self.bconfirm_mat.destroy()
        except RuntimeError as err:
            messagebox.showerror("Error", message=err)

    def read_mat_opt2(self):
        self.tmp.destroy()
        self.tmp = LabelFrame(self.lframe_mat)
        self.tmp.grid()
        self.l1 = Label(self.tmp, text='Insert a matrix: ex. [[1.5, 2], [3.1,4]] (1.5,2 - first row etc)')
        self.l1.grid(column=2, row=6)
        self.mat = StringVar()
        self.e1 = Entry(self.tmp, textvariable=self.mat)
        self.e1.grid(row=6, column=3)
        self.b1 = Button(self.tmp, text="Submit", command=self.read_mat_input).grid(column=4, row=6)

    def read_mat_input(self):
        try:
            self.tmp.destroy()
            self.list_mat = eval(self.mat.get())
            self.A = MyMatrix(self.list_mat)
            self.l1 = Label(self.lframe_mat, text="Matrix was created")
            self.l1.grid(column=1, row=8)
            self.b1 = Button(self.lframe_mat, text="Next", command=self.vec_initate)
            self.b1.grid(column=3, row=10)
        except RuntimeError as err:
            messagebox.showerror("Error", message=err)

    # del mat lf and create a one for vec
    def vec_initate(self):
        self.lframe_mat.destroy()
        self.lframe_vec = LabelFrame(self.lframe_destroy, text="Load vector")
        self.lframe_vec.grid(column=0, row=2, padx=20, pady=20)
        self.tmp = LabelFrame(self.lframe_vec)
        self.tmp.grid()
        self.b1 = Button(self.tmp, text="Browse a file", command=self.read_vec_opt1)
        self.b2 = Button(self.tmp, text="Generate a vector", command=self.read_vec_opt2)
        self.b3 = Button(self.tmp, text="Insert", command=self.read_vec_opt3)
        self.b1.grid(column=1, row=4)
        self.b2.grid(column=2, row=4)
        self.b3.grid(column=3, row=4)

    def read_vec_opt1(self):
        self.tmp.destroy()
        self.filename_vec = filedialog.askopenfilename(
            initialdir="/C:/Users/wikis/OneDrive/Documents/Przeniesc na dysk/ISEG - semestr 3/Python/Projekt/MAtrices_v2",
            title="Select A File",
            filetype=(("txt files", "*.txt"), ("all files", "*.*")))
        # Change label contents
        self.lfile_vec = Label(self.lframe_vec, text="File Opened: " + self.filename_vec)
        self.lfile_vec.grid(column=2, row=6)
        #add OK button
        self.b1 = Button(self.lframe_vec, text="OK", command=self.read_vec_ok1)
        self.b1.grid(column=5, row=7)

    def read_vec_opt2(self):
        self.tmp.destroy()
        self.tmp = LabelFrame(self.lframe_vec)
        self.tmp.grid()
        self.l1 = Label(self.tmp, text='Length of a vector: ')
        self.l1.grid(column=2, row=6)
        self.len = IntVar()
        self.e1 = Entry(self.tmp, textvariable=self.len)
        self.e1.grid(row=6, column=3)
        self.b1 = Button(self.tmp, text="Submit", command=self.read_vec_ok2).grid(column=4, row=6)

    def read_vec_opt3(self):
        self.tmp.destroy()
        self.tmp = LabelFrame(self.lframe_vec)
        self.tmp.grid()
        self.l1 = Label(self.tmp, text='Insert a vector: ex. 1 2 3 ')
        self.l1.grid(column=2, row=6)
        self.vec = StringVar()
        self.e1 = Entry(self.tmp, textvariable=self.vec)
        self.e1.grid(row=6, column=3)
        self.b1 = Button(self.tmp, text="Submit", command=self.read_vec_ok3).grid(column=4, row=6)

    def read_vec_ok1(self):
        try:
            self.b1.destroy()
            self.b = MyVector.load_from_file(self.filename_vec)
            self.l1 = Label(self.lframe_vec, text="Vector was loaded")
            self.l1.grid(column=1, row=8)
            self.b1 = Button(self.lframe_vec, text="Next", command=self.gauss_exe)
            self.b1.grid(column=3, row=10)
        except RuntimeErroras as err:
            messagebox.showerror("Error", message=err)

    def read_vec_ok2(self):
        try:
            self.tmp.destroy()
            self.b = MyVector.random_vector(self.len.get())
            self.l1 = Label(self.lframe_vec, text="Vector was loaded")
            self.l1.grid(column=1, row=8)
            self.b1 = Button(self.lframe_vec, text="Next", command=self.gauss_exe)
            self.b1.grid(column=3, row=10)
        except RuntimeError as err:
            messagebox.showerror("Error", message=err)

    def read_vec_ok3(self):
        try:
            self.tmp.destroy()
            self.list_vec = [float(x) for x in list(self.vec.get().split())]
            self.b = MyVector(self.list_vec)
            self.l1 = Label(self.lframe_vec, text="Vector was created")
            self.l1.grid(column=1, row=8)
            self.b1 = Button(self.lframe_vec, text="Next", command=self.gauss_exe)
            self.b1.grid(column=3, row=10)
        except RuntimeError as err:
            messagebox.showerror("Error", message=err)

    def gauss_exe(self):
        self.lframe_vec.destroy()
        start_time = time.time()
        self.lframe_gauss = LabelFrame(self.lframe_destroy, text="Results of Gauss")

        try:
            tmp = gauss(self.A, self.b)
            self.x = tmp[0]
            num_of_swaps = tmp[1]
            num_of_ope = tmp[2]

            self.lframe_gauss.grid(column=0, row=2, padx=20, pady=20)
            self.c1 = Checkbutton(self.lframe_gauss, text='Print X vector', command=self.print_x)
            self.c1.grid(column=1, row=1)
            l2 = Label(self.lframe_gauss, text="Number of swaps: " + str(num_of_swaps)).grid(column=2, row=2)
            l3 = Label(self.lframe_gauss, text="Number of operations: " + str(num_of_ope)).grid(column=2, row=3)
            l4 = Label(self.lframe_gauss, text="Check : " + str(check_gauss(self.A, self.x, self.b))).grid(column=2, row=4)
            l5 = Label(self.lframe_gauss, text="Time consumption : %s seconds " % (time.time() - start_time)).grid(column=2, row=5)
            self.c2 = Checkbutton(self.lframe_gauss, text='Save X vector to file', command=self.save_x)
            self.c2.grid(column=1, row=6)
            self.c3 = Checkbutton(self.lframe_gauss, text='Save b vector to file', command=self.save_b)
            self.c3.grid(column=1, row=7)
            self.c4 = Checkbutton(self.lframe_gauss, text='Save A matrix to file', command=self.save_A)
            self.c4.grid(column=1, row=8)

        except RuntimeError as err:
            messagebox.showerror("Error", message=err)

    def print_x(self):
        l1 = Label(self.lframe_gauss, text="X vector: " + str(round_vec_x(self.x))).grid(column=2, row=1)
        self.c1.destroy()

    def save_x(self):
        try:
            self.x.save_to_file("x_gauss.txt")
            self.c2.destroy()
            l1 = Label(self.lframe_gauss, text="File saved as x_gauss.txt").grid(column=2,row=6)
        except RuntimeError as err:
            messagebox.showerror("Error", message=err)

    def save_b(self):
        try:
            path = str("Vector_file_%d.txt" % (len(self.b)-1))
            self.b.save_to_file(path)
            self.c3.destroy()
            l1 = Label(self.lframe_gauss, text="File saved as %s" % path).grid(column=2,row=7)
        except RuntimeError as err:
            messagebox.showerror("Error", message=err)

    def save_A(self):
        try:
            path = str("Matrix_from_gauss_%d.txt" % (self.A.get_row()-1))
            self.A.save_to_file(path)
            self.c4.destroy()
            l1 = Label(self.lframe_gauss, text="File saved as %s " % path).grid(column=2,row=8)
        except RuntimeError as err:
            messagebox.showerror("Error", message=err)
    # ----------------------------------------------------------------------------


Window()





