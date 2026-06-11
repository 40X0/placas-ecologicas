#!/usr/bin/env python3
"""
Ejecuta este script UNA SOLA VEZ después de descargar los archivos.
Reemplaza BASE_URL_PLACEHOLDER con tu URL real de GitHub Pages.

Uso:
  python3 setup.py tuusuario/placas
  python3 setup.py tuusuario/placas  (si tu repo se llama 'placas')
  python3 setup.py tuusuario         (si usas usuario.github.io)
"""
import sys, os, re

if len(sys.argv) < 2:
    print("Uso: python3 setup.py <usuario>/<repositorio>")
    print("Ejemplo: python3 setup.py juanperez/placas-ecologicas")
    sys.exit(1)

ruta = sys.argv[1].strip('/')
base_url = f"https://{ruta.split('/')[0]}.github.io/{'/'.join(ruta.split('/')[1:])}" if '/' in ruta else f"https://{ruta}.github.io"

# Leer y reemplazar en subir.html
path = os.path.join(os.path.dirname(__file__), 'subir.html')
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('BASE_URL_PLACEHOLDER', base_url)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Listo. URL configurada: {base_url}")
print(f"   Los alumnos entrarán en: {base_url}/subir.html")
print(f"\nAhora sube TODOS los archivos de esta carpeta a tu repositorio GitHub.")
