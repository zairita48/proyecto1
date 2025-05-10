from flask import Flask, request, render_template      #se importa flask
import re                         #libreria estandar para trabajar con expresiones regulares (regular expressions)
from datetime import datetime           #el modulo datetime maneja fechas y horas en python
import matplotlib.pyplot as plt            #plt es el alias que le hemos creado a matplotlib que es una biblioteca 
import io
import base64
import pandas as pd



app = Flask(__name__)            #se le esta dando el nombre

paciente= {}
@app.route("/")              #es la ruta raiz donde lo busca del directorio o acceso de la web
def home():                     #def es una funcion
    return "Holaa, Flask"        

 #Ejemplo de otra ruta con paso de valor 
"""@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()                                                #para visualizar el segundo se coloca en la linea de busqueda /hello/ y el nombre 
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    return f"Hola {name}! La fecha y hora actual es: {formatted_now}"

#otra ruta 
@app.route("/producto/<int:id>")
def mostrar_producto(id):
    return f"Mostrando producto con Id {id}"

#otra ruta
@app.route("/temperatura/<float:grados>")
def mostrar_temperatura(grados):
    return f"la temperatura es {grados} °C"

#otra ruta
@app.route("/sumar/<int:a>/<int:b>")
def sumar(a, b):
    resultado = a + b
    return f"La suma de {a} y {b} es {resultado}"     

#otra rutta
@app.route("/pagina1/") 
def pagina():                                       #esta ruta esta vinculada con el archivo/plantilla de index 
    return render_template("index.html")           

#otra ruta
@app.route("/Bienvenida/<nombre>")
def Bienvenida(nombre):
    return render_template("index.html", nombre=nombre)

#un ejercicio nuevo
@app.route("/servicios")
def servicios():
 lista_servicios = ["Consulta", "Odontología", "Laboratorio", "Urgencias"]
 return render_template("index.html", servicios=lista_servicios)

#ptro ejercicio nuevo
@app.route("/fecha")
def mostrar_fecha():
 ahora = datetime.now().strftime("%d/%m/%Y %H:%M")
 return render_template("index.html", ahora=ahora)

#ptro ejercicio nuevo
@app.route("/paciente")
def paciente():
    datos_paciente = {
    "nombre": "Carlos Gómez",
    "edad": 35,
    "servicio": "Consulta General",
    "fecha": "28/04/2025"
 }
    return render_template("index.html", paciente=datos_paciente)

#ptro ejercicio nuevo
@app.route("/pacientes")
def lista_pacientes():
    pacientes = [
    {"nombre": "Ana Ruiz", "edad": 30, "servicio": "Odontología"},
    {"nombre": "Luis Martínez", "edad": 45, "servicio": "Pediatría"},
    {"nombre": "Laura Gómez", "edad": 28, "servicio": "Laboratorio"}
    ]
    return render_template("index.html", pacientes=pacientes)"""

@app.route("/proyecto/")
def proy_():                                #esta ruta esta vinculada a index1.html
    return render_template("index1.html")

@app.route("/pagina2")
def pagina2():                                  #esta ruta esta vinculada a index.html
    return render_template("index2.html")

@app.route("/grafico1") 
def grafico():
# Datos para el grafico 
    x = [1, 2, 3, 4, 5]
    y = [10, 14, 16, 20, 25]
# Creacion del grafico                                              hacemos el llamado a plt
    plt.figure(figsize=(6, 4))                                    #ancho y alto
    plt.plot(x, y, marker='o', linestyle='-', color='pink')           #indicamos que tendra el eje X y el eje Y, tendra una marcacion con linea Y un color rosado
    plt.title('Crecimiento de Ventas')                             #tendra un titulo
    plt.xlabel('Mes')                                             #tendra una etiqueta para el eje X 
    plt.ylabel('Ventas')                                          #y otra etiqueta para el eje Y
    # Guardar graficos en un buffer
    buf = io.BytesIO()                                           #guarda el garfico en el buffer
    plt.savefig(buf, format='png')                               #darle un formato como png imagen 
    buf.seek(0)                                                  #ubica la imagen en 0
    # Codificar imagen en base64
    imagen_base64 = base64.b64encode(buf.getvalue()).decode('utf8')
    return render_template('index1.html', imagen=imagen_base64)                 #que muestre el grafico enn la pagina index1.html

