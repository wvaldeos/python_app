from pdf2image import convert_from_path
import pytesseract
import os
import json
import re
from flask import jsonify

def filter_json_by_length(data):
    filtered_data = []
    for item in data:
        stripped_item = item.replace(" ", "")  # Elimina todos los espacios
        if len(stripped_item) >= 40:
            filtered_data.append(item)  # Solo incluye elementos con al menos 40 caracteres
    return filtered_data

def filter_json_by_keywords(data, keywords=["Tipo", "Precio", "Cant.", "Descuento", "Monto", "Neto"]):
    filtered_data = [item for item in data if not all(keyword in item for keyword in keywords)]
    return filtered_data


def extract_data(text):
    result = {
        'Repuestos': [],
        'Mano de obra': [],
    }
    
    # Extracción de datos de repuestos
    if text is not None:
        text = 'Nº de catálogo '+ re.search(r'catálogo(.*?)Total piezas', text, re.DOTALL).group(1)

        repuestos_lines = text.strip().split('\n')

        for line in repuestos_lines:
            parts = re.split(r'\s{2,}', line)  # Dividir por dos o más espacios en blanco
            if len(parts) >= 6:
                repuesto = {
                    "Catalogo": parts[0],
                    "Descripcion": parts[1],
                    "Tipo": parts[2],
                    "Precio": parts[3],
                    "Cantidad": parts[4],
                    "Descuento": parts[5],
                    "Monto_Neto": parts[6] if len(parts) > 6 else ""
                }
                result['Repuestos'].append(repuesto)

    # Ahora solo estamos devolviendo 'Repuestos', así que comprobamos si se encontraron algunos.
    if not result['Repuestos']:
        text = text.split('\n')
        text = filter_json_by_length(text)
        text = filter_json_by_keywords(text)
        return jsonify({'message': 'No data found', 'text': text}), 404
    else:
        return jsonify(result), 200