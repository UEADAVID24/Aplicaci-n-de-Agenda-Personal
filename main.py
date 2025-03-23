import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar  # Asegúrate de tener instalado 'tkcalendar'
# Función para agregar un evento
def agregar_evento():
    fecha = calendar.get_date()  # Obtener la fecha seleccionada en el calendario
    hora = entry_hora.get()  # Obtener la hora desde el campo de entrada
    descripcion = entry_descripcion.get()  # Obtener la descripción desde el campo de entrada

    # Verificar que los campos no estén vacíos
    if not hora or not descripcion:
        messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
        return

    # Insertar el evento en el Treeview
    eventos_tree.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar los campos después de agregar el evento
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)


# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccionado = eventos_tree.selection()  # Obtener el evento seleccionado
    if not seleccionado:
        messagebox.showwarning("Sin selección", "Seleccione un evento para eliminar.")
        return

    # Confirmar eliminación
    confirmar = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar este evento?")
    if confirmar:
        eventos_tree.delete(seleccionado)


# Función para salir de la aplicación
def salir():
    confirmar = messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?")
    if confirmar:
        ventana.quit()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")  # Tamaño de la ventana

# Crear un Frame para la lista de eventos
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=20)

# Crear TreeView para mostrar los eventos
eventos_tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
eventos_tree.heading("Fecha", text="Fecha")
eventos_tree.heading("Hora", text="Hora")
eventos_tree.heading("Descripción", text="Descripción")
eventos_tree.pack()

# Crear un Frame para los campos de entrada de eventos
frame_agregar = tk.Frame(ventana)
frame_agregar.pack(pady=10)

# Etiquetas y campos de entrada para la fecha, hora y descripción
label_fecha = tk.Label(frame_agregar, text="Fecha:")
label_fecha.grid(row=0, column=0, padx=10, pady=5)

calendar = Calendar(frame_agregar)
calendar.grid(row=0, column=1, padx=10, pady=5)

label_hora = tk.Label(frame_agregar, text="Hora:")
label_hora.grid(row=1, column=0, padx=10, pady=5)

entry_hora = tk.Entry(frame_agregar)
entry_hora.grid(row=1, column=1, padx=10, pady=5)

label_descripcion = tk.Label(frame_agregar, text="Descripción:")
label_descripcion.grid(row=2, column=0, padx=10, pady=5)

entry_descripcion = tk.Entry(frame_agregar)
entry_descripcion.grid(row=2, column=1, padx=10, pady=5)

# Botones de acción
boton_agregar = tk.Button(ventana, text="Agregar Evento", command=agregar_evento)
boton_agregar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()

