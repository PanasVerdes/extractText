import pdfplumber  # Importa la biblioteca pdfplumber

def encontrar_justificacion_en_documento(pdf_path):
    justificaciones = []  # Lista para almacenar las justificaciones encontradas
    with pdfplumber.open(pdf_path) as pdf:  # Abre el archivo PDF
        for i, page in enumerate(pdf.pages, 1):  # Itera sobre todas las páginas del PDF
            if i > 5:  # Ignora las primeras 5 páginas
                text = page.extract_text()  # Extrae el texto de la página
                parrafos = text.split('\n\n')  # Divide el texto en párrafos
                for parrafo in parrafos:  # Itera sobre cada párrafo
                    if "Justificación" in parrafo:  # Verifica si el párrafo contiene "Justificación"
                        justificaciones.append(parrafo.strip())  # Agrega la justificación a la lista
    return justificaciones  # Devuelve la lista de justificaciones

# Ruta del archivo PDF
pdf_path = "C:/Users/ROTSEN199/OneDrive - SABES/Documents/UNI SABES/Proyectos IA/Proyecto SER/Doc_Alumnos/Proyecto de investigación_TESIS_Jonathan Orduña_opción a liberar.pdf"

# Encuentra las justificaciones en el documento
justificaciones = encontrar_justificacion_en_documento(pdf_path)

if justificaciones:  # Si se encontraron justificaciones
    print("Las justificaciones encontradas son:")
    for i, justificacion in enumerate(justificaciones, 6):  # Enumera a partir de la página 6
        print(f"Justificación {i}: {justificacion}")  # Imprime el número de justificación y su contenido
else:  # Si no se encontraron justificaciones
    print("No se encontraron justificaciones en las páginas después de la página 5 del PDF.")  # Imprime un mensaje indicando que no se encontraron justificaciones