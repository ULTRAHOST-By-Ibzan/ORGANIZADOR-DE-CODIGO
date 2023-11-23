import jsbeautifier
import cssbeautifier
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog, ttk
from ttkthemes import ThemedStyle
import os
from PIL import Image, ImageTk

def beautify_html(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    return soup.prettify()

def beautify_css(css_code):
    options = cssbeautifier.default_options()
    options.indent = '    '  # Espacios
    options.openbrace = 'end-of-line'  # Colocar el corchete de apertura al final de la línea
    return cssbeautifier.beautify(css_code, options)

def beautify_js(js_code):
    return jsbeautifier.beautify(js_code)

def organize_and_save(content, file_type):
    if file_type == "HTML":
        organized_content = beautify_html(content)
    elif file_type == "CSS":
        organized_content = beautify_css(content)
    elif file_type == "JS":
        organized_content = beautify_js(content)
    else:
        return

    return organized_content

def save_file(content):
    # Definir las opciones de tipo de archivo
    file_types = [("Text files", "*.txt"), ("CSS files", "*.css"), ("HTML files", "*.html"), ("JavaScript files", "*.js")]

    # Pedir al usuario dónde guardar el archivo
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=file_types)

    # Guardar el contenido organizado en el archivo
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def organize_and_download():
    content, file_path = load_file()

    if content is not None and file_path is not None:
        # Obtener el tipo de archivo (HTML, CSS o JS) a partir de la extensión
        file_type = file_path.split('.')[-1].upper()

        # Organizar el archivo
        organized_content = organize_and_save(content, file_type)

        # Mostrar el contenido organizado en la ventana inferior
        result_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
        result_text.insert(tk.END, organized_content)

def load_file():
    selected_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.html;*.css;*.js;*.txt")])

    if selected_file_path:
        with open(selected_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content, selected_file_path

    return None, None

# Crear la interfaz
window = tk.Tk()
window.title("ULTRAHOST - Organizador de Codigo - By IBZAN")

# Establecer el tamaño de la ventana
window.geometry("500x700")

# Ruta del ícono
icon_path = "C:\\Users\\zero\\Documents\\codigoorganizador\\logo.ico"

# Verificar si la ruta del ícono existe
if os.path.exists(icon_path):
    # Cargar el ícono
    icon = ImageTk.PhotoImage(Image.open(icon_path))

    # Establecer el ícono en la ventana
    window.iconphoto(True, icon)

# Estilo
style = ThemedStyle(window)
style.set_theme("radiance")

# Contenedor superior
top_frame = ttk.Frame(window)
top_frame.pack(side="top", fill="both", expand=True)

# Contenedor inferior para el resultado
bottom_frame = ttk.Frame(window, height=200)
bottom_frame.pack(side="bottom", fill="both", expand=True)

# Botón para organizar y descargar el código
organize_button = ttk.Button(top_frame, text="SELECCIONAR ARCHIVO", command=organize_and_download)
organize_button.pack(pady=10)

# Línea divisoria
separator = ttk.Separator(top_frame, orient="horizontal")
separator.pack(fill="x", pady=10)

# Texto publicitario
text_label = tk.Label(top_frame, text="Diseño de aplicaciones - páginas y aplicativos web - servicio de hosting y dominio.", justify="center", wraplength=350)
text_label.pack(pady=10)

# Botones para WhatsApp y Web
whatsapp_button = ttk.Button(top_frame, text="WhatsApp", command=lambda: open_url("https://wa.me/447418353168"))
whatsapp_button.pack(side="left", padx=10)

web_button = ttk.Button(top_frame, text="WEB", command=lambda: open_url("https://ultrahost.uk"))
web_button.pack(side="right", padx=10)

# Función para abrir URL en el navegador
def open_url(url):
    import webbrowser
    webbrowser.open(url)

# Texto en la ventana inferior
result_text = tk.Text(bottom_frame, wrap="none", padx=10, pady=10)
result_text.pack(expand=True, fill="both")

# Botón para guardar el archivo
save_button = ttk.Button(bottom_frame, text="Guardar", command=lambda: save_file(result_text.get(1.0, tk.END)))
save_button.pack(pady=10)

# Iniciar el bucle
window.mainloop()
