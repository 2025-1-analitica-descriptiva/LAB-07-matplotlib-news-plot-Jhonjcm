"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


import pandas as pd
import matplotlib.pyplot as plt
import os


def pregunta_01():
    """
    Lee los datos de un archivo CSV con los medios de publicidad y genera
    una gráfica de barras que se guarda como 'files/plots/news.png'.
    """
    # Crear carpeta si no existe
    os.makedirs("files/plots", exist_ok=True)

    # Leer archivo
    df = pd.read_csv("files/input/news.csv")  # Asegúrate de que este archivo exista con las columnas correctas

    # Sumar por columnas (asumiendo que hay varias filas con gastos por medio)
    totals = df.sum()

    # Crear gráfica
    plt.figure(figsize=(8, 6))
    totals.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Publicidad por Medio")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar gráfico
    plt.savefig("files/plots/news.png")
    plt.close()

    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
