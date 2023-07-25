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
    # Extracción de datos de repuestos
    if text is not None:
        text = 'Nº de catálogo '+ re.search(r'catálogo(.*?)Total piezas', text, re.DOTALL).group(1)
        text = text.split('\n')
        text = filter_json_by_length(text)
        text = filter_json_by_keywords(text)
        return jsonify({ 'text': text}), 404
    else:
        return jsonify({'mensaje':'Sin datos'}), 200
