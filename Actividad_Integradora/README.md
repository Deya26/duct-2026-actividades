# Analizador de frecuencias – Actividad Integradora

Script en Python que lee el archivo `texto_integradora.txt`, cuenta cuántas veces aparece cada palabra (sin distinguir mayúsculas de minúsculas) y genera un gráfico de barras con las 10 palabras más frecuentes, que se guarda como `grafico_frecuencias.png`. Si el archivo de texto no existe, el script muestra un mensaje de error en lugar de interrumpirse.

## Requisitos
- Python 3
- matplotlib y pytest: `pip install matplotlib pytest`

## Cómo ejecutarlo
Desde la carpeta `Actividad_Integradora`:
- Generar el gráfico: `python analizador.py`
- Correr las pruebas: `pytest -v`