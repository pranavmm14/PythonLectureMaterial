# Python GUI Tkinter Module

**Introduction to Tkinter**
- **Overview**: Tkinter is Python's standard GUI (Graphical User Interface) package. It is the most commonly used method for creating simple and functional GUIs.
- **Key Features**: 
  - Lightweight and easy to use.
  - Comes with Python, no need for installation.
  - Supports multiple platforms (Windows, macOS, Linux).

**Widgets in Tkinter**
- **Definition**: Widgets are the building blocks of any Tkinter GUI application. They are the interactive elements like buttons, labels, text boxes, etc.
- **Common Widgets**:
  - Button, Canvas, Label, Entry, Listbox, Menu, etc.

**Tkinter Geometry**
- **Geometry Managers**: Tkinter provides three geometry managers to control the layout of widgets:
  - **pack()**: Arranges widgets in blocks before placing them in the parent widget.
  - **grid()**: Places widgets in a 2D grid.
  - **place()**: Places widgets at an absolute position you define.

**Python Tkinter Button**
- **Purpose**: Creates a clickable button that can trigger events.
- **Example**:
  ```python
  from tkinter import Tk, Button

  def on_click():
      print("Button Clicked!")

  root = Tk()
  button = Button(root, text="Click Me", command=on_click)
  button.pack()
  root.mainloop()
  ```

**Python Tkinter Canvas**
- **Purpose**: Used for drawing shapes, images, and other complex layouts.
- **Example**:
  ```python
  from tkinter import Tk, Canvas

  root = Tk()
  canvas = Canvas(root, width=200, height=100)
  canvas.create_line(0, 0, 200, 100)
  canvas.pack()
  root.mainloop()
  ```

**Python Tkinter CheckButton**
- **Purpose**: Creates a checkbox that users can select or deselect.
- **Example**:
  ```python
  from tkinter import Tk, Checkbutton, IntVar

  root = Tk()
  var = IntVar()
  checkbutton = Checkbutton(root, text="Option", variable=var)
  checkbutton.pack()
  root.mainloop()
  ```

**Python Tkinter Entry**
- **Purpose**: Creates a text entry widget that allows users to input text.
- **Example**:
  ```python
  from tkinter import Tk, Entry

  root = Tk()
  entry = Entry(root, width=30)
  entry.pack()
  root.mainloop()
  ```

**Python Tkinter Frame**
- **Purpose**: Acts as a container to group and organize other widgets.
- **Example**:
  ```python
  from tkinter import Tk, Frame

  root = Tk()
  frame = Frame(root, bg="lightgrey")
  frame.pack(fill="both", expand=True)
  root.mainloop()
  ```

**Python Tkinter Label**
- **Purpose**: Displays text or images on the screen.
- **Example**:
  ```python
  from tkinter import Tk, Label

  root = Tk()
  label = Label(root, text="Hello, Tkinter!", font=("Arial", 16))
  label.pack()
  root.mainloop()
  ```

**Python Tkinter Listbox**
- **Purpose**: Displays a list of items from which the user can select one or more.
- **Example**:
  ```python
  from tkinter import Tk, Listbox

  root = Tk()
  listbox = Listbox(root)
  listbox.insert(1, "Option 1")
  listbox.insert(2, "Option 2")
  listbox.pack()
  root.mainloop()
  ```

**Python Tkinter Menu**
- **Purpose**: Creates a drop-down menu bar.
- **Example**:
  ```python
  from tkinter import Tk, Menu

  root = Tk()
  menu = Menu(root)
  root.config(menu=menu)
  submenu = Menu(menu)
  menu.add_cascade(label="File", menu=submenu)
  submenu.add_command(label="Exit", command=root.quit)
  root.mainloop()
  ```

**Python Tkinter RadioButton**
- **Purpose**: Creates a set of mutually exclusive options (only one can be selected).
- **Example**:
  ```python
  from tkinter import Tk, Radiobutton, IntVar

  root = Tk()
  var = IntVar()
  radiobutton1 = Radiobutton(root, text="Option 1", variable=var, value=1)
  radiobutton2 = Radiobutton(root, text="Option 2", variable=var, value=2)
  radiobutton1.pack()
  radiobutton2.pack()
  root.mainloop()
  ```

**Python Tkinter Scale**
- **Purpose**: Creates a slider that the user can drag to select a value.
- **Example**:
  ```python
  from tkinter import Tk, Scale, HORIZONTAL

  root = Tk()
  scale = Scale(root, from_=0, to=100, orient=HORIZONTAL)
  scale.pack()
  root.mainloop()
  ```

**Python Tkinter Scrollbar**
- **Purpose**: Adds scrolling capability to other widgets (e.g., Text, Listbox).
- **Example**:
  ```python
  from tkinter import Tk, Listbox, Scrollbar, RIGHT, Y, LEFT, BOTH

  root = Tk()
  scrollbar = Scrollbar(root)
  listbox = Listbox(root, yscrollcommand=scrollbar.set)
  scrollbar.config(command=listbox.yview)
  scrollbar.pack(side=RIGHT, fill=Y)
  listbox.pack(side=LEFT, fill=BOTH)
  root.mainloop()
  ```

**Python Tkinter MessageBox**
- **Purpose**: Displays a message box for showing information, warnings, or errors.
- **Example**:
  ```python
  from tkinter import Tk, messagebox

  root = Tk()
  messagebox.showinfo("Greetings", "Welcome to Tkinter!")
  root.mainloop()
  ```

---
&copy; Pranav Mehendale, Yashashri Computers, Kothrud, Pune 2024. All rights reserved.

---