import fitz  # PyMuPDF
import unicodedata
import csv

# Función para eliminar acentos
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

# Abre el archivo PDF
ruta_del_archivo = "Doc_Alumnos/Tesis_Luis_Armando_Gutierrez_Jaime_U1903058M0065.pdf"  # Reemplaza esto con la ruta de tu archivo PDF
pdf = fitz.open(ruta_del_archivo)

# Imprime el número total de páginas en el archivo PDF
print("Número total de páginas:", len(pdf))

# Inicializa un diccionario para almacenar el texto de cada página
pages_text = {}

# Define la palabra clave de búsqueda
keyword = "justificacion"

# Convierte la palabra clave a minúsculas y elimina los acentos
keyword = remove_accents(keyword.lower())

# Itera sobre todas las páginas
for i in range(len(pdf)):
    # Carga la página
    page = pdf.load_page(i)
    
    # Extrae el texto de la página
    text = page.get_text()
    
    # Convierte el texto a minúsculas y elimina los acentos
    text = remove_accents(text.lower())
    
    # Si la palabra clave está en el texto, almacena el texto de la página en el diccionario
    if keyword in text:
        pages_text[f"page_{i+1}"] = text

# Cierra el archivo PDF
pdf.close()

# Guarda el texto extraído en un archivo .csv
with open("pruebasdocs/extracted_text.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    for page, text in pages_text.items():
        writer.writerow([page, text])

# Guarda el texto extraído en un archivo .txt
with open("pruebasdocs/extracted_text.txt", "w") as txt_file:
    for page, text in pages_text.items():
        txt_file.write(f"{page}:\n{text}\n{'='*50}\n")

# Imprime un mensaje de éxito
print("El texto extraído se guardó correctamente en los archivos extracted_text.csv y extracted_text.txt.")
