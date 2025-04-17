import pandas as pd

# ? Levantar el entorno virtual
# python -m venv .env / source ./env/bin/activate

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

# ? imprimir las primeras 10 lineas del libro
print(tienda.head())
# print(tienda2.head())
# print(tienda3.head())
# print(tienda4.head())
     
# ? En este primer análisis, debes calcular el ingreso total de cada tienda. Sumando los valores de la columna Precio de cada conjunto de datos de la tienda para estimar los ingresos.
ingreso_tienda = sum(list(tienda["Precio"]))
ingreso_tienda2 = sum(list(tienda2["Precio"]))
ingreso_tienda3 = sum(list(tienda3["Precio"]))
ingreso_tienda4 = sum(list(tienda4["Precio"]))

# ? Resultados
print(f"Ingreso de tienda1 es -> {ingreso_tienda}")
print(f"Ingreso de tienda2 es -> {ingreso_tienda2}")
print(f"Ingreso de tienda3 es -> {ingreso_tienda3}")
print(f"Ingreso de tienda4 es -> {ingreso_tienda4}")
