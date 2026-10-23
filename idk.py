import tkinter as tk

# 1. Create the main window
ventana = tk.Tk()
ventana.title("Displaying Text and Code")
ventana.geometry("500x400")

# 2. Display standard text using a Label
label_titulo = tk.Label(
    ventana,
    text="This is standard text (Label):",
    font=("Arial", 12, "bold")
)
label_titulo.pack(pady=10) # pack() places the widget in the window

# 3. Display code using a Text widget
# Setting background, foreground, and font makes it look like a code editor
cuadro_codigo = tk.Text(
    ventana,
    height=10,
    width=55,
    font=("Courier New", 11),
    bg="#1e1e1e",      # Dark background
    fg="#d4d4d4",      # Light text color
    insertbackground="white" # Cursor color
)
cuadro_codigo.pack(pady=10)

# The code block you want to display
codigo_ejemplo = """def saludar(nombre):
    print(f"Hola, {nombre}!")

# Llamada a la función
saludar("Mundo")
"""

# Insert the code into the text widget (1.0 means line 1, character 0)
cuadro_codigo.insert("1.0", codigo_ejemplo)

# (Optional) Disable editing so the user can only read and copy the code
cuadro_codigo.config(state="disabled")

# 4. Start the application loop
ventana.mainloop()