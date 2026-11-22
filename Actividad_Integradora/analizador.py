# analizador.py
import matplotlib.pyplot as plt


def leer_archivo(ruta):
    """Lee un archivo de texto. Si no existe, avisa y devuelve None."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta}'.")
        return None


def contar_frecuencias(texto):
    """Cuenta la frecuencia de cada palabra en un texto."""
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias


def graficar_top(frecuencias, top_n=10, salida="grafico_frecuencias.png"):
    """Genera y guarda un gráfico de barras con las top_n palabras más frecuentes."""
    top = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]
    palabras = [palabra for palabra, valor in top]
    valores = [valor for palabra, valor in top]

    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title(f"Top {top_n} palabras más frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(salida, dpi=150)
    plt.show()


def main():
    texto = leer_archivo("texto_integradora.txt")
    if texto is None:
        return
    frecuencias = contar_frecuencias(texto)
    graficar_top(frecuencias)


if __name__ == "__main__":
    main()