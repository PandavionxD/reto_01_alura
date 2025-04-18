import pandas as pd
import matplotlib.pyplot as plt

# ? Levantar el entorno virtual
# python -m venv .env / source ./env/bin/activate
# ? Crear archivo de requerimientos
# pip freeze > "requirements"
# ? Instalar las librerias en requirements.txt
# pip install -r requirements.txt

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

# ! diagrama de Matplotlib
# !Crear lista con los ingresos y las tiendas
ingresos = [ingreso_tienda, ingreso_tienda2, ingreso_tienda3, ingreso_tienda4]
tiendas = ['Tienda-1', 'Tienda-2', 'Tienda-3', 'Tienda-4']
colors = ["blue","red","orange","green"]
# !Crear el gráfico de barras
plt.figure(figsize=(10,6))
plt.bar(tiendas, ingresos, color=colors)
# !Títulos y etiquetas
plt.title('Ingresos por Tiendas', fontsize=14)
plt.xlabel('Tiendas', fontsize=12)
plt.ylabel('Ingreso Total (S/)', fontsize=12)
# !Mostrar el gráfico
plt.show()


# ? En este debes calcular la cantidad de productos vendidos por categoría en cada tienda. La idea es agrupar los datos por categoría y contar el número de ventas de cada tipo, mostrando las categorías más populares de cada tienda.
print("Productos vendidos por categoría en tienda 1:")
print(tienda["Categoría del Producto"].value_counts())
categoria_tienda1 = tienda["Categoría del Producto"].value_counts()

print("\nProductos vendidos por categoría en tienda 2:")
print(tienda2["Categoría del Producto"].value_counts())
categoria_tienda2 = tienda2["Categoría del Producto"].value_counts()

print("\nProductos vendidos por categoría en tienda 3:")
print(tienda3["Categoría del Producto"].value_counts())
categoria_tienda3 = tienda3["Categoría del Producto"].value_counts()

print("\nProductos vendidos por categoría en tienda 4:")
print(tienda4["Categoría del Producto"].value_counts())
categoria_tienda4 = tienda4["Categoría del Producto"].value_counts()

# ! Division en diagram circular
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes[0, 0].pie(categoria_tienda1, labels=categoria_tienda1.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
axes[0, 0].set_title('Productos por Categoría en Tienda 1')
# ! Graficar para tienda 2
axes[0, 1].pie(categoria_tienda2, labels=categoria_tienda2.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
axes[0, 1].set_title('Productos por Categoría en Tienda 2')
# ! Graficar para tienda 3
axes[1, 0].pie(categoria_tienda3, labels=categoria_tienda3.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
axes[1, 0].set_title('Productos por Categoría en Tienda 3')
# ! Graficar para tienda 4
axes[1, 1].pie(categoria_tienda4, labels=categoria_tienda4.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
axes[1, 1].set_title('Productos por Categoría en Tienda 4')
# ! Ajustar el espaciado entre gráficos
plt.tight_layout()
# Mostrar el gráfico
plt.show()

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

# ! Crear gráfico lineal
tiendas = ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']
calificaciones = [calificacion_promedio_tienda1, calificacion_promedio_tienda2, calificacion_promedio_tienda3, calificacion_promedio_tienda4]
plt.figure(figsize=(10, 6))
plt.plot(tiendas, calificaciones, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)

# ! Añadir títulos y etiquetas
plt.title('Calificaciones Promedio de Clientes por Tienda', fontsize=16)
plt.xlabel('Tienda', fontsize=14)
plt.ylabel('Calificación Promedio', fontsize=14)
plt.grid(True)

# ! Mostrar el gráfico
plt.show()

# ? En este paso, debes identificar qué productos fueron los más vendidos y los menos vendidos en cada tienda. Visualiza los resultados para que quede claro qué productos destacaron en ventas en cada tienda.
print(f"\n{"="*30} Productos mas vendidos en las tiendas ",end="="*30 + "\n")
producto_tienda1 = tienda["Producto"].value_counts()
producto_tienda2 = tienda2["Producto"].value_counts()
producto_tienda3 = tienda3["Producto"].value_counts()
producto_tienda4 = tienda4["Producto"].value_counts()

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
print(f"\nProducto mas vendido es tienda1 es {producto_tienda1.idxmax()} - {producto_tienda1.max()} y los productos menos vendidos son: {producto_tienda1.idxmin()} - {producto_tienda1.min()}")
print(f"Producto mas vendido es tienda2 es {producto_tienda2.idxmax()} - {producto_tienda2.max()} y los productos menos vendidos son: {producto_tienda2.idxmin()} - {producto_tienda2.min()}")
print(f"Producto mas vendido es tienda3 es {producto_tienda3.idxmax()} - {producto_tienda3.max()} y los productos menos vendidos son: {producto_tienda3.idxmin()} - {producto_tienda3.min()}")
print(f"Producto mas vendido es tienda4 es {producto_tienda4.idxmax()} - {producto_tienda4.max()} y los productos menos vendidos son: {producto_tienda4.idxmin()} - {producto_tienda4.min()}")

# ! Graficos
# Información del producto más y menos vendido para cada tienda
productos_tienda1 = [producto_tienda1.max(), producto_tienda1.min()]
productos_tienda2 = [producto_tienda2.max(), producto_tienda2.min()]
productos_tienda3 = [producto_tienda3.max(), producto_tienda3.min()]
productos_tienda4 = [producto_tienda4.max(), producto_tienda4.min()]

productos_tienda1_labels = [f"Más vendido: {producto_tienda1.idxmax()}", f"Menos vendido: {producto_tienda1.idxmin()}"]
productos_tienda2_labels = [f"Más vendido: {producto_tienda2.idxmax()}", f"Menos vendido: {producto_tienda2.idxmin()}"]
productos_tienda3_labels = [f"Más vendido: {producto_tienda3.idxmax()}", f"Menos vendido: {producto_tienda3.idxmin()}"]
productos_tienda4_labels = [f"Más vendido: {producto_tienda4.idxmax()}", f"Menos vendido: {producto_tienda4.idxmin()}"]

# Graficar los resultados en gráficos de pastel
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Tienda 1
axes[0, 0].pie(productos_tienda1, labels=productos_tienda1_labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
axes[0, 0].set_title(f'Productos más y menos vendidos en Tienda 1')

# Tienda 2
axes[0, 1].pie(productos_tienda2, labels=productos_tienda2_labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
axes[0, 1].set_title(f'Productos más y menos vendidos en Tienda 2')

# Tienda 3
axes[1, 0].pie(productos_tienda3, labels=productos_tienda3_labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
axes[1, 0].set_title(f'Productos más y menos vendidos en Tienda 3')

# Tienda 4
axes[1, 1].pie(productos_tienda4, labels=productos_tienda4_labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
axes[1, 1].set_title(f'Productos más y menos vendidos en Tienda 4')

# Ajustar el espaciado entre gráficos
plt.tight_layout()

# Mostrar el gráfico
plt.show()


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

# ! Graficos
# Crear un gráfico de barras
tiendas = ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']
costos_envio = [costo_promedio_envio, costo_promedio_envio2, costo_promedio_envio3, costo_promedio_envio4]

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.bar(tiendas, costos_envio, color=['blue', 'green', 'red', 'orange'])

# Añadir título y etiquetas a los ejes
plt.title('Costo Promedio de Envío por Tiendas', fontsize=16)
plt.xlabel('Tiendas', fontsize=14)
plt.ylabel('Costo Promedio de Envío', fontsize=14)

# Mostrar el gráfico
plt.show()
