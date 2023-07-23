import os
from pathlib import Path

def listar_directorio(ruta, indentacion=0, carpetas_a_ignorar=[], archivo_salida=None):
    for item in ruta.iterdir():
        if item.name not in carpetas_a_ignorar:
            if item.is_file():
                archivo_salida.write(' ' * indentacion + '├── ' + item.name + '\n')
            elif item.is_dir():
                archivo_salida.write(' ' * indentacion + item.name + '\n')
                listar_directorio(item, indentacion + 4, carpetas_a_ignorar, archivo_salida)
                archivo_salida.write(' ' * indentacion + '└── ' + '\n')

ruta_del_directorio = Path('../python_app/') 
carpetas_a_ignorar = ['../python_app/venv/','../python_app/app/__pycache__']

with open('output_schemma.txt', 'w') as f:
    listar_directorio(ruta_del_directorio, 0, carpetas_a_ignorar, f)