#______________________________________________________________________________________________________

@app.route('/grafico_pie/')
def grafico_pie():
    etiquetas = ['Python', 'Java', 'C++', 'JavaScript']
    tamanios = [40, 25, 20, 15]

    plt.figure(figsize=(6, 6))
    plt.pie(tamanios, labels=etiquetas, autopct='%1.1f%%', startangle=90)
    plt.title('Preferencias de Lenguaje de Programacion')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    imagen = base64.b64encode(buf.getvalue()).decode('utf8')
    return render_template('index1.html', imagen=imagen)

#_______________________________________________________________________________________________________

@app.route('/grafico_ventas_productos/')
def grafico_ventas_productos():
    # cargar archivo CSV
    df = pd.read_csv('data/ventas_anuales.csv')

    # Arupar por producto y sumar ventas
    resumen = df.groupby('Nombre Producto')['Ventas Totales'].sum().sort_values(ascending=False)

    #crear grafico
    plt.figure(figsize=(6, 3.5))
    resumen.plot(kind='bar', color='orange')                                    #ancho y alto
    plt.title('Ventas Totales por Producto')                             #tendra un titulo
    plt.xlabel('Producto')                                             #tendra una etiqueta para el eje X 
    plt.ylabel('Ventas Totales') 
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Convertir a imagen base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    imagen = base64.b64encode(buf.getvalue()).decode('utf8')
    plt.close()
    return render_template('index1.html', imagen=imagen)

#______________________________________________________________________________________________________

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        return f'Bienvenido, {usuario}'
    return '''
    <form mthod="post">
    usuario: <input type="text" name="username">
    <br>
    <input type="submit" value="Enviar">
    </form>'''

#________________________________________________________________________________________________________

@app.route('/grafico_barras_vertical/')
def grafico_barras_vertical():
    categorias = ['Ene', 'Feb', 'Mar', 'Abr']
    valores = [15, 30, 45, 10]

    plt.figure(figsize=(6, 4))
    plt.bar(categorias, valores, color='green')
    plt.title('Ventas por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Ventas')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    imagen = base64.b64encode(buf.getvalue()).decode('utf8')
    return render_template('index1.html', imagen=imagen)

#________________________________________________________________________________________________________

@app.route('/grafico_barras_horizontal/')
def grafico_barras_horizontal():
    productos = ['Producto A', 'Producto B', 'Producto C']
    cantidades = [40, 25, 60]

    plt.figure(figsize=(6, 4))
    plt.barh(productos, cantidades, color='green')
    plt.title('Inventario de Productos')
    plt.xlabel('Cantidad')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    imagen = base64.b64encode(buf.getvalue()).decode('utf8')
    return render_template('index1.html', imagen=imagen)

#_________________________________________________________________________________________________________

@app.route('/grafico_personalizado/')
def grafico_personalizado():
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'may']
    precios = [2000, 2200, 2100, 2500, 2400]

    plt.figure(figsize=(6, 4))
    plt.plot(meses, precios, marker='s', linestyle='--', color='purple')
    plt.title('Evolucion del Precio')
    plt.xlabel('Mes')
    plt.ylabel('Precio en $')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    imagen = base64.b64encode(buf.getvalue()).decode('utf8')
    return render_template('index1.html', imagen=imagen)

#________________________________________________________________________________________________________

@app.route("/ejercicio6/")
def ejercicio6():
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May']
    precios = [2000, 2200, 2500, 2400, 2600]

    plt.figure(figsize=(6, 4))
    plt.plot(meses, precios, marker='s', linestyle='--', color='purple')
    plt.title('Evolucion del precio')
    plt.xlabel('Mes')
    plt.ylabel('Precio en $')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    imagen = base64.b64encode(buf.getvalue()).decode('utf8')
    
    labels = ["Q1", "Q2", "Q3", "Q4"]
    empresa_a = [12000, 15000, 13000, 16000]    
    empresa_b = [10000, 14000, 12000, 17000] 
    return render_template("index1.html", labels=labels, empresa_a=empresa_a, empresa_b=empresa_b, imegen=imagen)