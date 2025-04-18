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
print(f"\n{"="*30} Ingresos en las tiendas ",end="="*30 + "\n")
print(f"Ingreso de tienda1 es -> {ingreso_tienda}")
print(f"Ingreso de tienda2 es -> {ingreso_tienda2}")
print(f"Ingreso de tienda3 es -> {ingreso_tienda3}")
print(f"Ingreso de tienda4 es -> {ingreso_tienda4}")

# ? En este debes calcular la cantidad de productos vendidos por categoría en cada tienda. La idea es agrupar los datos por categoría y contar el número de ventas de cada tipo, mostrando las categorías más populares de cada tienda.
print("Productos vendidos por categoría en tienda 1:")
print(tienda["Categoría del Producto"].value_counts())

print("\nProductos vendidos por categoría en tienda 2:")
print(tienda2["Categoría del Producto"].value_counts())

print("\nProductos vendidos por categoría en tienda 3:")
print(tienda3["Categoría del Producto"].value_counts())

print("\nProductos vendidos por categoría en tienda 4:")
print(tienda4["Categoría del Producto"].value_counts())


# ? En este paso, debes calcular las calificaciones promedio de los clientes para cada tienda. El objetivo es conocer la satisfacción del cliente con los productos vendidos.
calificacion_promedio_tienda1 = tienda["Calificación"].mean()
calificacion_promedio_tienda2 = tienda2["Calificación"].mean()
calificacion_promedio_tienda3 = tienda3["Calificación"].mean()
calificacion_promedio_tienda4 = tienda4["Calificación"].mean()

# ? Mostrar resultados
print(f"\n{"="*30} Calificaciones promedio en las tiendas ",end="="*30 + "\n")
print(f"\nCalificación promedio de tienda 1: {round(calificacion_promedio_tienda1,2)}")
print(f"Calificación promedio de tienda 2: {round(calificacion_promedio_tienda2,2)}")
print(f"Calificación promedio de tienda 3: {round(calificacion_promedio_tienda3,2)}")
print(f"Calificación promedio de tienda 4: {round(calificacion_promedio_tienda4,2)}")

# ? En este paso, debes identificar qué productos fueron los más vendidos y los menos vendidos en cada tienda. Visualiza los resultados para que quede claro qué productos destacaron en ventas en cada tienda.
print(f"\n{"="*30} Productos mas vendidos en las tiendas ",end="="*30 + "\n")
producto_tienda1 = tienda["Producto"].value_counts()
producto_tienda2 = tienda2["Producto"].value_counts()
producto_tienda3 = tienda3["Producto"].value_counts()
producto_tienda4 = tienda4["Producto"].value_counts()

print(f"\nProducto mas vendido es tienda1 es {producto_tienda1.idxmax()} - {producto_tienda1.max()} y los productos menos vendidos son: {producto_tienda1.idxmin()} - {producto_tienda1.min()}")
print(f"Producto mas vendido es tienda2 es {producto_tienda2.idxmax()} - {producto_tienda2.max()} y los productos menos vendidos son: {producto_tienda2.idxmin()} - {producto_tienda2.min()}")
print(f"Producto mas vendido es tienda3 es {producto_tienda3.idxmax()} - {producto_tienda3.max()} y los productos menos vendidos son: {producto_tienda3.idxmin()} - {producto_tienda3.min()}")
print(f"Producto mas vendido es tienda4 es {producto_tienda4.idxmax()} - {producto_tienda4.max()} y los productos menos vendidos son: {producto_tienda4.idxmin()} - {producto_tienda4.min()}")

# ? En este paso, debes calcular el costo de envío promedio para cada tienda. El objetivo es comprender cuánto se gasta, en promedio, en el envío de cada tienda.
costo_promedio_envio = tienda["Costo de envío"].mean()
costo_promedio_envio2 = tienda2["Costo de envío"].mean()
costo_promedio_envio3 = tienda3["Costo de envío"].mean()
costo_promedio_envio4 = tienda4["Costo de envío"].mean()
print(f"\n{"="*30} El costo envio de las tiendas ",end="="*30 + "\n")
print(f"\nEl costo envio de tienda1 es -> {round(costo_promedio_envio,2)}")
print(f"El costo envio de tienda2 es -> {round(costo_promedio_envio2,2)}")
print(f"El costo envio de tienda3 es -> {round(costo_promedio_envio3,2)}")
print(f"El costo envio de tienda4 es -> {round(costo_promedio_envio4,2)}")
