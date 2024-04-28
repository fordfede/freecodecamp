import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Paso 1: Leer datos del archivo
    data = pd.read_csv('epa-sea-level.csv')

    # Paso 2: Crear diagrama de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], alpha=0.7)

    # Paso 3: Crear primera línea de mejor ajuste
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    future_years = range(1880, 2051)
    plt.plot(future_years, slope * future_years + intercept, 'r', label='Línea de mejor ajuste')

    # Paso 4: Crear segunda línea de mejor ajuste
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    future_years_recent = range(2000, 2051)
    plt.plot(future_years_recent, slope_recent * future_years_recent + intercept_recent, 'g', label='Línea de mejor ajuste desde el año 2000')

    # Paso 5: Agregar etiquetas y título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Paso 6: Guardar el gráfico y devolver datos para pruebas
    plt.savefig('sea_level_plot.png')
    return plt.gca()

