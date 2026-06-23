{"nombre":"Carlos Pérez","edad":22,"carrera":"Diseño Gráfico"}

import json
# ----- Parte 1: Crear el diccionario -----
estudiante = {
"nombre": "María García",
"edad": 20,
"carrera": "Ingeniería de Sistemas",
"activo": True,
"materias": ["Python", "Bases de Datos", "Redes"],
"promedio": 4.5,
"beca": None }
# ----- Parte 2: Python → JSON (formateado) -----
estudiante_json = json.dumps(estudiante, indent=4, sort_keys=True)
print("=== Estudiante en formato JSON ===")
print(estudiante_json)


texto_json = '{"nombre":"Carlos Pérez","edad":22,"carrera":"Diseño Gráfico"}'
otro_estudiante = json.loads(texto_json)
print("\n=== Conversión JSON → Python ===")
print("Nombre del estudiante:", otro_estudiante["nombre"])