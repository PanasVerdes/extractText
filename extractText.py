import fitz  # PyMuPDF
import csv
import os

class TextExtractor:
    def __init__(self, ruta_del_archivo):
        self.ruta_del_archivo = ruta_del_archivo

    def extract_text(self):
        # Abre el archivo PDF
        pdf = fitz.open(self.ruta_del_archivo)

        # Inicializa un diccionario para almacenar el texto de cada página
        pages_text = {}

        # Itera sobre todas las páginas
        for i in range(len(pdf)):
            # Carga la página
            page = pdf.load_page(i)
            
            # Almacena el texto de la página en el diccionario
            pages_text[f"page_{i+1}"] = page.get_text()

        # Cierra el archivo PDF
        pdf.close()

        return pages_text

    def save_to_csv(self, pages_text):
        # Guarda el texto extraído en un archivo .csv
        with open("static/extracted_text.csv", "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            for page, text in pages_text.items():
                writer.writerow([page, text])
