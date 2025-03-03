import tkinter as tk
from tkinter import ttk
from Kutta import RungeKutta
from Newthon import NewtonRaphson
from Euler import EulerMejorado

class NumericalMethodsApp(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.root.title("Métodos Numéricos")
        self.root.geometry("1600x800")
        self.root.resizable(False, False)  # Deshabilitar cambio de tamaño
        
        # Crear Notebook (Pestañas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')
        
        # Crear pestañas
        self.kutta_tab = ttk.Frame(self.notebook)
        self.newton_tab = ttk.Frame(self.notebook)
        self.euler_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.newton_tab, text="Newton-Raphson")
        self.notebook.add(self.kutta_tab, text="Runge-Kutta")
        self.notebook.add(self.euler_tab, text="Euler Mejorado")
        
        self.create_newton_ui()
        self.create_euler_ui()
        self.create_kutta_ui()

        # Crear estilo antes de usarlo
        style = ttk.Style()
        style.configure('results.TFrame', background="#000000")  # Gris claro

    def clear_placeholder(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)

    def add_placeholder(self, event, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)

    def create_newton_ui(self):
        # Crear un PanedWindow para dividir el espacio
        paned_window = ttk.PanedWindow(self.newton_tab, orient="horizontal")
        
        # Crear los eaneles
        panel_1 = ttk.Frame(paned_window, relief="sunken", style="results.TFrame")
        panel_2 = ttk.Frame(paned_window, relief="sunken")
        
        # Añadir los paneles al PanedWindow
        paned_window.add(panel_1, weight=3)  # Panel 1 ocupa más espacio
        paned_window.add(panel_2, weight=1)  # Panel 2 ocupa menos espacio
        
        # Colocar el PanedWindow en la pestaña
        paned_window.pack(fill=tk.BOTH, expand=True)

        self.func_entry = ttk.Entry(panel_2)
        placeholder_text_func = "F(x): (x^2)"
        self.func_entry.insert(0, placeholder_text_func)
        self.func_entry.pack(padx=10, pady=5)
        self.func_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.func_entry, placeholder_text_func))
        self.func_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.func_entry, placeholder_text_func))

        self.punto_inicial_entry = ttk.Entry(panel_2)
        placeholder_text_punto_inicial = "Punto inicial"
        self.punto_inicial_entry.insert(0, placeholder_text_punto_inicial)
        self.punto_inicial_entry.pack(padx=10, pady=5)
        self.punto_inicial_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.punto_inicial_entry, placeholder_text_punto_inicial))
        self.punto_inicial_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.punto_inicial_entry, placeholder_text_punto_inicial))


        self.decimales_tol_entry = ttk.Entry(panel_2)
        placeholder_text_decimales_tol = "Tolerancia"
        self.decimales_tol_entry.insert(0, placeholder_text_decimales_tol)
        self.decimales_tol_entry.pack(padx=10, pady=5)
        self.decimales_tol_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.decimales_tol_entry, placeholder_text_decimales_tol))
        self.decimales_tol_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.decimales_tol_entry, placeholder_text_decimales_tol))

        # Crear el botón para calcular
        calculate_button = ttk.Button(panel_2, text="Calcular", command=self.calculate_newton)
        calculate_button.pack(padx=10, pady=10)

        # Crear el Treeview para mostrar los resultados
        self.treeview = ttk.Treeview(panel_1, columns=("Iteración", "x_n", "f(x_n)", "f'(x_n)", "x_n+1"), show="headings")
        self.treeview.heading("Iteración", text="Iteración")
        self.treeview.heading("x_n", text="x_n")
        self.treeview.heading("f(x_n)", text="f(x_n)")
        self.treeview.heading("f'(x_n)", text="f'(x_n)")
        self.treeview.heading("x_n+1", text="x_n+1")
        
        self.treeview.pack(fill=tk.BOTH, expand=True)
        self.error_message = ttk.Label(panel_2, text="Usar X para variables.", foreground="red")
        self.error_message.pack(side=tk.BOTTOM, pady=10)

    def calculate_newton(self):
        # Obtener los valores de los inputs
        funcion = self.func_entry.get()
        punto_inicial = float(self.punto_inicial_entry.get())
        decimales_tol = None if self.decimales_tol_entry.get() == "None" else int(self.decimales_tol_entry.get())

        print('calculando con valores: ', funcion, punto_inicial, decimales_tol)
        # Realizar el cálculo de Newton-Raphson
        newton = NewtonRaphson()
        resultados = newton.resolver(funcion= funcion, punto_inicial= punto_inicial,decimales_tol = decimales_tol)

        # Limpiar los resultados anteriores
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Insertar los resultados en el Treeview
        for iteracion, x_val, f_x_n, f_prime_x_n, x_n1 in resultados:
            self.treeview.insert("", "end", values=(iteracion, f"{x_val:.6f}", f"{f_x_n:.6f}", f"{f_prime_x_n:.6f}", f"{x_n1:.6f}"))

        # Limpiar los resultados anteriores
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Insertar los resultados en el Treeview
        for iteracion, x_val, f_x_n, f_prime_x_n, x_n1 in resultados:
            self.treeview.insert("", "end", values=(iteracion, f"{x_val:.6f}", f"{f_x_n:.6f}", f"{f_prime_x_n:.6f}", f"{x_n1:.6f}"))

    def create_euler_ui(self):
        paned_window = ttk.PanedWindow(self.euler_tab, orient="horizontal")
        
        # Crear los paneles
        panel_1 = ttk.Frame(paned_window, relief="sunken", style="results.TFrame")
        panel_2 = ttk.Frame(paned_window, relief="sunken")
        
        # Añadir los paneles al PanedWindow
        paned_window.add(panel_1, weight=3)  # Panel 1 ocupa más espacio
        paned_window.add(panel_2, weight=1)  # Panel 2 ocupa menos espacio
        
        # Colocar el PanedWindow en la pestaña
        paned_window.pack(fill=tk.BOTH, expand=True)

        self.func_entry_euler = ttk.Entry(panel_2)
        placeholder_text_func_euler = "f(x,y): x^2+y"
        self.func_entry_euler.insert(0, placeholder_text_func_euler)
        self.func_entry_euler.pack(padx=10, pady=5)
        self.func_entry_euler.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.func_entry_euler, placeholder_text_func_euler))
        self.func_entry_euler.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.func_entry_euler, placeholder_text_func_euler))

        self.x_initial_euler_entry = ttk.Entry(panel_2)
        placeholder_text_x_initial_euler = "xO"
        self.x_initial_euler_entry.insert(0, placeholder_text_x_initial_euler)
        self.x_initial_euler_entry.pack(padx=10, pady=5)
        self.x_initial_euler_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.x_initial_euler_entry, placeholder_text_x_initial_euler))
        self.x_initial_euler_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.x_initial_euler_entry, placeholder_text_x_initial_euler))

        self.y_initial_euler_entry = ttk.Entry(panel_2)
        placeholder_text_y_initial_euler = "yO"
        self.y_initial_euler_entry.insert(0, placeholder_text_y_initial_euler)
        self.y_initial_euler_entry.pack(padx=10, pady=5)
        self.y_initial_euler_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.y_initial_euler_entry, placeholder_text_y_initial_euler))
        self.y_initial_euler_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.y_initial_euler_entry, placeholder_text_y_initial_euler))

        self.x_step_euler_entry = ttk.Entry(panel_2)
        placeholder_text_x_step_euler = "x"
        self.x_step_euler_entry.insert(0, placeholder_text_x_step_euler)
        self.x_step_euler_entry.pack(padx=10, pady=5)
        self.x_step_euler_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.x_step_euler_entry, placeholder_text_x_step_euler))
        self.x_step_euler_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.x_step_euler_entry, placeholder_text_x_step_euler))

        self.h_euler_entry = ttk.Entry(panel_2)
        placeholder_text_h_euler = "H"
        self.h_euler_entry.insert(0, placeholder_text_h_euler)
        self.h_euler_entry.pack(padx=10, pady=5)
        self.h_euler_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.h_euler_entry, placeholder_text_h_euler))
        self.h_euler_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.h_euler_entry, placeholder_text_h_euler))

        self.tolerance_euler_entry = ttk.Entry(panel_2)
        placeholder_text_tolerance_euler = "Tolerancia"
        self.tolerance_euler_entry.insert(0, placeholder_text_tolerance_euler)
        self.tolerance_euler_entry.pack(padx=10, pady=5)
        self.tolerance_euler_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.tolerance_euler_entry, placeholder_text_tolerance_euler))
        self.tolerance_euler_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.tolerance_euler_entry, placeholder_text_tolerance_euler))


        # Crear el botón para calcular
        calculate_button = ttk.Button(panel_2, text="Calcular", command=self.calculate_euler)
        calculate_button.pack(padx=10, pady=10)

        # Crear el Treeview para mostrar los resultados
        self.treeview_euler = ttk.Treeview(panel_1, columns=("Iteración", "X", "Y aprox", "Y real", "Err Absol"), show="headings")
        self.treeview_euler.heading("Iteración", text="Iteración")
        self.treeview_euler.heading("X", text="X")
        self.treeview_euler.heading("Y aprox", text="Y aprox")
        self.treeview_euler.heading("Y real", text="Y real")
        self.treeview_euler.heading("Err Absol", text="Err Absol")
        
        self.treeview_euler.pack(fill=tk.BOTH, expand=True)
    
        self.error_message = ttk.Label(panel_2, text="Usar X, Y para variables.", foreground="red")
        self.error_message.pack(side=tk.BOTTOM, pady=10)
    def calculate_euler(self):
        # Obtener los valores de los inputs
        funcion = self.func_entry_euler.get()  # Ajusta el nombre según tu variable
        xInitial = float(self.x_initial_euler_entry.get())
        yInitial = float(self.y_initial_euler_entry.get())
        xEuler = float(self.x_step_euler_entry.get())
        hEuler = float(self.h_euler_entry.get())
        tol = int(self.tolerance_euler_entry.get())

        # Realizar el cálculo de Euler Mejorado
        euler = EulerMejorado()
        resultados = euler.euler_mejorado(
            function=funcion, 
            x0=xInitial, 
            y0=yInitial, 
            x=xEuler, 
            h=hEuler,
            tol=tol
        )

        # Limpiar los resultados anteriores en el Treeview
        for row in self.treeview_euler.get_children():
            self.treeview_euler.delete(row)

        # Insertar los resultados en el Treeview
        for iteracion, x_val, y_aprox, y_real, error_abs in resultados:
            self.treeview_euler.insert("", "end", values=(
                iteracion, 
                f"{x_val:.6f}", 
                f"{y_aprox:.6f}", 
                f"{y_real:.6f}", 
                f"{error_abs:.6f}"
            ))

    def create_kutta_ui(self):
        # Crear un PanedWindow para dividir el espacio
        paned_window = ttk.PanedWindow(self.kutta_tab, orient="horizontal")
        
        # Crear los paneles
        panel_1 = ttk.Frame(paned_window, relief="sunken", style="results.TFrame")
        panel_2 = ttk.Frame(paned_window, relief="sunken")
        
        # Añadir los paneles al PanedWindow
        paned_window.add(panel_1, weight=3)  # Panel 1 ocupa más espacio
        paned_window.add(panel_2, weight=1)  # Panel 2 ocupa menos espacio
        
        # Colocar el PanedWindow en la pestaña
        paned_window.pack(fill=tk.BOTH, expand=True)

        self.func_entry_kutta = ttk.Entry(panel_2)
        placeholder_text_func_kutta = "f(x,y): x^2+y"
        self.func_entry_kutta.insert(0, placeholder_text_func_kutta)
        self.func_entry_kutta.pack(padx=10, pady=5)
        self.func_entry_kutta.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.func_entry_kutta, placeholder_text_func_kutta))
        self.func_entry_kutta.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.func_entry_kutta, placeholder_text_func_kutta))

        self.x_initial_kutta_entry = ttk.Entry(panel_2)
        placeholder_text_x_initial_kutta = "xO"
        self.x_initial_kutta_entry.insert(0, placeholder_text_x_initial_kutta)
        self.x_initial_kutta_entry.pack(padx=10, pady=5)
        self.x_initial_kutta_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.x_initial_kutta_entry, placeholder_text_x_initial_kutta))
        self.x_initial_kutta_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.x_initial_kutta_entry, placeholder_text_x_initial_kutta))

        self.y_initial_kutta_entry = ttk.Entry(panel_2)
        placeholder_text_y_initial_kutta = "yO"
        self.y_initial_kutta_entry.insert(0, placeholder_text_y_initial_kutta)
        self.y_initial_kutta_entry.pack(padx=10, pady=5)
        self.y_initial_kutta_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.y_initial_kutta_entry, placeholder_text_y_initial_kutta))
        self.y_initial_kutta_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.y_initial_kutta_entry, placeholder_text_y_initial_kutta))

        self.x_step_kutta_entry = ttk.Entry(panel_2)
        placeholder_text_x_step_kutta = "x"
        self.x_step_kutta_entry.insert(0, placeholder_text_x_step_kutta)
        self.x_step_kutta_entry.pack(padx=10, pady=5)
        self.x_step_kutta_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.x_step_kutta_entry, placeholder_text_x_step_kutta))
        self.x_step_kutta_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.x_step_kutta_entry, placeholder_text_x_step_kutta))

        self.h_kutta_entry = ttk.Entry(panel_2)
        placeholder_text_h_kutta = "H"
        self.h_kutta_entry.insert(0, placeholder_text_h_kutta)
        self.h_kutta_entry.pack(padx=10, pady=5)
        self.h_kutta_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.h_kutta_entry, placeholder_text_h_kutta))
        self.h_kutta_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.h_kutta_entry, placeholder_text_h_kutta))

        self.tolerance_kutta_entry = ttk.Entry(panel_2)
        placeholder_text_tolerance_kutta = "Tolerancia"
        self.tolerance_kutta_entry.insert(0, placeholder_text_tolerance_kutta)
        self.tolerance_kutta_entry.pack(padx=10, pady=5)
        self.tolerance_kutta_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, self.tolerance_kutta_entry, placeholder_text_tolerance_kutta))
        self.tolerance_kutta_entry.bind("<FocusOut>", lambda event: self.add_placeholder(event, self.tolerance_kutta_entry, placeholder_text_tolerance_kutta))


        # Crear el botón para calcular
        calculate_button = ttk.Button(panel_2, text="Calcular", command=self.calculate_kutta)
        calculate_button.pack(padx=10, pady=10)

        # Crear el Treeview para mostrar los resultados
        self.treeview_kutta = ttk.Treeview(panel_1, columns=("Iteración", "X", "Y aprox", "Y real", "Err Absol"), show="headings")
        self.treeview_kutta.heading("Iteración", text="Iteración")
        self.treeview_kutta.heading("X", text="X")
        self.treeview_kutta.heading("Y aprox", text="Y aprox")
        self.treeview_kutta.heading("Y real", text="Y real")
        self.treeview_kutta.heading("Err Absol", text="Err Absol")
        
        self.treeview_kutta.pack(fill=tk.BOTH, expand=True)

        self.error_message = ttk.Label(panel_2, text="Usar X, Y para variables.", foreground="red")
        self.error_message.pack(side=tk.BOTTOM, pady=10)

    def calculate_kutta(self):
        # Obtener los valores de los inputs
        funcion = self.func_entry_kutta.get()
        xInitial = float(self.x_initial_kutta_entry.get())
        yInitial = float(self.y_initial_kutta_entry.get())
        xKutta = float(self.x_step_kutta_entry.get())
        hKutta = float(self.h_kutta_entry.get())
        tol = int(self.tolerance_kutta_entry.get())

        # Realizar el cálculo de Runge-Kutta
        kutta = RungeKutta()
        resultados = kutta.rungeKutta(
            f=funcion, 
            x0=xInitial, 
            y0=yInitial, 
            x=xKutta, 
            h=hKutta,
            tol=tol
        )

        # Limpiar los resultados anteriores en el Treeview
        for row in self.treeview_kutta.get_children():
            self.treeview_kutta.delete(row)

        # Insertar los resultados en el Treeview
        for iteracion, x_val, y_aprox, y_real, error_abs in resultados:
            self.treeview_kutta.insert("", "end", values=(
                iteracion, 
                f"{x_val:.6f}", 
                f"{y_aprox:.6f}", 
                f"{y_real:.6f}", 
                f"{error_abs:.6f}"
            ))
app = tk.Tk()
NumericalMethodsApp(app)
app.mainloop()
